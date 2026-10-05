# Phase 1 · Membrane biophysics and Hodgkin–Huxley

By the end you can write Hodgkin–Huxley from a blank page, explain every term physically, and reproduce its classic behaviours in your own code.

*Bio recap:* the lipid bilayer acts as a capacitor (about 1 μF/cm²), ion channels act as voltage-dependent conductances, and pumps keep Na⁺ concentrated outside and K⁺ inside.

**Notes:** [Nernst–Planck](../../notes/nernst-planck.md) · [Nernst](../../notes/nernst.md) · [GHK](../../notes/ghk.md) · [Hodgkin–Huxley](../../notes/hodgkin-huxley.md) · [gating kinetics](../../notes/gating-kinetics.md)

**Code:** `src/compneuro/membrane.py` · checks in `tests/test_p1_membrane.py`

| Derive | Implement | Read |
| --- | --- | --- |
| Nernst–Planck to Nernst; GHK from the constant-field assumption | GHK calculator; sensitivity of resting potential to extracellular K⁺ | Plonsey & Barr, membrane potential chapters; Johnston & Wu, ion movement |
| Membrane as an RC circuit; charging time course | Passive membrane step response vs the analytic exponential | Dayan & Abbott ch. 5 |
| HH gating kinetics; steady states and time constants | HH from scratch (RK4, checked against SciPy): threshold, refractoriness, anode break, f–I curve | Ermentrout & Terman ch. 1; Gerstner ch. 2 |
| Channels as Markov chains; master equation | Stochastic channels with the Gillespie algorithm; spike-time jitter vs channel count | Johnston & Wu, single-channel kinetics |

## Self-test (optional)

- [ ] Write GHK and HH from memory, with units for every term
- [ ] Reproduce threshold, refractoriness, anode-break excitation and the f–I curve
- [ ] Set τ_n = τ_m, simulate, and explain what happens to the spike
- [ ] Explain why the Cl⁻ concentrations are swapped in GHK

## Log

<!-- A line now and then: what you derived, what you built, where you got stuck. -->
