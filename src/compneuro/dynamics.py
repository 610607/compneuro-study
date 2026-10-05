"""Phase 3: nonlinear dynamics and reduced neuron models.

FitzHugh-Nagumo:  dv/dt = v - v^3/3 - w + I,   dw/dt = eps (v + a - b w)
Theta neuron:     dtheta/dt = (1 - cos theta) + (1 + cos theta) I

Checks in tests/test_p3_dynamics.py:
    fhn_fixed_point       lies on both nullclines
    theta_neuron_period   matches pi / sqrt(I) for I > 0
"""

import numpy as np


def fhn_rhs(v, w, I, a=0.7, b=0.8, eps=0.08):
    """Right-hand side of FitzHugh-Nagumo. Returns (dv/dt, dw/dt)."""
    raise NotImplementedError


def fhn_fixed_point(I, a=0.7, b=0.8):
    """The fixed point (v*, w*) of FitzHugh-Nagumo for input I (unique for these a, b)."""
    raise NotImplementedError


def theta_neuron_period(I, dt=1e-3):
    """Interspike period of the theta neuron, found by simulation.

    A spike is theta passing pi. Simulate long enough to measure at least
    a few periods and return the mean.
    """
    raise NotImplementedError
