# Fokker–Planck equation for a noisy LIF population

Phase [4 · Noise and networks](../phases/p4-noise-networks/README.md) · status: not started

## Statement

```math
\tau\,\partial_t P = \partial_V\big[(V-\mu)P\big] + \tfrac{\sigma^2}{2}\,\partial_V^2 P,\qquad P(V_{th},t) = 0,\quad \nu(t) = -\tfrac{\sigma^2}{2\tau}\,\partial_V P\big|_{V_{th}}
```

$P(V,t)$ membrane-potential density, $\nu$ population firing rate. Probability leaving at threshold re-enters at reset.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

no stub; write your own module or notebook

## Related

- [Leaky integrate-and-fire neuron](lif.md)
- [Ornstein–Uhlenbeck process](ornstein-uhlenbeck.md)
- [Exact mean field for QIF networks (Montbrió–Pazó–Roxin)](mpr-mean-field.md)
