"""Phase 6: neural coding, inference and closed-loop control.

Checks in tests/test_p6_coding.py:
    poisson_glm_loglik   peaks near the true parameters on simulated data, and is
                         concave along random lines through parameter space
    kalman_filter        for a scalar random walk, the posterior variance converges
                         to the steady-state Riccati solution
"""

import numpy as np


def poisson_glm_loglik(theta, X, y, dt):
    """Log-likelihood of spike counts y under a Poisson GLM with exponential link.

    lambda_t = exp(X[t] @ theta);  log L = sum_t [ y_t log(lambda_t dt) - lambda_t dt ]
    (dropping the log y_t! term, which does not depend on theta).
    X : (T, p) design matrix; y : (T,) counts; dt : bin width.
    """
    raise NotImplementedError


def kalman_filter(y, A, C, Q, R, x0, P0):
    """Kalman filter for x_{t+1} = A x_t + w_t,  y_t = C x_t + v_t.

    w ~ N(0, Q), v ~ N(0, R); prior x_0 ~ N(x0, P0).
    y : (T, m) observations. Returns (means, covs) of the filtered state,
    shapes (T, n) and (T, n, n).
    """
    raise NotImplementedError
