---
name: check
description: Run the analytic-limit tests for a phase or module, explain failures with hints rather than fixes, and summarize what is implemented. Use when asked to check, test, or see progress on the owner's implementations.
---

# Check the owner's implementations

The argument is a phase number, a module name, or nothing (all phases).

1. Run `pytest -rs` on the matching test file(s), e.g. `pytest -rs tests/test_p1_membrane.py`.
2. Report in a short table: function, status (pass / fail / not implemented yet).
3. For each failure, do not fix the code. Point to the failing check and what it compares (e.g. "ISI vs t_ref + tau ln(RI/(RI - V_th))"), show the observed vs expected numbers, and give the first rung of a hint ladder: a question that narrows down where the discrepancy comes from (units, sign, time step, boundary condition, initial state). Give more hints only when asked.
4. If everything implemented passes, suggest one extra analytic check the owner could add as a test (state the limit, not the code), and point to the phase README's optional self-test.
5. If the owner wants, add a one-line dated entry to the phase README's Log section describing what now passes.
