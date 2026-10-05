# Linear-Gaussian state space, Kalman filter and LQR

Phase [6 · Coding and control](../phases/p6-coding-control/README.md) · status: not started

## Statement

```math
\mathbf x_{t+1} = A\mathbf x_t + B\mathbf u_t + \mathbf w_t,\qquad \mathbf y_t = C\mathbf x_t + \mathbf v_t,\qquad J = \sum_t\big(\mathbf x_t^\top Q\,\mathbf x_t + \mathbf u_t^\top R\,\mathbf u_t\big)
```

$\mathbf u$ stimulation input, $\mathbf w$, $\mathbf v$ process and observation noise.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

`compneuro.coding.kalman_filter` · test: [`tests/test_p6_coding.py`](../tests/test_p6_coding.py)

## Related

- [Dynamic causal modelling](dcm.md)
- [Phase reduction and the phase response curve](phase-reduction.md)
