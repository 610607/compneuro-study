# FitzHugh–Nagumo model

Phase [3 · Nonlinear dynamics](../phases/p3-nonlinear-dynamics/README.md) · status: not started

## Statement

```math
\dot v = v - \tfrac{v^3}{3} - w + I,\qquad \dot w = \varepsilon\,(v + a - b\,w)
```

$v$ fast voltage-like variable, $w$ slow recovery variable.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

`compneuro.dynamics.fhn_rhs` · test: [`tests/test_p3_dynamics.py`](../tests/test_p3_dynamics.py)

## Related

- [Hodgkin–Huxley membrane equation](hodgkin-huxley.md)
- [Theta neuron (SNIC normal form)](theta-neuron.md)
- [Phase reduction and the phase response curve](phase-reduction.md)
