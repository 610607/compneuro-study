"""Phase 6 checks: Poisson GLM likelihood and the steady-state Kalman filter."""

import numpy as np

from compneuro import coding
from compneuro.testing import call_or_skip


def _simulated_glm(rng, T=20000, dt=0.01):
    X = np.column_stack([np.ones(T), rng.standard_normal((T, 2))])
    theta = np.array([np.log(20.0), 0.5, -0.3])  # 20 Hz baseline, two covariates
    y = rng.poisson(np.exp(X @ theta) * dt)
    return X, y, theta, dt


def test_glm_loglik_peaks_near_true_parameters():
    rng = np.random.default_rng(1)
    X, y, theta, dt = _simulated_glm(rng)
    best = call_or_skip(coding.poisson_glm_loglik, theta, X, y, dt)
    for _ in range(20):
        assert coding.poisson_glm_loglik(theta + 0.3 * rng.standard_normal(3), X, y, dt) < best


def test_glm_loglik_is_concave_along_lines():
    rng = np.random.default_rng(4)
    X, y, theta, dt = _simulated_glm(rng)
    L = lambda th: call_or_skip(coding.poisson_glm_loglik, th, X, y, dt)
    for _ in range(10):
        a, b = theta + 0.5 * rng.standard_normal(3), theta + 0.5 * rng.standard_normal(3)
        mid = L((a + b) / 2)
        assert mid >= (L(a) + L(b)) / 2 - 1e-9 * abs(mid)


def test_kalman_scalar_random_walk_reaches_riccati_steady_state():
    q, r, T = 0.1, 1.0, 200
    rng = np.random.default_rng(2)
    x = np.cumsum(rng.normal(0.0, np.sqrt(q), T))
    y = (x + rng.normal(0.0, np.sqrt(r), T)).reshape(T, 1)
    I1 = np.eye(1)
    means, covs = call_or_skip(coding.kalman_filter, y, I1, I1, q * I1, r * I1, np.zeros(1), I1)
    p_pred = (q + np.sqrt(q * q + 4 * q * r)) / 2
    p_post = p_pred * r / (p_pred + r)
    assert abs(np.asarray(covs)[-1][0, 0] - p_post) < 1e-6
    assert np.mean((np.asarray(means)[:, 0] - x) ** 2) < np.mean((y[:, 0] - x) ** 2)
