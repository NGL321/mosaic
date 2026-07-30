# Architecture Decision Records

Numbered, immutable records of decisions that were expensive to reverse, surprising without
context, or the result of a real trade-off. A decision needs all three to earn an ADR;
most decisions do not, and belong in a wayfinder ticket resolution instead.

ADRs are **record** files under [`PROTOCOL.md` §5](../../PROTOCOL.md) — agent-writable.

## Naming

`NNNN-short-slug.md`, numbered in the order they were accepted, never renumbered.

## Superseding

An ADR is never edited to change its decision and never deleted. A decision that no longer
holds gets a **new** ADR that supersedes it, and the old one gains a header line pointing
forward. The record is of what was decided and when, which a rewrite would destroy — the same
reasoning that forbids rebasing a pushed branch.

## Index

A number is reserved when the ADR is written, not when it is planned — an index entry
linking a file that does not exist is a broken link in a document that claims to be a
permanent record.

| # | Title | Status |
|---|---|---|
| 0001 | A private Transcript Archive inside a transparent programme | *not yet written — [#10](https://github.com/NGL321/mosaic/issues/10)* |
