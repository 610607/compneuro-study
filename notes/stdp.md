# Spike-timing-dependent plasticity

Phase [7 · Plasticity](../phases/p7-plasticity/README.md) · status: not started

## Statement

```math
\Delta w = \begin{cases} A_+e^{-\Delta t/\tau_+} & \Delta t > 0 \\ -A_-e^{\Delta t/\tau_-} & \Delta t < 0 \end{cases},\qquad \Delta t = t_{post} - t_{pre}
```

$A_\pm$ amplitudes, $\tau_\pm$ window time constants.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

`compneuro.plasticity.stdp_dw` · test: [`tests/test_p7_plasticity.py`](../tests/test_p7_plasticity.py)

## Related

- [Oja's rule](oja.md)
