"""Phase 3 checks: FitzHugh-Nagumo fixed point and the theta-neuron period."""

import numpy as np
import pytest

from compneuro import dynamics as dyn
from compneuro.testing import call_or_skip


def test_fhn_fixed_point_lies_on_both_nullclines():
    I, a, b = 0.5, 0.7, 0.8
    v, w = call_or_skip(dyn.fhn_fixed_point, I, a, b)
    assert abs(v - v**3 / 3 - w + I) < 1e-8
    assert abs(v + a - b * w) < 1e-8


def test_fhn_rhs_vanishes_at_fixed_point():
    v, w = call_or_skip(dyn.fhn_fixed_point, 0.5)
    dv, dw = call_or_skip(dyn.fhn_rhs, v, w, 0.5)
    assert abs(dv) < 1e-8 and abs(dw) < 1e-8


@pytest.mark.parametrize("I", [0.25, 1.0])
def test_theta_neuron_period(I):
    expected = np.pi / np.sqrt(I)
    assert abs(call_or_skip(dyn.theta_neuron_period, I) - expected) / expected < 0.01
