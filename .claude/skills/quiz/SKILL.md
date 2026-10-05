---
name: quiz
description: Run a short spaced-review quiz from review/cards.md, one card at a time, and log results to review/history.md. Use when asked to quiz, review, or practise recall.
---

# Spaced-review quiz

The argument is the number of cards (default 5) and optionally a phase.

1. Read `review/cards.md` (equation cards and question cards) and `review/history.md`.
2. Pick cards: first any marked `missed` in the last two entries of history, then cards never quizzed, then the least recently quizzed. Restrict to the phase if one was given. Prefer phases the owner has started (phase README logs or implemented functions).
3. Ask one card at a time:
   - Equation card: give the name; the owner writes the equation. Compare term by term, including signs and factors. Reveal the reference form only after their attempt.
   - Question card: ask it; evaluate the owner's answer for correctness and completeness. If it is wrong, give a hint and let them try once more before explaining.
4. At the end, append a dated line to `review/history.md` in the form `- YYYY-MM-DD: got <names>; missed <names>`, and offer to commit it on a `claude/` branch.

Keep each message to the card and your verdict.
