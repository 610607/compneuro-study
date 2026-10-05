---
name: derive
description: Guide the owner through deriving one equation from notes/ step by step, Socratically, then record their derivation in the note. Use when asked to derive, work through, or understand where an equation comes from.
---

# Derive an equation with the owner

The argument names a note (e.g. `nernst`, `cable-equation`) or an equation in words. If none is given, ask which note, listing the notes whose Derivation section is still empty.

1. Read the note in `notes/` and its phase README. State the target equation and the starting point you propose (e.g. "from Nernst–Planck with zero flux"). Ask the owner to confirm or pick another starting point.
2. Ask for the first step. Do not supply it.
3. For each step the owner gives:
   - Correct: say so in a line, ask for the next step.
   - Wrong or stuck: climb the hint ladder one rung at a time: a guiding question, then a pointed hint naming the idea needed, then the single next step. Show more only if asked.
   - Check units and signs at every step; ask the owner to check them when they skip it.
4. When the result matches the statement, ask for one analytic limit or sanity check (a special case, a sign, a typical value).
5. Offer to write the owner's derivation, in their own steps, into the note's Derivation, Assumptions and Analytic limits sections, and set `status: derived`. Commit on a `claude/` branch only if the owner agrees.

Keep messages short. Equations in LaTeX. Biology only as a one-line recap when needed.
