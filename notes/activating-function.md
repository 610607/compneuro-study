# Activating function and quasipotential

Phase [2 · Cable theory and TMS](../phases/p2-cable-tms/README.md) · status: not started

## Statement

```math
\psi(s) = -\int^{s}\mathbf E\cdot d\mathbf s,\qquad f(s) = \frac{\partial^2\psi}{\partial s^2} = -\frac{\partial E_\parallel}{\partial s}
```

$E_\parallel$ field component along the fiber. In TMS, $\mathbf E = -\partial_t\mathbf A - \nabla\phi$ is not purely conservative.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

`compneuro.cable.activating_function` · test: [`tests/test_p2_cable.py`](../tests/test_p2_cable.py)

## Related

- [Cable equation with extracellular drive](cable-equation.md)
