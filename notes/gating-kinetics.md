# Gating kinetics

Phase [1 · Membrane and Hodgkin–Huxley](../phases/p1-membrane-hh/README.md) · status: not started

## Statement

```math
\dot x = \alpha_x(V)(1-x) - \beta_x(V)\,x = \frac{x_\infty(V) - x}{\tau_x(V)},\qquad x\in\{m,h,n\}
```

$\alpha, \beta$ opening and closing rates; $x$ read as a two-state Markov probability.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

`compneuro.membrane.hh_rates` · test: [`tests/test_p1_membrane.py`](../tests/test_p1_membrane.py)

## Related

- [Hodgkin–Huxley membrane equation](hodgkin-huxley.md)
