"""Phase 4: stochastic neurons and spiking networks.

Leaky integrate-and-fire:
    tau_m dV/dt = -(V - E_L) + R I(t);   V >= V_th  ->  spike, V -> V_reset,
    then V is held at V_reset for t_ref.

Checks in tests/test_p4_spiking.py:
    simulate_lif   with constant input and E_L = V_reset = 0, the interspike
                   interval equals t_ref + tau_m ln(R I / (R I - V_th))
"""

import numpy as np


def simulate_lif(I, t, tau_m, R, V_th, V_reset=0.0, E_L=0.0, t_ref=0.0):
    """Simulate one LIF neuron.

    I : callable I(t)
    t : uniform time grid
    Returns (V, spike_times): V has the same length as t; spike_times is a 1D array.
    """
    raise NotImplementedError
