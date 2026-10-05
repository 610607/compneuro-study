# Dynamic causal modelling

Phase [6 · Coding and control](../phases/p6-coding-control/README.md) · status: not started

## Statement

```math
\dot{\mathbf z} = \Big(A + \sum_j u_j B^{(j)}\Big)\mathbf z + C\mathbf u,\qquad \mathbf y = g(\mathbf z, \theta_h) + \boldsymbol\varepsilon
```

$A$ intrinsic coupling, $B^{(j)}$ input-dependent modulation, $C$ driving inputs, $g$ haemodynamic observation model.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

no stub; write your own module or notebook

## Related

- [Linear-Gaussian state space, Kalman filter and LQR](state-space-lqr.md)
- [Balloon–Windkessel haemodynamic model](balloon-windkessel.md)
- [Mass-univariate fMRI GLM](fmri-glm.md)
