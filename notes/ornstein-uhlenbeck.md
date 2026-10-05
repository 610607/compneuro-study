# Ornstein–Uhlenbeck process

Phase [0 · Setup and math warm-up](../phases/p0-setup-math/README.md) · status: not started

## Statement

```math
dX = -\frac{X}{\tau}\,dt + \sigma\,dW
```

$\tau$ correlation time, $\sigma$ noise amplitude, $W$ a Wiener process.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

`compneuro.integrators.euler_maruyama` · test: [`tests/test_p0_integrators.py`](../tests/test_p0_integrators.py)

## Related

- [Fokker–Planck equation for a noisy LIF population](fokker-planck-lif.md)
- [Leaky integrate-and-fire neuron](lif.md)
