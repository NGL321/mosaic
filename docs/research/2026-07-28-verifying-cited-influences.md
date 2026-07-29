# Verifying the vocabulary's cited influences

**Ticket:** [#13 — Verify the vocabulary's cited influences](https://github.com/NGL321/mosaic/issues/13)
**Map:** [#1 — Founding charter for Mosaic](https://github.com/NGL321/mosaic/issues/1)
**Date:** 2026-07-28
**Provenance Tier:** machine-produced, unverified. Every verdict below rests on a primary document that was read directly — arXiv PDF, publisher landing page, Project Gutenberg or Internet Archive scan of the original edition, or Google Books search-inside on the scanned first edition. Where a primary source could not be reached, the verdict is **Unresolved** and says so. None of these readings has been checked by Noah unaided; discharging that is Verification Debt, logged against the Curriculum in §11.

---

## 0. Summary

Nine attributions were checked. **Four came back clean. Four need wording changes. One is unresolved.** The two worst findings are both in the Least Action / Representation cluster, which is where the file leans hardest.

| Attribution | Verdict | One-line reason |
|---|---|---|
| **Jaynes (1957) + Landauer (1961)** — "the information–thermodynamics identity" | **Loose** | Landauer states a *minimum*, not an identity, and explicitly declines to rest his argument on an entropy–information connection. Jaynes's result is inferential, not physical. |
| **Still, Sivak, Bell & Crooks (2012)** — non-predictive information as dissipated work | **Supported** | Eq. (14) is an equality for instantaneous dissipation; Eq. (18) is a lower bound on the total. Conditions matter and are listed. |
| Representation's line *"structure that is not functional… is dissipated work"* | **Loose** | Still et al. dissipate the non-*predictive* part of retained information. Mosaic's "functional" adds a use-by-the-engine condition the theorem does not carry. |
| **Tishby, Pereira & Bialek (1999) + Still (2014)** — compression against a predictive relevance variable | **Supported** | Tishby et al. are agnostic about the relevance variable; Still (2014) is what makes it the future. The `_After_` line currently credits both for the "predictive" part. |
| **Pearl (1988) + Friston** — Markov blanket | **Supported** | Pearl's coinage, Def. (3.12) p. 97, purely conditional-independence. Friston 2013/2019 do make every blanketed thing free-energy-minimising. The claimed departure is real. |
| **Piaget** — schema / assimilation / accommodation; **Piaget & García (1989)** | **Supported** | *Schème* = generalisable structure of an action, from Piaget's own French; the English collapse is demonstrable in two separate translations; Piaget & García p. 268 says exactly what Mosaic says it says. |
| **Poincaré (1908)** — incubation and the aesthetic sieve | **Supported** | Both are in the essay verbatim. The word *schema* occurs **zero** times in it. The four-stage naming is Wallas (1926), confirmed from Wallas's own text. |
| **Mountcastle (1957; 1978)** + **Horton & Adams (2005)** | **Loose** | Horton & Adams deny a *function*, not existence — correctly cited. But Mountcastle did not frame it as a hypothesis; the hedge is Mosaic's, and the sentence currently reads as if it were his. |
| **Hawkins et al. (2019); Hawkins (2021)** | **Loose** | "The same object" and "vote" are the papers' own. "**Interchangeable** reference frames" is not — and misdescribes the theory, in which each column has a *distinct* location and a *distinct* sensory patch. |
| **Singer & Wu / Hansen & Ghrist** — connection Laplacian as orthogonal-restriction sheaf Laplacian | **Supported** | Hansen & Ghrist state it themselves, §3.6, in one sentence. Two qualifications they add are worth carrying. |
| *Limnaea stagnalis* as the biological root of assimilation/accommodation | **Unresolved** | Could not reach Piaget's 1929 malacology paper. Also: the mollusc work was **not** his thesis — see §6.3. |
| Pohl et al. (2026) / Walker et al. (2023) bibliographic details | **Supported** | Author lists, years, venues and both arXiv numbers check out exactly. |

---

## 1. Jaynes (1957) and Landauer (1961) — **Loose**

### What CONTEXT.md claims

> `_After_: Jaynes (1957) and Landauer (1961) for the information–thermodynamics identity`

### Jaynes

Read from the [reprint scan at bayes.wustl.edu](https://bayes.wustl.edu/etj/articles/theory.1.pdf) of [*Information Theory and Statistical Mechanics*, Phys. Rev. **106**, 620–630 (1957)](https://link.aps.org/doi/10.1103/PhysRev.106.620).

The abstract (p. 620), verbatim in relevant part:

> "Information theory provides a constructive criterion for setting up probability distributions on the basis of partial knowledge, and leads to a type of statistical inference which is called the maximum-entropy estimate… If one considers statistical mechanics as a form of statistical inference rather than as a physical theory, it is found that the usual computational rules, starting with the determination of the partition function, are an immediate consequence of the maximum-entropy principle. In the resulting 'subjective statistical mechanics,' the usual rules are thus justified independently of any physical argument, and in particular independently of experimental verification."

And the closing sentence of the abstract:

> "It is concluded that statistical mechanics need not be regarded as a physical theory dependent for its validity on the truth of additional assumptions not contained in the laws of mechanics… The former consists only of the correct enumeration of the states of a system and their properties; the latter is a straightforward example of statistical inference."

The identification Jaynes does make is of the *functional form*. §2, Eq. (2-3), p. 621:

> "H(p₁ ⋯ pₙ) = −K Σᵢ pᵢ ln pᵢ … Since this is just the expression for entropy as found in statistical mechanics, it will be called the entropy of the probability distribution pᵢ; henceforth we will consider the terms 'entropy' and 'uncertainty' as synonymous."

So Jaynes gives an *epistemic* reading of thermodynamic entropy, and explicitly declines to make statistical mechanics a physical theory. Calling this half of an "information–thermodynamics identity" reads him as asserting something he takes pains to disclaim.

### Landauer

Read from the [IBM Journal reprint scan](https://sites.pitt.edu/~jdnorton/lectures/Rotman_Summer_School_2013/thermo_computing_docs/Landauer_1961.pdf) of [*Irreversibility and Heat Generation in the Computing Process*, IBM J. Res. Dev. **5**, 183–191 (1961)](https://ieeexplore.ieee.org/document/5392446). Two passages are decisive, both from §4, *Logical irreversibility and entropy generation*, p. 188.

First, the result — stated as a **minimum**, with an explicit disclaimer of achievability:

> "Consider a statistical ensemble of bits in thermal equilibrium. If these are all reset to ONE, the number of states covered in the ensemble has been cut in half. The entropy therefore has been reduced by k logₑ 2 = 0.6931 k per bit. The entropy of a closed system, e.g., a computer with its own batteries, cannot decrease; hence this entropy must appear elsewhere as a heating effect, supplying 0.6931 kT per restored bit to the surroundings. **This is, of course, a minimum heating effect, and our method of reasoning gives no guarantee that this minimum is in fact achievable.**"

Second — and this is the uncomfortable one — Landauer explicitly refuses the framing CONTEXT.md attributes to him. Same section, immediately prior:

> "**Note that our argument here does not necessarily depend upon connections, frequently made in other writings, between entropy and information.** We simply think of each bit as being located in a physical system, with perhaps a great many degrees of freedom, in addition to the relevant one."

The paper's own abstract (p. 183) also hedges the constant: "requires a minimal heat generation, per machine cycle, typically of the **order** of kT for each irreversible function." The kT ln 2 figure appears in §4, not the abstract.

### Verdict and proposed wording

**Loose.** "Identity" is wrong twice over: Landauer's result is a bound with a stated gap between bound and achievability, and Jaynes's result is inferential rather than physical. Bundling the two under one label also blurs an epistemology-of-inference paper with a thermodynamics-of-erasure paper.

Does it matter to Mosaic's use? Yes, mildly and in Mosaic's favour. Least Action says "information transformation is a thermodynamic process, so inference is subject to the same variational principle as any other physical process." A *bound* underwrites a variational principle perfectly well — better, in fact, than an identity would, because a variational principle needs something to be extremised against, and Landauer's gap is exactly that. The axiom does not need the stronger claim, so the citation should stop making it.

**Proposed replacement** (applied):

> `_After_: Jaynes (1957) for entropy as an inferential quantity and Landauer (1961) for the thermodynamic cost of erasure — a *bound*, not an identity; Still, Sivak, Bell & Crooks (2012) for retained non-predictive information as dissipated work.`

---

## 2. Still, Sivak, Bell & Crooks (2012) — **Supported**

Read in full from [arXiv:1203.3271v3](https://arxiv.org/abs/1203.3271), *The thermodynamics of prediction*, [Phys. Rev. Lett. **109**, 120604 (2012)](https://doi.org/10.1103/PhysRevLett.109.120604). This is the load-bearing citation and it holds. Here is exactly what it establishes.

### The result, precisely

Define instantaneous memory `I_mem(t) := I[s_t, x_t]` and instantaneous predictive power `I_pred(t) := I[s_t, x_{t+1}]`. The **nostalgia** is their difference — the paper's own gloss: *"It represents useless nostalgia and provides a measure for the ineffectiveness of the model."*

Two distinct results, and the distinction matters:

- **Eq. (14) — an equality, not a bound.** `β⟨W_diss[x_t → x_{t+1}]⟩ = I_mem(t) − I_pred(t)`. The paper's words: *"the instantaneous nonpredictive information is proportional to the average work dissipated while the signal changes from x_t to x_{t+1} … the unwarranted retention of past information is fundamentally equivalent to energetic inefficiency."*
- **Eq. (18) — a lower bound on the total.** `I_mem − I_pred ≤ β⟨W_diss⟩ ≤ β⟨W_ex⟩`. The gap is `−β⟨ΔF_neq^relax⟩ ≥ 0`, the nonequilibrium free energy released during relaxation steps (Eqs. 16–17).

There is also a refinement of Landauer, Eq. (21): `−β⟨Q⟩ ≥ I_e + I_mem − I_pred`, i.e. *"the bound is augmented by the total nostalgia. The system dynamics of a computing device that retains memory therefore must be maximally predictive to approach Landauer's limit."*

### The conditions — these are load-bearing for Mosaic

From the *Problem setup* section, p. 1–2:

1. **Discrete-time Markovian system dynamics** with a **fixed** kernel `p(s_t | s_{t−1}, x_t)`.
2. The system is **in thermodynamic equilibrium at t = 0**, in contact with a heat bath at inverse temperature β, and stays in thermal contact throughout.
3. The drive is stochastic with arbitrary `P_X` — the paper is explicit that it *"require[s] neither that P_X has specific properties, nor that it is known by the system."* This is a genuine strength.
4. **"We assume that there is no feedback from the system to the driving signal."**

Condition 4 is the one Mosaic should be nervous about. An inference engine that *acts* on its environment violates it. Still herself treats the feedback case as a separate and harder problem — see [Still (2014)](https://doi.org/10.3390/e16020968) §4.1, which explicitly scopes itself to *"passive predictive inference, without feedback."* Mosaic's engines are not obviously in scope, and this should be an acknowledged limit rather than a silent extension.

### Does it make prediction "the thermodynamically distinguished behaviour rather than a stipulation"?

**Yes, conditionally** — and the conditional is stated by the authors, not imposed by me. The abstract's own formulation:

> "any system constructed to keep memory about its environment and to operate with maximal energetic efficiency **has to be** predictive."

and the conclusion:

> "any system which is built to have nonzero memory has to be predictive in order to allow for minimal possible dissipation, i.e. to operate at maximal energetic efficiency."

So: given memory, and given a pressure toward energetic efficiency, prediction is forced. It is not a stipulation and it is not merely a modelling convenience — it falls out of the thermodynamics. But a memoryless system is not obliged to predict, and nothing in the paper supplies the efficiency pressure; that has to come from elsewhere (selection, in the biological case, which the *Discussion* gestures at without proving). CONTEXT.md's framing is fair. The `_After_` line as written — "for retained non-predictive information as dissipated work" — is exactly right.

**Verdict: Supported.**

### The over-extension in Representation — **Loose**

Representation currently says:

> "Structure that is not functional is not a representation; under least action it is dissipated work."

Mosaic defines *functional* as "carrying predictive information the engine's inference **actually uses**." Still et al.'s dissipated quantity is `I_mem − I_pred`, and `I_pred = I[s_t, x_{t+1}]` is a mutual information — it requires only that the state *correlate* with the next signal value, not that the system's inference use it. So there is a wedge: information that is predictive but unused is **non-functional in Mosaic's sense and non-dissipated in Still's**. The sentence as written asserts an identification the theorem does not license.

**Proposed replacement** (applied):

> "Structure that is not functional is not a representation; whatever it retains that is not predictive is, under least action, dissipated work."

This keeps the rhetorical force and drops the claim Still et al. do not support.

---

## 3. Tishby, Pereira & Bialek (1999) and Still (2014) — **Supported**

### Tishby et al. are agnostic about the relevance variable

From [arXiv:physics/0004057](https://arxiv.org/abs/physics/0004057), *The Information Bottleneck Method*: relevant information is *"the information that this signal provides about another signal ȳ"*, illustrated with *"the information that face images provide about the names of the people portrayed, or the information that speech sounds provide about the words spoken."* Nothing temporal. The relevance variable is whatever you nominate. **Confirmed agnostic.**

A dating note: the arXiv posting is dated **24 April 2000** and carries no journal-ref. The 1999 date is the 37th Annual Allerton Conference on Communication, Control and Computing, which is the conventional citation and which I did not reach in original. Minor debt; the 1999 date is standard and I would not change it.

### Still (2014) makes the relevance variable the future

The paper is **Susanne Still, *Information Bottleneck Approach to Predictive Inference*, [Entropy 16(2), 968–989 (2014)](https://doi.org/10.3390/e16020968)** — read in full from the publisher PDF. Confirmed decisively at p. 969:

> "The data to be compressed, or summarized, are past experiences, and the summary should be useful for predicting future experiences. **We can thus identify relevant information as information about future data.**"

and the objective itself, Eq. (4), p. 971: maximise `I[s_t, x⃗_t] − λ I[s_t, x⃖_t]` over `p(s_t | x⃖_t)` — compress the past `x⃖_t`, preserve information about the future `x⃗_t`.

**Bibliographic warning:** there is **no arXiv version** of this paper. **arXiv:1205.6447 is a different paper entirely** — Maxim, Saito & Schürmann, *Hirzebruch–Milnor classes of complete intersections*, algebraic geometry. If that number has been noted anywhere in the programme's working files, delete it. CONTEXT.md does not carry it, so nothing to fix there.

### The wording problem

CONTEXT.md credits *both* sources for "compression against a **predictive** relevance variable." Tishby et al. supply the compression-against-a-relevance-variable machinery; the *predictive* specialisation is Still's. Small but real.

**Proposed replacement** (applied):

> `Tishby, Pereira & Bialek (1999) for compression against a relevance variable, and Still (2014) for making that variable the future.`

**Verdict: Supported**, with the credit split corrected.

---

## 4. Pearl (1988) and Friston — **Supported**

### Pearl

Verified against the **scanned first edition** via Google Books search-inside on [*Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference*](https://books.google.com/books/about/Probabilistic_Reasoning_in_Intelligent_S.html?id=AvNID7LyMusC) (Morgan Kaufmann, 1988). Definition (3.12), **p. 97**, §3.3 *Markov networks*:

> "A **Markov blanket** BL_I(a) of an element a ∈ U is any subset S of elements for which I(a, S, U − S − a) and a ∉ S. (3.12) A set is called a **Markov boundary** of a, denoted B_I(a), if it is a minimal Markov blanket of a…"

The book's own index (p. 549) gives *Markov blanket 97, 120–121, 216* and *Markov boundary 97, 99–102*. The construct is purely conditional-independence: `I(a, S, U − S − a)` is Pearl's conditional-independence relation. Coinage confirmed; both terms are his.

**One precision point worth carrying:** in Pearl a Markov blanket is *any* shielding set. The **minimal** one is the Markov **boundary**. CONTEXT.md says only "Pearl (1988) for the blanket as conditional independence," which is correct as written — but if the minimality ever becomes load-bearing, the right word is *boundary*, not *blanket*.

### Friston

Two primary statements, and they are stronger than a reader might expect.

[Friston (2013), *Life as we know it*, J. R. Soc. Interface **10**:20130475](https://doi.org/10.1098/rsif.2013.0475) — abstract:

> "This paper presents a heuristic proof (and simulations of a primordial soup) suggesting that life — or biological self-organization — is an inevitable and emergent property of any (ergodic) random dynamical system that possesses a Markov blanket."

and from §2, *Heuristic proof*: *"any ergodic random dynamical system that possesses a Markov blanket will appear to actively maintain its structural and dynamical integrity"*, with Lemma 2.1 establishing that the flow of internal and active states minimises free energy.

[Friston (2019), *A free energy principle for a particular physics*, arXiv:1906.10184](https://arxiv.org/abs/1906.10184) — abstract:

> "This monograph attempts a theory of every 'thing' that can be distinguished from other things in a statistical sense. The ensuing statistical independencies, mediated by Markov blankets… we recover an information geometry and accompanying free energy principle that allows one to interpret the internal states of something as representing or making inferences about its external states."

### Is CONTEXT.md's departure fair?

**Yes.** In Friston, possessing a Markov blanket is by itself sufficient — for a thing to *be* a thing (individuation) *and* for it to be free-energy-minimising / inference-performing (qualification). "Every blanketed thing is already minimising free energy" is a fair reading of the 2013 lemma. Mosaic's Inference Engine adds a substantive extra requirement — that the internal state carry predictive information beyond what the boundary carries — and so genuinely departs. The `_Departs_` line stands as written.

There is a substantial critical literature on whether Friston's blankets do the work claimed (Biehl et al.; Aguilera et al.; Bruineberg et al.). Per the ticket, that is a separate ticket and was not surveyed here.

**Verdict: Supported.** No change needed.

---

## 5. Piaget — **Supported** (with one unresolved sub-point, §6.3)

### 5.1 *Schème* is the generalisable structure of an action

From Piaget & Inhelder, *La psychologie de l'enfant* (PUF, 1966), p. 11, quoted in the [Fondation Jean Piaget's own vocabulary resource](https://www.fondationjeanpiaget.ch/fjp/site/oeuvre/index_notions_7.php):

> « Un schème est la structure ou l'organisation des actions telles qu'elles se transfèrent ou se généralisent lors de la répétition de cette action en des circonstances semblables ou analogues. »

and from *Études d'épistémologie génétique* vol. 2, p. 46:

> « Nous appelons schèmes sensori-moteurs les organisations sensori-motrices susceptibles d'application à un ensemble de situations analogues. »

Structure of an **action**, defined by transfer and generalisation across analogous circumstances. CONTEXT.md's `_Departs_` line is exact.

### 5.2 The English translation collapses the terms

Demonstrated directly, in two independent translations:

- **Margaret Cook's translation of *The Origins of Intelligence in Children*** (International Universities Press, 1952) — read in full from [this scan](https://sites.pitt.edu/~strauss/origins_r.pdf). Word counts across the whole book: **"schema"/"schemata" — 1,171 occurrences. "scheme" — 0.** Every *schème* in the French becomes *schema* in the English.
- **Gattegno & Hodgson's translation of *Play, Dreams and Imitation in Childhood*** (Routledge, 1951). Their **TRANSLATORS' NOTE**, which defines the handful of terms they consider load-bearing, defines exactly one of the pair:

  > "**Schema.** This word is used to indicate an elementary structure, particularly in the beginnings of psychological life."

  *Scheme* appears nowhere in the volume.

So the collapse is not folklore; it is visible in the primary translations. **Confirmed.**

**Unresolved sub-point:** that Piaget himself used *schéma* as a distinct, figurative term (image/sketch, as against the operative *schème*) is widely asserted in the secondary literature but I could not confirm it from a primary French text within this ticket — the Fondation Jean Piaget's own notion pages define *schème* extensively and never contrast it with *schéma*, and its full-text PDFs of *La formation du symbole* were not reachable. CONTEXT.md's claim is only that "English translation collapses *schème* and *schéma*," which the above establishes for *schème*→*schema*. Logged as debt (§11).

### 5.3 The observations are of children — his own three

Confirmed from Cook's translation of *The Origins of Intelligence in Children*, which is a numbered observation diary. Counts across the volume: **Laurent 407, Jacqueline 273, Lucienne 228** — Piaget's own three children, named throughout. Typical entry, Observation 1:

> "Lucienne and Laurent, a quarter of an hour and a half hour after birth, respectively, had already sucked their hand like this… For some children like Lucienne and Laurent, contact of the lips and probably the tongue with the nipple suffices to produce sucking and swallowing. Other children, such as Jacqueline, have slower coordination…"

**Confirmed.**

### 5.4 Piaget & García (1989)

**Jean Piaget & Rolando García, *Psychogenesis and the History of Science*, trans. Helga Feider, Columbia University Press, 1989** (from the French *Psychogenèse et histoire des sciences*, Flammarion, 1983). Verified via Google Books search-inside on the [Columbia edition](https://books.google.com/books/about/Psychogenesis_and_the_History_of_Science.html?id=xipw247yMTsC). The decisive passage, p. 268:

> "…assimilation of objects or events to the subject's existing schemata. This assimilation is virtually universal. It is true in **all** cases, from the infant's reflexes to the most highly developed forms of **scientific thought**."

and p. 25:

> "…assimilation and accommodation, which determines the internal coherence of the subject. Cognitive structures, inasmuch as they are an organization of knowledge, are essentially comparable to organisms…"

The book's organising thesis is stated as a search for **"common mechanisms"** between psychogenesis and the history of science (chapter headings at pp. 26, 63, 78, 133, 142). Note what this is *not*: it is not a recapitulation or stage-parallelism claim. The correspondence is at the level of mechanism, not content or sequence. CONTEXT.md says "for the same **mechanism** in scientific theory change" — which is precisely and only what the book claims.

**Verdict: Supported.** Translator credit (Feider) and publisher (Columbia UP) both confirmed.

---

## 6. Poincaré (1908), and Wallas (1926) — **Supported**

Read from the Halsted translation in [*The Foundations of Science*, Project Gutenberg #39713](https://www.gutenberg.org/ebooks/39713). "Mathematical Creation" is Book I, Chapter III of *Science and Method*, occupying 462 lines of that text.

### 6.1 The incubation phenomenology is there

> "Most striking at first is this appearance of sudden illumination, a manifest sign of long, unconscious prior work… Often when one works at a hard question, nothing good is accomplished at the first attack. Then one takes a rest, longer or shorter, and sits down anew to the work. During the first half-hour, as before, nothing is found, and then all of a sudden the decisive idea presents itself to the mind… it is more probable that this rest has been filled out with unconscious work."

### 6.2 The aesthetic sieve is there

> "Among the great numbers of combinations blindly formed by the subliminal self, almost all are without interest and without utility; but just for that reason they are also without effect upon the esthetic sensibility. Consciousness will never know them; only certain ones are harmonious, and, consequently, at once useful and beautiful… **Thus it is this special esthetic sensibility which plays the rôle of the delicate sieve of which I spoke**, and that sufficiently explains why the one lacking it will never be a real creator."

with the conclusion he draws from it: *"The useful combinations are precisely the most beautiful."*

### 6.3 "Schema" is absent

Machine count over the 462 lines of the essay: **zero occurrences of "schema", "schemata", or "scheme"** in any form. (Across the entire 1,200,000-character *Foundations of Science* volume the string "scheme" occurs four times, all outside this essay, twice in Royce's introduction.) CONTEXT.md's parenthetical — *"The **word** schema is not his"* — is exactly right.

### 6.4 The four stages are Wallas's

Verified from **Graham Wallas, *The Art of Thought* (Jonathan Cape, 1926)**, read from the [Internet Archive scan](https://archive.org/details/theartofthought). Chapter IV, *Stages of Control*, p. 79–80, in Wallas's own voice:

> "[Helmholtz] gives us three stages in the formation of a new thought. **The first in time I shall call Preparation**, the stage during which the problem was 'investigated … in all directions'; the second is the stage during which he was not consciously thinking about the problem, **which I shall call Incubation**; the third, consisting of the appearance of the 'happy idea' together with the psychological events which immediately preceded and accompanied that appearance, **I shall call Illumination**.
>
> **And I shall add a fourth stage, of Verification**, which Helmholtz does not here mention. Henri Poincaré, for instance, in the book *Science and Method*, which I have already quoted (p. 75), describes in vivid detail the successive stages of two of his great mathematical discoveries…"

and the summary at p. 80: *"the four stages of Preparation, Incubation, Illumination, and the Verification of the final result can generally be distinguished from each other."*

So the naming is unambiguously Wallas's — three stages derived from Helmholtz's 1891 birthday address, a fourth added by Wallas himself, with Poincaré used as corroborating illustration. **The four-stage model is not Poincaré's.**

**One honest qualification, since it cuts slightly against the neatness of that claim:** Poincaré *does* describe all four phases in substance — "some days of voluntary effort", then "a rest… filled out with unconscious work", then "sudden illumination", then *"The need for the second period of conscious work, after the inspiration… but above all is verification necessary."* What is Wallas's is the *segmentation, the naming, and the presentation as a general model of creative thought*. The distinction is real and worth keeping, but it is a distinction about who systematised, not about who first observed.

**Verdict: Supported.** No change to CONTEXT.md needed; the trailing comment is accurate as written.

---

## 7. Mountcastle and Horton & Adams — **Loose**

### Horton & Adams: correctly cited

[Horton, J. C. & Adams, D. L. (2005), *The cortical column: a structure without a function*, Phil. Trans. R. Soc. B **360**, 837–862](https://doi.org/10.1098/rstb.2005.1623), read via [PMC1569491](https://pmc.ncbi.nlm.nih.gov/articles/PMC1569491/). Abstract, verbatim opening:

> "This year, the field of neuroscience celebrates the 50th anniversary of Mountcastle's discovery of the cortical column. In this review, we summarize half a century of research and come to the disappointing realization that the column may have no function."

And the conclusion: *"although the column is an attractive concept, it has failed as a unifying principle for understanding cortical function"*, with the recommendation that *"unravelling the organization of the cerebral cortex will require a painstaking description of the circuits, projections and response properties peculiar to cells in each of its various areas."*

**What it denies: a general function, and the column's status as a unifying explanatory principle. What it does not deny: that columnar structures exist and are demonstrable anatomically.** That is exactly how CONTEXT.md uses it — "a contested one (Horton & Adams, 2005)". **Supported.**

### Mountcastle: the hedge is Mosaic's, not his

This is where the briefing assumption fails. Mountcastle did **not** present columnar organisation as a hypothesis awaiting confirmation.

- His [1978 chapter's title](https://www.semanticscholar.org/paper/An-organizing-principle-for-cerebral-function-:-the-Mountcastle/4fae92cf350729bc89172e6afef7ebda01e99034) is *"An Organizing Principle for Cerebral Function: The Unit Module and the Distributed System"* (in Edelman & Mountcastle, *The Mindful Brain*, MIT Press, 1978) — a principle, offered as such.
- His own retrospective review, [Mountcastle (1997), *The columnar organization of the neocortex*, Brain **120**, 701–722](https://academic.oup.com/brain/article/120/4/701/372118), opens: *"The modular organization of nervous systems is a widely documented principle of design for both vertebrate and invertebrate brains of which the columnar organization of the neocortex is an example."* A documented principle of design, not a conjecture.

CONTEXT.md's sentence reads:

> "Mountcastle's columnar organisation (1957; 1978) for the repeated-unit picture, held as a **hypothesis** and a contested one (Horton & Adams, 2005), never a theorem."

Grammatically the hedge attaches to Mosaic's holding, which is correct and is good discipline. But a reader can easily take "held as a hypothesis" to be a claim about Mountcastle's own framing, which would be false. One word fixes it.

**Proposed replacement** (applied): `…for the repeated-unit picture, held **here** as a **hypothesis** and a contested one (Horton & Adams, 2005), never a theorem.`

**Debt:** I could not reach the full text of Mountcastle (1957), J. Neurophysiol. **20**, 408–434, or the 1978 chapter — both paywalled or print-only. The 1957 conclusion ("the neurons which lie in narrow vertical columns, or cylinders, extending from layer II through layer VI make up an elementary unit of organization") is quoted consistently across the citing literature but I did not read it in original. Logged in §11.

**Verdict: Loose**, on the one-word ambiguity only. The substance is right.

---

## 8. Hawkins et al. (2019) and Hawkins (2021) — **Loose**

Read from the full text of [Hawkins, Lewis, Klukas, Purdy & Ahmad (2019), *A Framework for Intelligence and Cortical Function Based on Grid Cells in the Neocortex*, Front. Neural Circuits **12**:121](https://doi.org/10.3389/fncir.2018.00121). Taking Mosaic's departure paragraph clause by clause.

### (a) Do columns model the same object? — **Yes, and each learns complete objects**

> "We propose that cortical columns are more powerful than currently believed. **Every cortical column learns models of complete objects.** They achieve this by combining input with a grid cell-derived location, and then integrating over movements… every region contains multiple models of objects."

> "**Typically, many columns will be simultaneously observing the same object.** The non-hierarchical connections between columns allow them to rapidly infer the correct object."

**Supported.**

### (b) Is consensus-by-voting the stated mechanism? — **Yes, in those words**

> "We showed how long-range associative connections in the 'object' layer **allow multiple columns to vote on what object they are currently observing**. For example, if we see and touch a coffee cup there will be many columns simultaneously observing different parts of the cup… if the columns are observing the same object, then connections between cells in the object layer allow the columns to rapidly settle on the correct object."

**Supported.** Hawkins (2021), *A Thousand Brains* (Basic Books) carries the same mechanism to the book-length argument — perception as a consensus the columns reach by voting.

### (c) "Interchangeable reference frames" — **not the paper's language, and wrong**

The word "interchangeable" appears **zero times** in the paper. More importantly, the theory says something close to the opposite in two ways.

**First, the columns are not interchangeable.** Immediately after the voting passage:

> "**Every one of these columns has a unique sensory input and a unique location**, and therefore, long-range connections between cells representing location and input do not make sense."

Each column sees a *different patch* of the object and occupies a *different location* in the object's frame. What is shared is the object identity in the L2/3 object layer; that is what votes. If the reference frames were interchangeable, the location-layer connections the paper explicitly rules out would make sense.

**Second, the reference frames are not even all of one kind.** Figure 5 caption:

> "(A) If grid cell modules in the hippocampal complex are anchored by cues in an environment, then grid cell activation patterns will represent locations relative to that environment. (B) If cortical grid cell modules are anchored relative to the body, then they will represent locations in **body space**. (C) If cortical grid cell modules are anchored by cues relative to an object, then they will represent locations in the **object's space**. … Operations performed in (B,C) are associated with 'where' and 'what' regions in the neocortex."

So the framework already carries heterogeneous anchoring — environment, body, object — mapped onto the where/what division.

### What survives, and what has to change

Mosaic's departure survives, and is if anything cleaner once stated accurately. In TBT every column is modelling **an object** — the domain is homogeneous even where the vantage points differ. Mosaic's schemas are heterogeneous **in what they are about**: different problems, not one object seen from many places. And Mosaic's primary observable is where reconciliation *fails*, whereas TBT's voting is designed to make it succeed. Both of those contrasts hold against the corrected description. Only the word "interchangeable" has to go, and it should, because it hands a reader who knows the paper an easy reason to distrust the rest of the paragraph.

**Proposed replacement** (applied):

> "There, many cortical columns model *the same object*, each from its own sensory patch and its own location in an object-anchored reference frame, and vote toward a consensus about which object is present."

**Verdict: Loose.**

---

## 9. Singer & Wu and Hansen & Ghrist — **Supported**

Hansen & Ghrist state the claim themselves, in one sentence. From [*Toward a spectral theory of cellular sheaves*, arXiv:1808.01513](https://arxiv.org/abs/1808.01513) (J. Appl. Comput. Topology **3**, 315–358, 2019), §3.6 *Comparison with previous constructions*:

> "**The graph connection Laplacian, introduced by Singer and Wu in [SW12], is simply the sheaf Laplacian of an O(n)-vector bundle over a graph.**"

The referenced construction is [Singer, A. & Wu, H.-T., *Vector diffusion maps and the connection Laplacian*, Comm. Pure Appl. Math. **65**(8), 1067–1144 (2012)](https://doi.org/10.1002/cpa.21395) — [arXiv:1102.0075](https://arxiv.org/abs/1102.0075) — where the data is *"a weighted graph, where the weights w_ij are accompanied by linear orthogonal transformations O_ij"*, all of the same size d×d.

### Two qualifications Hansen & Ghrist supply, both worth carrying

**(i) "Discrete vector bundle" means invertible restriction maps.** §3.5: *"A subclass of sheaves of particular interest are those where all restriction maps are invertible… we will call it a discrete vector bundle."* Invertibility forces equal stalk dimension across each incidence, which is why the O(n) case has a single ambient dimension n. (Hansen & Ghrist do **not** in general require equal stalk dimensions of sheaves — Figure 1 exhibits two nonisomorphic sheaves with different stalk structure and the same Laplacian. The constraint enters only via the bundle condition.)

**(ii) "Orthogonal" is not quite the right refinement; "orthogonal up to a positive scalar" is.** §3.5, in full:

> "one might wish to define an O(n) discrete vector bundle on a graph to be a cellular sheaf of real vector spaces where all restriction maps are orthogonal. However, from the perspective of the degree-0 Laplacian, a uniform scaling of the inner product on an edge does not change the orthogonality of the bundle, but instead in some sense changes the length of the edge… **So a discrete O(n)-bundle should be one where the restriction maps on each cell are scalar multiples of orthonormal maps.** That is, for each cell σ, we have a positive scalar α_σ, such that for every σ ⊴ τ, the restriction map F_{σ⊴τ} is an orthonormal map times α_τ/α_σ."

They add that for graphs one usually sets α_σ = 1 on 0-cells, *"but this is not necessary. (Indeed, when dealing with the normalized Laplacian of a graph, we have α_v = √d_v.)"*

### The exact qualified statement

> The graph connection Laplacian of Singer & Wu is the degree-0 sheaf Laplacian of a discrete O(n)-vector bundle **over a graph** — a cellular sheaf on a 1-dimensional complex whose restriction maps are all invertible and are orthonormal up to a positive scalar per cell.

CONTEXT.md's sentence — "Singer & Wu's connection Laplacian is the special case of Hansen & Ghrist's sheaf Laplacian in which every map is orthogonal" — is the naive form of exactly the statement Hansen & Ghrist make, and is the form they themselves use in §3.6. The only substantive omission is *over a graph*: sheaf Laplacians are defined on cell complexes of arbitrary dimension, and without that restriction the sentence overstates. **One phrase added** (applied); the scalar-multiple subtlety is left out of CONTEXT.md deliberately, since it is a normalisation convention rather than a change of content, but it is recorded here so the claim can be defended if pressed.

**Verdict: Supported.**

---

## 10. Bibliographic sanity check — Pohl et al. and Walker et al.

Not re-verified for content (already checked in the vocabulary session), but the details were confirmed against the arXiv records:

| Field | CONTEXT.md / ticket | Verified |
|---|---|---|
| Pohl et al. authors | Pohl, Walker, Barack, Lee, Denison, Block, Meyniel & Ma | ✔ Stephan Pohl, Edgar Y. Walker, David L. Barack, Jennifer Lee, Rachel N. Denison, Ned Block, Florent Meyniel, Wei Ji Ma — **order matches** |
| Pohl et al. year / venue | 2026, *Nat Rev Neurosci* 27:357–372 | ✔ Nature Reviews Neuroscience 27, 357–372 (2026), DOI 10.1038/s41583-026-01030-8 |
| Pohl et al. arXiv | 2403.14046 | ✔ [arXiv:2403.14046](https://arxiv.org/abs/2403.14046) |
| Walker et al. year / venue | 2023, *Nat Neurosci* | ✔ Nature Neuroscience (2023), DOI 10.1038/s41593-023-01444-y |
| Walker et al. arXiv | 2202.04324 | ✔ [arXiv:2202.04324](https://arxiv.org/abs/2202.04324) |

**No errors.**

---

## 11. Surviving Verification Debt

To be logged against the Curriculum. Two kinds: sources I could not reach, and derivations Noah would need to be able to defend unaided.

### Sources not reached

1. **Mountcastle (1957)**, J. Neurophysiol. **20**, 408–434, and **Mountcastle (1978)**, *The Mindful Brain* chapter. Both paywalled or print-only. The 1957 conclusion is quoted consistently across the citing literature, and the 1978 chapter's framing is inferable from its title and Mountcastle's own 1997 review, but neither was read in original. *What would settle it:* a library copy of *The Mindful Brain*, or institutional access to J. Neurophysiol.
2. **Piaget (1929)**, *Les races lacustres de la Limnaea stagnalis L.*, Bull. Biol. France Belgique **63**, 424–455. Not reached. The species, the transplant experiment (elongate ↔ globular shell morph under still ↔ turbulent water), and the claim that this work is the biological root of assimilation/accommodation are attested only in secondary sources here. **Also note a probable error in the way this is usually remembered:** Piaget's *doctoral thesis* (1918) was *Introduction à la malacologie valaisanne*, on Valais molluscs generally — the *Limnaea* work is a research programme running from the 1920s, not a thesis. Nothing in CONTEXT.md turns on this, so no edit was made, but the programme should not repeat the "1929 thesis" formulation. *What would settle it:* the 1929 paper itself, or Piaget's *Biologie et connaissance* (1967), where he draws the biology→cognition link in his own voice.
3. **Piaget's own use of *schéma*** as a distinct figurative term. The *schème* side is nailed from primary French; the contrast is not. *What would settle it:* the French text of *La formation du symbole chez l'enfant* (1945) or *L'image mentale chez l'enfant* (1966), checked for whether Piaget uses *schéma* systematically for the figurative/image aspect.
4. **Tishby, Pereira & Bialek**, Proc. 37th Allerton Conference (1999). Only the April 2000 arXiv posting was read. The 1999 date is the conventional citation and is almost certainly right; the proceedings volume itself was not consulted.

### Mathematics and physics Noah would need to defend unaided

5. **Still et al. (2012) Eq. (14).** Deriving `β⟨W_diss[x_t→x_{t+1}]⟩ = H[s_t|x_{t+1}] − H[s_t|x_t] = I_mem(t) − I_pred(t)` requires nonequilibrium free energy as a functional of an arbitrary distribution (their Eq. 8), the Crooks/Jarzynski setting, and the KL-divergence expression for the additional nonequilibrium free energy (Eq. 6). This is the single most load-bearing derivation in the entire vocabulary and it is currently unowned. **Highest-priority item.**
6. **The no-feedback condition.** Still et al. assume no feedback from system to drive. Mosaic's inference engines act. Establishing whether the nostalgia–dissipation result survives feedback — or what replaces it — is a genuine open question for the programme, not just a reading exercise. Still (2014) §4.1 and the interactive-learning line she cites are the entry point.
7. **Sheaf Laplacians and the O(n)-bundle specialisation.** Enough Hodge theory on cell complexes to see why δ² = 0 makes the coboundary a discrete flat connection, and why the scalar-multiple refinement in Hansen & Ghrist §3.5 is forced rather than cosmetic.
8. **Landauer's bound versus the second law.** The gap between "this is a minimum" and "this minimum is achievable" is where the entire thermodynamics-of-computation literature since 1961 lives (Bennett, Norton, Sagawa). Least Action is stated as an axiom and CONTEXT.md declares it out of scope for falsification — but the *bound* language now in the `_After_` line is a promise that the distinction is understood.

---

## Appendix: primary sources read

- Jaynes, E. T. (1957). *Information Theory and Statistical Mechanics.* Phys. Rev. 106, 620–630. https://link.aps.org/doi/10.1103/PhysRev.106.620 (scan: https://bayes.wustl.edu/etj/articles/theory.1.pdf)
- Landauer, R. (1961). *Irreversibility and Heat Generation in the Computing Process.* IBM J. Res. Dev. 5, 183–191. (scan: https://sites.pitt.edu/~jdnorton/lectures/Rotman_Summer_School_2013/thermo_computing_docs/Landauer_1961.pdf)
- Still, S., Sivak, D. A., Bell, A. J. & Crooks, G. E. (2012). *The thermodynamics of prediction.* Phys. Rev. Lett. 109, 120604. https://arxiv.org/abs/1203.3271
- Still, S. (2014). *Information Bottleneck Approach to Predictive Inference.* Entropy 16(2), 968–989. https://doi.org/10.3390/e16020968
- Tishby, N., Pereira, F. C. & Bialek, W. *The Information Bottleneck Method.* https://arxiv.org/abs/physics/0004057
- Pearl, J. (1988). *Probabilistic Reasoning in Intelligent Systems.* Morgan Kaufmann. Def. (3.12), p. 97. https://books.google.com/books/about/Probabilistic_Reasoning_in_Intelligent_S.html?id=AvNID7LyMusC
- Friston, K. (2013). *Life as we know it.* J. R. Soc. Interface 10:20130475. https://pmc.ncbi.nlm.nih.gov/articles/PMC3730701/
- Friston, K. (2019). *A free energy principle for a particular physics.* https://arxiv.org/abs/1906.10184
- Piaget, J. (1952). *The Origins of Intelligence in Children*, trans. M. Cook. https://sites.pitt.edu/~strauss/origins_r.pdf
- Piaget, J. (1951). *Play, Dreams and Imitation in Childhood*, trans. C. Gattegno & F. M. Hodgson. Translators' Note. https://archive.org/details/playdreamsimitat00piag
- Piaget, J. & Inhelder, B. (1966). *La psychologie de l'enfant*, p. 11, via https://www.fondationjeanpiaget.ch/fjp/site/oeuvre/index_notions_7.php
- Piaget, J. & García, R. (1989). *Psychogenesis and the History of Science*, trans. H. Feider. Columbia UP. https://cup.columbia.edu/book/psychogenesis-and-the-history-of-science/9780231059923/
- Poincaré, H. (1908). *Mathematical Creation*, in *Science and Method*, trans. G. B. Halsted, in *The Foundations of Science*. https://www.gutenberg.org/ebooks/39713
- Wallas, G. (1926). *The Art of Thought.* Ch. IV, pp. 79–80. https://archive.org/details/theartofthought
- Mountcastle, V. B. (1997). *The columnar organization of the neocortex.* Brain 120, 701–722. https://academic.oup.com/brain/article/120/4/701/372118 (abstract only)
- Horton, J. C. & Adams, D. L. (2005). *The cortical column: a structure without a function.* Phil. Trans. R. Soc. B 360, 837–862. https://pmc.ncbi.nlm.nih.gov/articles/PMC1569491/
- Hawkins, J., Lewis, M., Klukas, M., Purdy, S. & Ahmad, S. (2019). *A Framework for Intelligence and Cortical Function Based on Grid Cells in the Neocortex.* Front. Neural Circuits 12:121. https://doi.org/10.3389/fncir.2018.00121
- Singer, A. & Wu, H.-T. (2012). *Vector diffusion maps and the connection Laplacian.* Comm. Pure Appl. Math. 65(8), 1067–1144. https://arxiv.org/abs/1102.0075
- Hansen, J. & Ghrist, R. (2019). *Toward a spectral theory of cellular sheaves.* J. Appl. Comput. Topology 3, 315–358. https://arxiv.org/abs/1808.01513
- Pohl, S. et al. (2026). *Clarifying the conceptual dimensions of representation in neuroscience.* Nat. Rev. Neurosci. 27, 357–372. https://arxiv.org/abs/2403.14046
- Walker, E. Y. et al. (2023). *Studying the neural representations of uncertainty.* Nat. Neurosci. https://arxiv.org/abs/2202.04324
