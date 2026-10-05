"""Phase 1 checks: Nernst, GHK limits, and Hodgkin-Huxley rest and firing."""

import numpy as np

from compneuro import membrane as mem
from compneuro.testing import call_or_skip, threshold_crossings

IONS = dict(K_o=5.0, K_i=140.0, Na_o=145.0, Na_i=12.0, Cl_o=110.0, Cl_i=10.0)
E_K = -89.06  # mV at 37 C for [K]o = 5 mM, [K]i = 140 mM
E_CL = -64.09  # mV at 37 C for [Cl]o = 110 mM, [Cl]i = 10 mM


def test_nernst_potassium():
    assert abs(call_or_skip(mem.nernst, 5.0, 140.0, 1) - E_K) < 0.3


def test_nernst_chloride_valence():
    assert abs(call_or_skip(mem.nernst, 110.0, 10.0, -1) - E_CL) < 0.3


def test_ghk_reduces_to_nernst_when_only_k_is_permeant():
    assert abs(call_or_skip(mem.ghk_voltage, 1.0, 0.0, 0.0, **IONS) - E_K) < 0.3


def test_ghk_reduces_to_nernst_when_only_cl_is_permeant():
    assert abs(call_or_skip(mem.ghk_voltage, 0.0, 0.0, 1.0, **IONS) - E_CL) < 0.3


def test_hh_rest_and_repetitive_firing():
    t = np.arange(0.0, 200.0, 0.01)
    v_rest = np.asarray(call_or_skip(mem.simulate_hh, lambda t: 0.0, t))
    assert -70.0 < v_rest[-1] < -60.0
    assert len(threshold_crossings(v_rest, t, 0.0)) == 0

    v_step = np.asarray(mem.simulate_hh(lambda t: 10.0 if t >= 50.0 else 0.0, t))
    assert len(threshold_crossings(v_step, t, 0.0)) >= 5
