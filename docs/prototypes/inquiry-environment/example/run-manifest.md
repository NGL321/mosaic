# PROTOTYPE — inquiries/172-formation-signature-grokking/runs/2026-08-14-r0e7a91.md
#
# ONE MANIFEST PER RUN. `inquiries/README.md` already fixes most of these fields; this
# prototype adds the `env:` block and nothing else. The block is PER RUN and not per
# Experiment, because the Experiment is its config's sha256 and nothing else — so two runs
# of one Experiment on two base digests are the same Experiment, and may still disagree.
# The manifest is what turns that disagreement into a diagnosis.

run_id: 2026-08-14-r0e7a91
inquiry: 172
config_sha: sha256:8f7e6d5c4b3a29180f7e6d5c4b3a29180f7e6d5c4b3a29180f7e6d5c4b3a2918
seed: 4417
output_sha256: sha256:d4c3b2a1908f7e6d5c4b3a29180f7e6d5c4b3a29180f7e6d5c4b3a29180f7e6d
drive_path: Desk/mosaic/runs/2026-08-14-r0e7a91/

# ---------------------------------------------------------------------------
# THE ENVIRONMENT BLOCK. Written by the runner, never by the job inside the container:
# a container cannot verify its own digest from the inside, so the only party that can
# honestly report what was pulled is the party that pulled it.
# ---------------------------------------------------------------------------
env:
  # What the lock froze. Copied from env.lock so the manifest is readable alone.
  base_digest: sha256:9c1f1a1e4a1f3b8f4d2c5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f708
  lock_sha256: sha256:6d5c4b3a29180f7e6d5c4b3a29180f7e6d5c4b3a29180f7e6d5c4b3a29180f7e

  # What actually ran: base + lock installed. This is the derived image, and it is what
  # the cache is keyed on. Equal to sha256(base_digest || lock_sha256) by construction —
  # recorded anyway, because a mismatch between the key and the pulled digest is the one
  # symptom a poisoned cache would show.
  image_digest: sha256:0319eede2986ae09a39e4add242e0abe6057a4d8ab1ca2b849d6297a3eb62d21
  cache: hit

  # The host boundary, OBSERVED. env.lock states a range; the manifest states the value.
  nvidia_driver: "550.90.07"
  accelerator: "Tesla T4, 16GB"

  # Where it ran. Recorded as fact, never as a constraint — the charter declares a
  # requirement and the loop decides what satisfies it (premise 11).
  runner: github-hosted
  provider: modal
