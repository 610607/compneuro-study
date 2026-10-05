---
name: tutor-review
description: Review a pull request or branch of the owner's implementation against the matching note and tests, and leave hints rather than fixes. Use for PR review, or when asked to review the owner's work.
---

# Tutor review of a pull request

The argument is a pull request number, or nothing to review the current branch against `main`.

1. Get the diff: `gh api repos/610607/compneuro-study/pulls/<n>/files` for a PR, or `git diff main...HEAD` for a branch. Identify which `src/compneuro` functions and notes changed.
2. Run `pytest -rs` and note which checks now pass, fail or still skip.
3. For each changed function, compare it with its note's statement and the module docstring: equation terms, signs, units, boundary and initial conditions, numerical method and step size.
4. Write the review as hints, not fixes:
   - What is correct (briefly).
   - Each problem: where it is (file and line), what is off, and a guiding question toward the fix. Never paste corrected code.
   - One suggestion for an extra analytic check, stated as a limit, not code.
5. Post it as a single review comment on the PR: `gh api repos/610607/compneuro-study/pulls/<n>/reviews -f event=COMMENT -f body="..."`. If posting fails, print the review in the session instead.

Do not push commits to the owner's branch.
