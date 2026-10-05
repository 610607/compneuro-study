"""Phase 0 checks: solver order, stiffness, and the Ornstein-Uhlenbeck variance."""

import numpy as np
import pytest

from compneuro import integrators as integ
from compneuro.testing import call_or_skip, convergence_order


def _final_error(method, n_steps):
    t = np.linspace(0.0, 1.0, n_steps + 1)
    y = call_or_skip(method, lambda t, y: -y, 1.0, t)
    return abs(np.asarray(y)[-1] - np.exp(-1.0))


@pytest.mark.parametrize("method, order", [(integ.euler, 1), (integ.rk4, 4)])
def test_observed_order(method, order):
    ns = [10, 20, 40, 80]
    errors = [_final_error(method, n) for n in ns]
    assert abs(convergence_order([1 / n for n in ns], errors) - order) < 0.3


def test_stiff_system_explicit_blows_up_implicit_does_not():
    A = np.diag([-1.0, -1000.0])
    y0 = np.array([1.0, 1.0])
    t = np.linspace(0.0, 1.0, 101)  # dt = 0.01, so dt * 1000 = 10 > 2
    y_explicit = np.asarray(call_or_skip(integ.euler, lambda t, y: A @ y, y0, t))
    y_implicit = np.asarray(call_or_skip(integ.backward_euler_linear, A, y0, t))
    assert np.abs(y_explicit[-1]).max() > 1e6
    assert np.abs(y_implicit[-1]).max() < 1.0
    assert np.isclose(y_implicit[-1][0], np.exp(-1.0), rtol=0.01)


def test_euler_maruyama_ou_stationary_variance():
    tau, sigma = 0.1, 1.0
    rng = np.random.default_rng(0)
    t = np.linspace(0.0, 2.0, 2001)  # 20 correlation times
    y0 = np.zeros(4000)  # independent paths
    y = call_or_skip(
        integ.euler_maruyama, lambda t, y: -y / tau, lambda t, y: sigma, y0, t, rng
    )
    expected = sigma**2 * tau / 2
    assert abs(np.var(np.asarray(y)[-1]) - expected) / expected < 0.1
