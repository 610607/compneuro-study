"""Phase 1: membrane biophysics and Hodgkin-Huxley.

Conventions: potentials in mV, concentrations in mM, temperature in K,
currents in uA/cm^2, time in ms, modern HH convention (rest near -65 mV).

Checks in tests/test_p1_membrane.py:
    nernst          K+ with [K]o = 5 mM, [K]i = 140 mM at 37 C is about -89 mV
    ghk_voltage     reduces to the Nernst potential when only one ion is permeant
                    (including Cl-, where inside and outside swap)
    simulate_hh     silent near rest at I = 0; fires repetitively at I = 10 uA/cm^2
"""

import numpy as np

FARADAY = 96485.33212  # C/mol
GAS_CONSTANT = 8.314462618  # J/(mol K)


def nernst(c_out, c_in, z, T=310.15):
    """Nernst potential in mV for an ion of valence z."""
    raise NotImplementedError


def ghk_voltage(p_K, p_Na, p_Cl, K_o, K_i, Na_o, Na_i, Cl_o, Cl_i, T=310.15):
    """Goldman-Hodgkin-Katz resting potential in mV. Permeabilities are relative."""
    raise NotImplementedError


def hh_rates(V):
    """Hodgkin-Huxley rate functions at membrane potential V (mV).

    Returns a dict with keys 'alpha_m', 'beta_m', 'alpha_h', 'beta_h',
    'alpha_n', 'beta_n' (units 1/ms). Watch the removable singularities.
    """
    raise NotImplementedError


def simulate_hh(I_ext, t):
    """Simulate the space-clamped HH membrane.

    I_ext : callable I_ext(t) in uA/cm^2
    t     : time grid in ms (start from the resting state at t[0])
    Returns V(t) in mV, same length as t.

    Classic parameters: C_m = 1 uF/cm^2, g_Na = 120, g_K = 36, g_L = 0.3 mS/cm^2,
    E_Na = 50, E_K = -77, E_L = -54.4 mV.
    """
    raise NotImplementedError
