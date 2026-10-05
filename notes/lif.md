# Leaky integrate-and-fire neuron

Phase [4 · Noise and networks](../phases/p4-noise-networks/README.md) · status: not started

## Statement

```math
\tau_m\dot V = -(V - E_L) + R\,I(t),\qquad V \ge V_{th}\;\Rightarrow\;V \to V_{reset}
```

$\tau_m$ membrane time constant, $R$ input resistance.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

`compneuro.spiking.simulate_lif` · test: [`tests/test_p4_spiking.py`](../tests/test_p4_spiking.py)

## Related

- [Fokker–Planck equation for a noisy LIF population](fokker-planck-lif.md)
- [Ornstein–Uhlenbeck process](ornstein-uhlenbeck.md)
