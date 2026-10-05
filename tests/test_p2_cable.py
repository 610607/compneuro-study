"""Phase 2 checks: passive cable length constant and the activating function."""

import numpy as np

from compneuro import cable
from compneuro.testing import call_or_skip


def test_steady_state_decays_with_length_constant():
    lam, dx, n = 1.0, 0.01, 2001  # cable 20 lambda long, current injected in the middle
    v = np.asarray(call_or_skip(cable.steady_state_cable, n, dx, lam, n // 2))
    x = (np.arange(n) - n // 2) * dx
    away = (x > 1.0) & (x < 5.0)  # clear of the injection site and the far end
    slope = np.polyfit(x[away], np.log(v[away]), 1)[0]
    assert abs(slope + 1.0 / lam) < 0.02


def test_activating_function_zero_in_uniform_field():
    f = np.asarray(call_or_skip(cable.activating_function, np.full(101, 3.0), 0.1))
    assert np.allclose(f[1:-1], 0.0)


def test_activating_function_linear_field():
    s = np.linspace(0.0, 1.0, 101)
    a = 2.5
    f = np.asarray(call_or_skip(cable.activating_function, a * s, s[1] - s[0]))
    assert np.allclose(f[1:-1], -a)
