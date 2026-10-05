"""Helpers for the analytic-limit tests. These are infrastructure, already implemented."""

import numpy as np
import pytest


def call_or_skip(func, *args, **kwargs):
    """Call a study function, or skip the calling test if it is still a stub."""
    try:
        return func(*args, **kwargs)
    except NotImplementedError:
        pytest.skip(f"{func.__module__}.{func.__name__} is not implemented yet")


def convergence_order(step_sizes, errors):
    """Slope of log(error) against log(step size): the observed order of a method."""
    h = np.log(np.asarray(step_sizes, dtype=float))
    e = np.log(np.asarray(errors, dtype=float))
    slope, _ = np.polyfit(h, e, 1)
    return slope


def threshold_crossings(x, t, level=0.0):
    """Times at which x crosses `level` upward (e.g. spike times from a voltage trace)."""
    x = np.asarray(x)
    idx = np.flatnonzero((x[:-1] < level) & (x[1:] >= level))
    return np.asarray(t)[idx + 1]
