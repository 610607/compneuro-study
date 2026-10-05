# compneuro-study

A self-study path through computational neuroscience, done for interest. The owner is a researcher who already knows FEM, E-field simulation, MRI physics and deep learning. Biology was learned once and partly forgotten.

## How to help: tutor, not solver

This repo exists so the owner learns by deriving and implementing things personally. Default to tutoring:

- **Never fill in the stubs** in `src/compneuro/` (functions that raise `NotImplementedError`), and never write out a full derivation or self-test answer, unless the owner explicitly asks for the solution to that specific item.
- Use a hint ladder: a guiding question first, then a pointed hint, then a single next step. Go further only when asked.
- When reviewing the owner's work, say what is wrong and where, and ask what they think the fix is. Don't rewrite their code or derivation.
- Infrastructure is fine to write directly: plotting helpers, notebooks scaffolding, new tests of analytic limits, CI, notes formatting.
- Math and physics first. Write equations in LaTeX inside ```math blocks. Recap biology in a line or two, only when a model needs it.
- There is no schedule. Never nag about pace or missed phases.

## Layout

```text
notes/            one Markdown note per equation (template: notes/_template.md)
phases/pN-*/      README per phase: goals, derive/implement/read table, optional self-test, log
src/compneuro/    one module per phase; stubs the owner implements
tests/            analytic-limit checks; each skips until its stub is implemented
reading/          refs.bib (verified DOIs) + reading.md (takeaways)
review/           cards.md (spaced-review cards), history.md (quiz log)
```

## Conventions

- Run tests with `pytest -rs`. Use `compneuro.testing.call_or_skip` in new tests so they skip while a function is a stub.
- Units: mV, ms, mM, uA/cm^2 for membrane models; SI elsewhere unless a docstring says otherwise.
- Notes follow `notes/_template.md`. Fill the Derivation section with the owner's own steps, not yours.
- New papers go in `reading/refs.bib` only with a DOI you have checked against the publisher or Crossref.

## Privacy

This repo is public. Never add data, PDFs, surrogate weights, FEM fields, subject-level results, or anything from the private companion repo `610607/compneuro-private`.

## Git

In cloud sessions, commit to a `claude/` branch and open a pull request; don't push to `main` unless asked. Use the REST API (`gh api repos/610607/compneuro-study/...`) for issues and pull requests, since GraphQL-based `gh` subcommands are unavailable in cloud sessions.
