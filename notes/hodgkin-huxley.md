# Hodgkin–Huxley membrane equation

Phase [1 · Membrane and Hodgkin–Huxley](../phases/p1-membrane-hh/README.md) · status: not started

## Statement

```math
C_m\frac{dV}{dt} = -\bar g_{Na}m^3h\,(V-E_{Na}) - \bar g_K n^4\,(V-E_K) - g_L(V-E_L) + I
```

$\bar g$ maximal conductances, $m, h, n$ gating variables, $E$ reversal potentials.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

`compneuro.membrane.simulate_hh` · test: [`tests/test_p1_membrane.py`](../tests/test_p1_membrane.py)

## Related

- [Gating kinetics](gating-kinetics.md)
- [Goldman–Hodgkin–Katz voltage equation](ghk.md)
- [FitzHugh–Nagumo model](fitzhugh-nagumo.md)
