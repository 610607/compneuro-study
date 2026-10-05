---
name: weekly-review
description: Open a GitHub issue with this week's spaced-review cards for the owner to answer asynchronously. Intended for a scheduled routine; also usable by hand.
---

# Weekly review issue

1. Read `review/cards.md`, `review/history.md`, the phase README logs and which `src/compneuro` functions are implemented (stubs raise `NotImplementedError`).
2. Pick 5 cards, preferring: cards missed recently, cards from phases the owner has started, then cards never reviewed. If no phase has been started, pick from Phases 0 and 1.
3. Open one issue with the REST API:
   `gh api repos/610607/compneuro-study/issues -f title="Review: week of YYYY-MM-DD" -f body="..." -f "labels[]=review"`
   Body: a short intro line, then the cards as a checklist. Equation cards show only the name; question cards show the question. No answers. End with: "Answer in a comment; ask Claude to grade it with /quiz or in a session."
4. If an open review issue from an earlier week has comments with answers, grade them in a reply comment on that issue (hints for anything wrong, no full solutions) and append the result to `review/history.md` on a `claude/` branch with a pull request.
5. If posting fails, print the cards in the session instead.

Never include answers or solutions in the issue.
