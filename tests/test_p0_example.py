"""Worked example of the pattern every test here follows: model, analytic solution, check.

Model: dx/dt = -x / tau, with exact solution x(t) = x0 exp(-t / tau).
The forward-Euler loop is written inline so this example runs before
compneuro.integrators is implemented. Your own tests can copy this shape.
"""

import numpy as np

from compneuro.testing import convergence_order

TAU, X0, T_END = 1.0, 1.0, 2.0


def euler_decay(dt):
    x = X0
    for _ in range(int(round(T_END / dt))):
        x = x + dt * (-x / TAU)
    return x


def exact():
    return X0 * np.exp(-T_END / TAU)


def test_euler_decay_matches_analytic_solution():
    assert abs(euler_decay(1e-4) - exact()) < 1e-4


def test_euler_decay_is_first_order():
    dts = [0.02, 0.01, 0.005, 0.0025]
    errors = [abs(euler_decay(dt) - exact()) for dt in dts]
    assert abs(convergence_order(dts, errors) - 1.0) < 0.1
