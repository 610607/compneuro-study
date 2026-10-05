"""Phase 7: plasticity and learning.

Checks in tests/test_p7_plasticity.py:
    run_oja   ||w|| -> 1 and w aligns with the top principal component of the data
    stdp_dw   potentiation for pre-before-post (dt > 0), depression otherwise;
              the jump at dt -> 0+ equals A_plus
"""

import numpy as np


def run_oja(X, eta, w0):
    """Apply Oja's rule once per sample: w <- w + eta y (x - y w), with y = w . x.

    X : (n_samples, d) zero-mean inputs; w0 : (d,) initial weights.
    Returns the weight history, shape (n_samples + 1, d).
    """
    raise NotImplementedError


def stdp_dw(dt, A_plus=0.01, A_minus=0.012, tau_plus=20.0, tau_minus=20.0):
    """Pair-based STDP weight change for spike-time difference dt = t_post - t_pre (ms).

    Accepts scalars or arrays.
    """
    raise NotImplementedError
