#!/usr/bin/env python3
"""PROTOTYPE -- the command surface and dispatch, as one object.

Ticket #232, on Map: The Operation set (#220). Built to be thrown away and
retained as a primary source for how the interface was chosen -- not as a tool.
Nothing runs it, nothing depends on it, and it never touches GitHub, git, or
the network.

    python docs/prototypes/operation-interface/prototype_tui.py

One object, two faces: a human types a key and gets an entry; an agent is
handed the same key as a mandate and its first act is the same call. Four
things are switchable -- dispatch primitive, whether the command writes, what
happens when live state is unreadable, and where a proposal routes -- so the
failures can be made to happen rather than described.
"""

# ---------------------------------------------------------------------------
# THE CELL TABLE. A hand-cut slice of source/, enough to make the interface
# argue. Flags and rulings are copied from the real files, not invented.
# ---------------------------------------------------------------------------

CELLS = {
    "add@vocabulary-entry": dict(
        ruling="in", custody="human-authored", mode="execute",
        steps=["Draft the entry", "Open a pull request", "review"],
        inputs=["ticket", "term"],
    ),
    "propose:add@vocabulary-entry": dict(
        ruling="in", custody="human-authored", mode="propose",
        steps=["Draft the entry", "Open a pull request", "Noah decides"],
        inputs=["ticket", "term"],
    ),
    "regenerate@curriculum-open": dict(
        ruling="in", custody="agent-writable", mode="execute",
        steps=["Cut a branch", "Run tools/snapshot_debt.py", "Commit",
               "Open a pull request", "review"],
        inputs=["ticket"],
        trigger=None,   # THE FILED GAP: nothing fires it (#198, second surface)
    ),
    "add@curriculum-open": dict(
        ruling="null", null_kind="derived",
        reason="the class is origin: generated -- there is nothing to decide",
        redirect="regenerate@curriculum-open",
    ),
    "dispatch@ticket": dict(
        ruling="in", custody="agent-writable", mode="execute",
        steps=["Apply the mandate label", "Record the parent edge"],
        inputs=["ticket", "delegate"],
        couples="close@ticket (after)",
    ),
    "dispatch@map": dict(
        ruling="null", null_kind="stated",
        reason="a mandate over a map has no close -- a map does not resolve",
        redirect="dispatch@ticket",
    ),
    "close@ticket": dict(
        ruling="in", custody="agent-writable", mode="execute",
        actor_override="the dispatcher, never the delegate",
        steps=["Cite the evidence", "Close the ticket"],
        inputs=["ticket", "evidence"],
    ),
    "propose:edit@operation-cell": dict(
        ruling="in", custody="human-authored", mode="propose",
        steps=["State what you were trying to do", "State why nothing fit",
               "Noah decides"],
        inputs=["key", "recommendation"],
    ),
}

# Which live facts each cell's refusals depend on. A cell that needs a fact the
# actor cannot read is not executable there -- that is Q11.
NEEDS_LIVE = {
    "add@vocabulary-entry": ["assignee"],
    "propose:add@vocabulary-entry": ["assignee"],
    "regenerate@curriculum-open": ["assignee", "branch"],
    "dispatch@ticket": ["labels"],
    "close@ticket": ["labels", "assignee"],
}


HUMANS = {"Noah"}


class World:
    def __init__(self):
        self.reset()

    def reset(self):
        self.tickets = {
            300: dict(title="Build the thing", labels=set(), assignee="Noah",
                      state="open", parent=None, dispatcher=None),
        }
        self.next_num = 301
        self.branch = "prototype/232-operation-interface"
        self.mixed_track = False
        self.findings = []
        self.log = []

    def say(self, text):
        self.log.append(text)

    def find(self, sev, text):
        self.findings.append((sev, text))
        self.log.append("  !! %-8s %s" % (sev.upper(), text))

    def root_of(self, num):
        """The WORK root: walk parent edges. Never stored (Q19)."""
        seen, cur = set(), num
        while self.tickets[cur]["parent"] is not None and cur not in seen:
            seen.add(cur)
            cur = self.tickets[cur]["parent"]
        return cur

    def authority_root(self, num):
        """The AUTHORITY root: the nearest ticket DISPATCHED BY a human.

        FOUND BY DRIVING THIS. Q19 said 'store the parent edge, compute the
        root', and the first implementation walked parents and read the root
        ticket's ASSIGNEE -- which is the first DELEGATE, never the human. The
        parent edge is the work tree; the dispatcher is the authority chain,
        and a proposal routes up authority. Returns None when no human appears
        anywhere in the chain, which is a condition dispatch must refuse.
        """
        seen, cur = set(), num
        while cur is not None and cur not in seen:
            seen.add(cur)
            if self.tickets[cur]["dispatcher"] in HUMANS:
                return cur
            cur = self.tickets[cur]["parent"]
        return None

    def actor_of(self, num):
        return self.tickets[num]["assignee"]


W = World()

SW = dict(primitive="label", writes="never", unreadable="refuse", routing="root")


# ---------------------------------------------------------------------------
# THE COMMAND. Renders and refuses. Under the default switches it never writes.
# ---------------------------------------------------------------------------

def operation(key, actor, ticket=None, sandboxed=False):
    W.say("")
    W.say("$ python tools/operation.py %s        [actor: %s%s]"
          % (key, actor, ", sandboxed" if sandboxed else ""))

    cell = CELLS.get(key)

    # 1. THE DOOR. Three outcomes: render, refuse+redirect, catch-all.
    if cell is None:
        return catch_all(key, actor, ticket)

    if cell["ruling"] == "null":
        W.say("  REFUSED  %s null (%s)" % (cell["null_kind"], cell["reason"]))
        W.say("  ->       you want: %s" % cell["redirect"])
        W.say("  (a refusal is a redirect, never a dead end)")
        return "refused"

    # 2. LIVE STATE. Unreadable state is a refusal, not a warning (Q11).
    needed = NEEDS_LIVE.get(key, [])
    if sandboxed and needed:
        if SW["unreadable"] == "refuse":
            W.say("  REFUSED  cannot read %s from here." % ", ".join(needed))
            W.say("           This step is not executable in this context.")
            W.say("           Declare it in inputs: and be handed it.")
            return "refused"
        W.say("  warning  cannot read %s -- continuing." % ", ".join(needed))
        W.find("critical",
               "FALSE GREEN: every refusal keyed to %s silently stopped "
               "firing. Anything that can make state unreadable can make a "
               "refusal not fire -- a control surface, not a degraded check."
               % "/".join(needed))

    # 3. COMPUTABLE FACTS. Mixed track is #176's ruled violation.
    if W.mixed_track and key != "propose:edit@operation-cell":
        W.say("  REFUSED  you are on a mixed-track branch (%s)." % W.branch)
        W.say("  ->       split the branch, then re-enter this key")
        return "refused"

    # 4. CUSTODY. The actor column, derived from the flag.
    if (cell.get("custody") == "human-authored" and actor != "Noah"
            and cell["mode"] == "execute"):
        W.say("  REFUSED  custody: human-authored -- %s may not hold the pen."
              % actor)
        W.say("  ->       you want: propose:%s" % key)
        return "refused"

    # 5. THE ACTOR OVERRIDE, stated rather than derived.
    if cell.get("actor_override") and ticket is not None:
        t = W.tickets[ticket]
        if t["dispatcher"] is not None and actor != t["dispatcher"]:
            W.say("  REFUSED  actor override: %s" % cell["actor_override"])
            W.say("  ->       return it to %s" % t["dispatcher"])
            return "refused"

    # 6. THE BASE CASE. A live-state refusal on the cell, NOT a step in the
    # procedure -- FOUND BY DRIVING THIS. It first sat in dispatch()'s step
    # list, where it fired AFTER the entry had already rendered: the actor was
    # handed a procedure and then told it was void. A step can be skipped and a
    # refusal cannot, so a condition that invalidates the whole cell belongs in
    # the command's refusal set. A chain whose authority root is not a human
    # can still raise a proposal, and premise 19 would have nowhere to send it.
    if key == "dispatch@ticket" and actor not in HUMANS:
        if ticket is None or W.authority_root(ticket) is None:
            W.say("  REFUSED  no human in the authority chain.")
            W.say("           %s was not dispatched by a human, so a proposal "
                  "raised beneath this mandate could not reach one." % actor)
            W.say("  ->       a chain's first dispatch is a human's act")
            return "refused"

    # 7. RENDER. Flat at the point of use.
    W.say("  RENDER   %s   [mode: %s]" % (key, cell["mode"]))
    W.say("           inputs: %s" % ", ".join(cell.get("inputs") or ["--"]))
    for i, s in enumerate(cell["steps"], 1):
        W.say("             %d. %s" % (i, s))
    if cell.get("couples"):
        W.say("           couples: %s" % cell["couples"])
    if "trigger" in cell and cell["trigger"] is None:
        W.find("high", "executor: none -- %s has no trigger. Nothing fires it. "
                       "#236 makes this a hard blocker on the delegability "
                       "check." % key)
    if cell["mode"] == "propose":
        W.say("           GATED ON NOAH. The command renders this; it does not "
              "perform it.")
    return "rendered"


def catch_all(key, actor, ticket):
    W.say("  CATCH-ALL  '%s' does not resolve. Absent, not null -- nobody "
          "looked." % key)
    if actor == "Noah":
        W.say("  ->       interview, then the rendered steps for "
              "propose:add@operation-cell")
        operation("propose:edit@operation-cell", actor, ticket)
    else:
        W.say("  ->       propose-and-escalate: cut a ticket carrying your "
              "recommendation, and stop.")
        if ticket is not None:
            route_proposal(ticket, actor, "no cell for '%s'" % key)
        else:
            W.say("           (no mandate in hand -- nothing to route to)")
    return "catch-all"


# ---------------------------------------------------------------------------
# DISPATCH. The same object, with an agent on the other end.
# ---------------------------------------------------------------------------

def dispatch(dispatcher, delegate, parent_ticket=None, title="a unit of work"):
    W.say("")
    W.say("-- %s dispatches %s --" % (dispatcher, delegate))

    if operation("dispatch@ticket", dispatcher, ticket=parent_ticket) != "rendered":
        return None

    num = W.next_num
    W.next_num += 1
    W.tickets[num] = dict(title=title, labels=set(), assignee=delegate,
                          state="open", parent=parent_ticket,
                          dispatcher=dispatcher)

    # STEP 1 -- the mandate. Who performs it is the whole of switch [w].
    if SW["writes"] == "never":
        W.say("  step 1 performed by %s (has a write bit): label "
              "agent:dispatched on #%d" % (dispatcher, num))
    else:
        W.say("  step 1 performed by THE COMMAND: label agent:dispatched "
              "on #%d" % num)
        W.find("high",
               "the command wrote. The timeline records the tool, not the "
               "actor -- and the write bit stopped being the authorisation. "
               "Q3's answer is what keeps 'who dispatched this' answerable.")
    W.tickets[num]["labels"].add("agent:dispatched")

    # STEP 2 -- the parent edge. Stored; the root is computed (Q19).
    W.say("  step 2 performed by %s: parent edge #%s recorded on #%d"
          % (dispatcher, parent_ticket, num))

    if SW["primitive"] == "invocation":
        W.tickets[num]["labels"].discard("agent:dispatched")
        W.find("high",
               "bare invocation: the mandate exists nowhere. Open mandates are "
               "not discoverable (premise 20), dispatch-owes-a-close cannot be "
               "checked, and re-dispatch leaves no act by a named actor.")

    W.say("  #%d dispatched to %s   [root: #%d]"
          % (num, delegate, W.root_of(num)))
    return num


def work(num):
    """The delegate does its unit. Labels command, comments report."""
    t = W.tickets[num]
    W.say("")
    W.say("-- #%d: %s runs its mandate --" % (num, t["assignee"]))
    t["labels"].discard("agent:dispatched")
    t["labels"].add("agent:in-progress")
    W.say("  agent:dispatched consumed by the run answering it; "
          "agent:in-progress applied")
    W.say("  the delegate re-enters the command once per write "
          "(a Ralph iteration is one key, never a bundle)")
    operation("regenerate@curriculum-open", t["assignee"], ticket=num)


def report(num, kind):
    """The return: a structured comment on the dispatching ticket (Q13)."""
    t = W.tickets[num]
    actor = t["assignee"]
    W.say("")
    W.say("-- #%d: %s returns [%s] --" % (num, actor, kind))
    W.say("  comment on #%d:" % num)
    W.say("    keys entered   : regenerate@curriculum-open")
    W.say("    addresses      : curriculum/open.md")
    W.say("    evidence       : PR #%d" % (900 + num % 100))
    W.say("    stopped at     : step 5 'review' -- not my step")
    W.say("  (that last field is a RESULT, not a failure -- #224's delegate "
          "stopped correctly)")

    if kind == "close":
        # Q8/Q18: a close pops ONE frame.
        W.say("  proposed close routes ONE HOP -> %s" % t["dispatcher"])
        operation("close@ticket", t["dispatcher"], ticket=num)
        t["state"] = "closed"
        t["labels"].discard("agent:in-progress")
    else:
        route_proposal(num, actor, "a novel refusal, not recorded in the set")


def route_proposal(num, actor, why):
    """Q18: a propose jumps to the ROOT, which is always a human."""
    root = W.authority_root(num)
    parent = W.tickets[num]["dispatcher"]
    W.say("  PROPOSAL raised by %s (%s)" % (actor, why))
    if SW["routing"] == "root":
        if root is None:
            W.find("critical", "unroutable proposal: no human in the authority "
                               "chain. This is why the base case is checked at "
                               "DISPATCH and not here.")
            return
        W.say("  routes to the AUTHORITY ROOT: #%d, dispatched by %s"
              % (root, W.tickets[root]["dispatcher"]))
        W.say("  (computed by walking parent edges and reading the DISPATCHER, "
              "never the assignee -- and never stored)")
        W.say("  Noah sees it. propose:edit@operation-cell is his to execute.")
    else:
        W.say("  routes ONE HOP: to %s" % parent)
        if parent != "Noah":
            W.find("critical",
                   "%s is an agent and may execute propose cells that arrive "
                   "here. A chain of agents each passes the proposal to another "
                   "agent -- premise 19 holds formally ('it was escalated') and "
                   "is false in practice: no new way to interface with this "
                   "project reached Noah." % parent)


# ---------------------------------------------------------------------------
# THE SCREEN
# ---------------------------------------------------------------------------

BANNER = """
=============================================================================
 PROTOTYPE  #232 -- the command surface and dispatch, as ONE object
=============================================================================
"""

MENU = """
 EVENTS
  1  agent-A runs  add@vocabulary-entry       (custody refuses -> propose)
  2  agent-A runs  add@curriculum-open        (a derived null -> redirect)
  3  agent-A runs  dispatch@map               (a stated null -> redirect)
  4  agent-A runs  frobnicate@ticket          (the door: absent -> catch-all)
  5  Noah dispatches agent-A                  (the mandate)
  6  agent-A dispatches agent-B               (an agent dispatches an agent)
  7  agent-B works, and returns a CLOSE       (one hop)
  8  agent-B works, and returns a PROPOSAL    (to the root)
  9  agent-B runs the command FROM A SANDBOX  (live state unreadable)
  0  agent-A dispatches with NO human above it  (the base case)
  d  agent-B closes ITS OWN mandate           (self-certification)

 SWITCHES
  t  dispatch primitive .... %-12s (label | invocation)
  w  the command writes .... %-12s (never | mandate)
  u  unreadable state ...... %-12s (refuse | warn)
  p  proposal routing ...... %-12s (root | hop)
  b  mixed-track branch .... %-12s

 c  run the chain: 5, 6, then 8      s  show state      z  reset      q  quit
"""


def screen():
    print(BANNER)
    print(MENU % (SW["primitive"], SW["writes"], SW["unreadable"],
                  SW["routing"], "on" if W.mixed_track else "off"))
    print(" TICKETS")
    for n in sorted(W.tickets):
        t = W.tickets[n]
        ar = W.authority_root(n)
        print("  #%d  %-18s %-8s %-7s parent=%-5s work=#%-4d auth=%-5s [%s]"
              % (n, t["title"][:18], t["assignee"], t["state"], t["parent"],
                 W.root_of(n), ("#%d" % ar) if ar else "NONE",
                 ",".join(sorted(t["labels"])) or "-"))
    print("")
    for line in W.log[-30:]:
        print(line)
    if W.findings:
        print("")
        print(" FINDINGS THIS RUN: %d" % len(W.findings))


def chain():
    a = dispatch("Noah", "agent-A", None, "the parent unit")
    if a is None:
        return
    b = dispatch("agent-A", "agent-B", a, "the child unit")
    if b is None:
        return
    work(b)
    report(b, "proposal")


ACTIONS = {
    "1": lambda: operation("add@vocabulary-entry", "agent-A", 300),
    "2": lambda: operation("add@curriculum-open", "agent-A", 300),
    "3": lambda: operation("dispatch@map", "agent-A", 300),
    "4": lambda: operation("frobnicate@ticket", "agent-A", 300),
    "5": lambda: dispatch("Noah", "agent-A", None, "the parent unit"),
    "6": lambda: dispatch("agent-A", "agent-B", max(W.tickets), "the child unit"),
    "7": lambda: (work(max(W.tickets)), report(max(W.tickets), "close")),
    "8": lambda: (work(max(W.tickets)), report(max(W.tickets), "proposal")),
    "9": lambda: operation("regenerate@curriculum-open", "agent-B",
                           max(W.tickets), sandboxed=True),
    "0": lambda: dispatch("agent-A", "agent-B", None, "an orphan unit"),
    "d": lambda: operation("close@ticket", W.tickets[max(W.tickets)]["assignee"],
                           ticket=max(W.tickets)),
    "c": chain,
}

TOGGLES = {
    "t": ("primitive", ["label", "invocation"]),
    "w": ("writes", ["never", "mandate"]),
    "u": ("unreadable", ["refuse", "warn"]),
    "p": ("routing", ["root", "hop"]),
}


def main():
    while True:
        screen()
        try:
            k = input("\n > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("")
            return
        if k == "q":
            return
        if k == "z":
            W.reset()
        elif k == "b":
            W.mixed_track = not W.mixed_track
        elif k in TOGGLES:
            field, vals = TOGGLES[k]
            SW[field] = vals[(vals.index(SW[field]) + 1) % len(vals)]
        elif k in ACTIONS:
            ACTIONS[k]()


if __name__ == "__main__":
    main()
