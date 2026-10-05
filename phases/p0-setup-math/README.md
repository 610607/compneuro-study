# Phase 0 · Setup and math warm-up

Set up the tools, then refresh the two math areas most likely to be rusty: nonlinear ODEs and stochastic processes.

| Task | Read |
| --- | --- |
| Clone both repos, create the environment (`conda env create -f environment.yml`), run `pytest -rs` | — |
| Connect your fMRI pipeline (nibabel, nilearn); pick one resting-state and one task dataset (your own kept in the private repo's data folder, or open ones from OpenNeuro) for Phases 5 and 6 | — |
| Linear systems, eigenvalues and stability; Euler vs RK4 vs implicit solvers, stiffness | Strogatz ch. 2, 5 |
| Poisson process, Gaussian white noise, Langevin equations, Euler–Maruyama; Itô vs Stratonovich at a working level | Gardiner, *Stochastic Methods*, early chapters |
| Start [review/cards.md](../../review/cards.md), if spaced repetition suits you | — |

**Notes:** [Ornstein–Uhlenbeck process](../../notes/ornstein-uhlenbeck.md)

**Code:** `src/compneuro/integrators.py` · checks in `tests/test_p0_integrators.py`

**Worked example of the test pattern:** `tests/test_p0_example.py`

## Self-test (optional)

- [ ] Integrate a stiff 2D linear system with explicit Euler and with an implicit solver, and explain why one blows up
- [ ] Simulate an Ornstein–Uhlenbeck process and match its stationary variance to the analytic value

## Log

<!-- A line now and then: what you derived, what you built, where you got stuck. -->
