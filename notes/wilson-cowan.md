# Wilson–Cowan equations

Phase [5 · Multi-level models](../phases/p5-multilevel-models/README.md) · status: not started

## Statement

```math
\tau_E\dot E = -E + S(w_{EE}E - w_{EI}I + h_E),\qquad \tau_I\dot I = -I + S(w_{IE}E - w_{II}I + h_I)
```

$E$, $I$ excitatory and inhibitory population activity, $S$ sigmoid.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

`compneuro.populations.wilson_cowan_rhs` · test: [`tests/test_p5_populations.py`](../tests/test_p5_populations.py)

## Related

- [Exact mean field for QIF networks (Montbrió–Pazó–Roxin)](mpr-mean-field.md)
- [Amari neural field](amari-neural-field.md)
- [Connectome-coupled whole-brain model](whole-brain-network.md)
