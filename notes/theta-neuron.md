# Theta neuron (SNIC normal form)

Phase [3 · Nonlinear dynamics](../phases/p3-nonlinear-dynamics/README.md) · status: not started

## Statement

```math
\dot\theta = (1-\cos\theta) + (1+\cos\theta)\,I
```

A spike is $\theta$ passing $\pi$.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

`compneuro.dynamics.theta_neuron_period` · test: [`tests/test_p3_dynamics.py`](../tests/test_p3_dynamics.py)

## Related

- [FitzHugh–Nagumo model](fitzhugh-nagumo.md)
- [Exact mean field for QIF networks (Montbrió–Pazó–Roxin)](mpr-mean-field.md)
