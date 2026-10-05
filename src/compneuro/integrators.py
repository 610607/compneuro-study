"""Phase 0: ODE and SDE solvers, written from scratch.

All solvers take a time grid `t` (1D array, uniform or not) and return the
whole trajectory, shape (len(t), *np.shape(y0)).

Checks in tests/test_p0_integrators.py:
    euler           observed order ~1 on dy/dt = -y
    rk4             observed order ~4 on dy/dt = -y
    backward_euler_linear   stays bounded on a stiff system where euler blows up
    euler_maruyama  Ornstein-Uhlenbeck stationary variance = sigma^2 tau / 2
"""

import numpy as np


def euler(f, y0, t):
    """Forward Euler for dy/dt = f(t, y).

    f  : callable f(t, y) -> array shaped like y
    y0 : initial state (scalar or array)
    t  : time grid
    """
    raise NotImplementedError


def rk4(f, y0, t):
    """Classical fourth-order Runge-Kutta for dy/dt = f(t, y). Same interface as euler."""
    raise NotImplementedError


def backward_euler_linear(A, y0, t):
    """Implicit (backward) Euler for the linear system dy/dt = A y.

    Each step solves (I - dt A) y_{n+1} = y_n.
    A : (n, n) array; y0 : (n,) array.
    """
    raise NotImplementedError


def euler_maruyama(f, g, y0, t, rng):
    """Euler-Maruyama for dy = f(t, y) dt + g(t, y) dW.

    rng : numpy Generator; draw dW = sqrt(dt) * rng.standard_normal(np.shape(y)).
    y0 may be an array of independent paths, e.g. shape (n_paths,).
    """
    raise NotImplementedError
