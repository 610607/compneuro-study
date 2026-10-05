# Cable equation with extracellular drive

Phase [2 · Cable theory and TMS](../phases/p2-cable-tms/README.md) · status: not started

## Statement

```math
\lambda^2\frac{\partial^2V_m}{\partial s^2} - \tau_m\frac{\partial V_m}{\partial t} - V_m = -\lambda^2\frac{\partial^2\psi}{\partial s^2},\qquad \lambda=\sqrt{\frac{R_m d}{4R_i}},\quad \tau_m = R_m C_m
```

$V_m$ transmembrane potential, $s$ fiber coordinate, $\psi$ extracellular quasipotential, $R_m$, $R_i$ membrane and axial resistivity, $d$ diameter.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

`compneuro.cable.steady_state_cable` · test: [`tests/test_p2_cable.py`](../tests/test_p2_cable.py)

## Related

- [Activating function and quasipotential](activating-function.md)
- [Hodgkin–Huxley membrane equation](hodgkin-huxley.md)
