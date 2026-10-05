# Phase 2 · Cable theory and extracellular / TMS stimulation

Links E-field work to neural activation. By the end you can predict where a fiber depolarizes from the field along it.

*Bio recap:* axons and dendrites are thin resistive cores in a leaky sheath. Myelin cuts membrane conductance and capacitance between nodes of Ranvier. In cortex, TMS-relevant targets include pyramidal-cell axons, their terminals and their bends.

**Notes:** [cable equation](../../notes/cable-equation.md) · [activating function](../../notes/activating-function.md)

**Code:** `src/compneuro/cable.py` · checks in `tests/test_p2_cable.py`

| Derive | Implement | Read |
| --- | --- | --- |
| Cable equation from Kirchhoff's laws; λ and τ_m; Green's function of the infinite cable | Finite-difference passive cable; check the steady-state e^(−\|x\|/λ) decay | Johnston & Wu, cable theory; Dayan & Abbott ch. 6 |
| Activating function; sealed-end boundary term proportional to E_∥ | Straight and bent axons in uniform and graded fields | Rattay 1986; Plonsey & Barr, stimulation chapters |
| Quasi-static induction E = −∂A/∂t − ∇φ; quasipotential; filtering of the pulse waveform by the membrane | Reproduce Roth & Basser's threshold vs coil position (own code, then NEURON's extracellular mechanism) | Roth & Basser 1990; NEURON extracellular-stimulation tutorials |
| Myelinated axon (node + internode); strength–duration curve | Mini-project A1 (in the private repo) | Aberra et al. 2018 |

**Mini-project A1 (optional):** compare activation thresholds from FEM and surrogate fields along straight and bent fibers. It uses unpublished fields, so it lives in `compneuro-private/capstones/a1-field-to-threshold/` and imports this repo's `compneuro.cable`.

## Self-test (optional)

- [ ] Derive the cable equation with extracellular drive, including the sealed-end boundary condition
- [ ] Predict, before simulating, where a straight and a bent axon depolarize and hyperpolarize in a uniform field
- [ ] Reproduce the Roth & Basser threshold trend
- [ ] A1: one plot of threshold error vs E-field error, FEM vs surrogate

## Log

<!-- A line now and then: what you derived, what you built, where you got stuck. -->
