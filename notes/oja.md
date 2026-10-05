# Oja's rule

Phase [7 · Plasticity](../phases/p7-plasticity/README.md) · status: not started

## Statement

```math
\dot{\mathbf w} = \eta\,y\,(\mathbf x - y\,\mathbf w),\qquad y = \mathbf w\cdot\mathbf x
```

$\eta$ learning rate.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

`compneuro.plasticity.run_oja` · test: [`tests/test_p7_plasticity.py`](../tests/test_p7_plasticity.py)

## Related

- [Spike-timing-dependent plasticity](stdp.md)
