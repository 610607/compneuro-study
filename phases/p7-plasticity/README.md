# Phase 7 · Plasticity and learning

Short, because learning rules overlap with deep learning. The new part is how stimulation patterns can drive plasticity.

**Notes:** [Oja's rule](../../notes/oja.md) · [STDP](../../notes/stdp.md)

**Code:** `src/compneuro/plasticity.py` · checks in `tests/test_p7_plasticity.py`

| Derive | Implement | Read |
| --- | --- | --- |
| Instability of plain Hebbian learning; Oja convergence; BCM sliding threshold | Oja's rule recovers the first principal component of synthetic data | Dayan & Abbott ch. 8 |
| STDP; calcium-based plasticity | STDP in a Brian2 network driven by correlated input | Gerstner ch. 19; Graupner & Brunel 2012 |
| Plasticity models of repetitive TMS protocols such as theta burst | Toy model: pulse pattern to plasticity outcome | Look for a current modeling review when you get here |

## Self-test (optional)

- [ ] Prove that Oja's rule drives ‖w‖ to 1
- [ ] Show in simulation how pulse timing relative to postsynaptic spikes flips the sign of Δw

## Log

<!-- A line now and then: what you derived, what you built, where you got stuck. -->
