# Balloon–Windkessel haemodynamic model

Phase [5 · Multi-level models](../phases/p5-multilevel-models/README.md) · status: not started

## Statement

```math
\dot s = z - \kappa s - \gamma(f-1),\quad \dot f = s,\quad \tau\dot v = f - v^{1/\alpha},\quad \tau\dot q = \frac{f\,E(f)}{E_0} - \frac{v^{1/\alpha}q}{v},\quad E(f) = 1-(1-E_0)^{1/f}
```

```math
y_{BOLD} = V_0\big[k_1(1-q) + k_2(1-q/v) + k_3(1-v)\big]
```

$z$ neural drive, $s$ vasodilatory signal, $f$ inflow, $v$ blood volume, $q$ deoxyhaemoglobin.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

`compneuro.populations.balloon_windkessel_rhs` · test: [`tests/test_p5_populations.py`](../tests/test_p5_populations.py)

## Related

- [Connectome-coupled whole-brain model](whole-brain-network.md)
- [Mass-univariate fMRI GLM](fmri-glm.md)
- [Dynamic causal modelling](dcm.md)
