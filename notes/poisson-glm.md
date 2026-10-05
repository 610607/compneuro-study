# Poisson GLM for spike trains

Phase [6 · Coding and control](../phases/p6-coding-control/README.md) · status: not started

## Statement

```math
\lambda(t) = \exp\big(\mathbf k\cdot\mathbf x(t) + \mathbf h\cdot\mathbf y_{hist}(t) + b\big),\qquad \log\mathcal L = \sum_t\big[y_t\log(\lambda_t\Delta) - \lambda_t\Delta\big]
```

$\mathbf k$ stimulus filter, $\mathbf h$ spike-history filter, $\Delta$ bin width.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

`compneuro.coding.poisson_glm_loglik` · test: [`tests/test_p6_coding.py`](../tests/test_p6_coding.py)

## Related

- [Mass-univariate fMRI GLM](fmri-glm.md)
- [Fisher information and the Cramér–Rao bound](fisher-information.md)
