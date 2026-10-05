# Phase 3 · Nonlinear dynamics and reduced neuron models

The language every later model is analysed in: phase planes, bifurcations and phase response.

**Notes:** [FitzHugh–Nagumo](../../notes/fitzhugh-nagumo.md) · [theta neuron](../../notes/theta-neuron.md) · [phase reduction](../../notes/phase-reduction.md)

**Code:** `src/compneuro/dynamics.py` · checks in `tests/test_p3_dynamics.py`

| Derive | Implement | Read |
| --- | --- | --- |
| 1D and 2D flows; nullclines; linearization and fixed-point classification | Phase-plane tool: vector field, nullclines, trajectories | Strogatz ch. 2–3, 5–6 |
| FitzHugh–Nagumo and Morris–Lecar; reduction from HH | Excitable vs oscillatory regimes as I varies | Izhikevich ch. 4–5; Ermentrout & Terman ch. 3 |
| Saddle-node, SNIC and Hopf bifurcations; class I vs II excitability; theta neuron | Bifurcation diagrams (XPPAUT/AUTO, or parameter sweeps in Python) | Strogatz ch. 7–8; Izhikevich ch. 6–7 |
| Phase reduction; PRC; weak coupling and phase locking | PRC computed two ways (direct perturbation and adjoint); locking to a periodic pulse train | Izhikevich ch. 10; Ermentrout & Terman ch. 8 |

## Self-test (optional)

- [ ] Classify a new 2D model's excitability class from its phase plane alone
- [ ] Compute a PRC two ways and show that they agree
- [ ] Explain why a class I neuron can fire arbitrarily slowly but a class II neuron can't
- [ ] Predict the phase at which a pulse train locks an oscillator, then confirm it by simulation

## Log

<!-- A line now and then: what you derived, what you built, where you got stuck. -->
