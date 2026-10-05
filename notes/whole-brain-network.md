# Connectome-coupled whole-brain model

Phase [5 · Multi-level models](../phases/p5-multilevel-models/README.md) · status: not started

## Statement

```math
\dot{\mathbf x}_i = F(\mathbf x_i) + G\sum_j C_{ij}\,\mathbf x_j(t - d_{ij}/v) + \boldsymbol\xi_i(t)
```

$F$ local neural-mass dynamics, $G$ global coupling, $C_{ij}$ connectome weights, $d_{ij}$ tract lengths, $v$ conduction speed.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

no stub; write your own module or notebook

## Related

- [Wilson–Cowan equations](wilson-cowan.md)
- [Balloon–Windkessel haemodynamic model](balloon-windkessel.md)
- [Dynamic causal modelling](dcm.md)
