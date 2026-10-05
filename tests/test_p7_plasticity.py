"""Phase 7 checks: Oja's rule finds the top principal component; the STDP window."""

import numpy as np

from compneuro import plasticity as pl
from compneuro.testing import call_or_skip


def test_oja_converges_to_unit_top_principal_component():
    rng = np.random.default_rng(3)
    c, s = np.cos(0.6), np.sin(0.6)
    rot = np.array([[c, -s], [s, c]])
    cov = rot @ np.diag([3.0, 0.5]) @ rot.T
    X = rng.multivariate_normal([0.0, 0.0], cov, size=20000)
    w = np.asarray(call_or_skip(pl.run_oja, X, 0.002, np.array([0.3, -0.2])))[-1]
    assert abs(np.linalg.norm(w) - 1.0) < 0.05
    assert abs(w @ rot[:, 0]) / np.linalg.norm(w) > 0.99


def test_stdp_window():
    A_plus, A_minus = 0.01, 0.012
    assert call_or_skip(pl.stdp_dw, 5.0) > 0
    assert pl.stdp_dw(-5.0) < 0
    assert np.isclose(pl.stdp_dw(1e-9), A_plus, rtol=1e-6)
    assert np.isclose(pl.stdp_dw(-1e-9), -A_minus, rtol=1e-6)
    dw = np.asarray(pl.stdp_dw(np.array([-40.0, -10.0, 10.0, 40.0])))
    assert dw.shape == (4,)
    assert abs(dw[2]) > abs(dw[3]) and abs(dw[1]) > abs(dw[0])
