"""Phase 4 checks: leaky integrate-and-fire interspike interval and rheobase."""

import numpy as np

from compneuro import spiking as sp
from compneuro.testing import call_or_skip


def test_lif_interspike_interval_matches_analytic():
    tau, R, I, v_th, t_ref = 10.0, 1.0, 1.5, 1.0, 2.0
    t = np.arange(0.0, 500.0, 0.005)
    _, spikes = call_or_skip(sp.simulate_lif, lambda t: I, t, tau, R, v_th, 0.0, 0.0, t_ref)
    expected = t_ref + tau * np.log(R * I / (R * I - v_th))
    assert abs(np.diff(spikes).mean() - expected) / expected < 0.01


def test_lif_silent_below_rheobase():
    t = np.arange(0.0, 200.0, 0.01)
    _, spikes = call_or_skip(sp.simulate_lif, lambda t: 0.9, t, 10.0, 1.0, 1.0)
    assert len(spikes) == 0
