"""Phase 5 checks: Wilson-Cowan at zero coupling, and the Balloon-Windkessel BOLD response."""

import numpy as np
from scipy.integrate import solve_ivp

from compneuro import populations as pop
from compneuro.testing import call_or_skip

REST = np.array([0.0, 1.0, 1.0, 1.0])  # (s, f, v, q)


def test_wilson_cowan_uncoupled_relaxes_toward_half():
    # With zero weights and inputs, the logistic sigmoid gives S(0) = 1/2.
    dE, dI = call_or_skip(pop.wilson_cowan_rhs, 0.0, 0.0, 0, 0, 0, 0, 0, 0, tau_E=2.0, tau_I=4.0)
    assert np.isclose(dE, 0.25) and np.isclose(dI, 0.125)


def test_balloon_rest_is_a_fixed_point():
    assert np.allclose(call_or_skip(pop.balloon_windkessel_rhs, REST, 0.0), 0.0, atol=1e-12)


def test_bold_is_zero_at_rest():
    assert abs(call_or_skip(pop.bold_signal, 1.0, 1.0)) < 1e-12


def test_bold_peaks_a_few_seconds_after_a_burst():
    call_or_skip(pop.balloon_windkessel_rhs, REST, 0.0)  # skip early if still a stub
    drive = lambda t: 1.0 if t < 1.0 else 0.0  # 1 s burst of neural drive
    sol = solve_ivp(
        lambda t, y: pop.balloon_windkessel_rhs(y, drive(t)), (0.0, 20.0), REST, max_step=0.01
    )
    bold = np.asarray(call_or_skip(pop.bold_signal, sol.y[2], sol.y[3]))
    k = np.argmax(bold)
    assert bold[k] > 0
    assert 3.0 < sol.t[k] < 8.0
