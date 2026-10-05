"""Phase 5: multi-level brain modeling, from neural masses to BOLD.

Balloon-Windkessel (neural drive z -> BOLD), state (s, f, v, q):
    ds/dt = z - kappa s - gamma (f - 1)
    df/dt = s
    tau dv/dt = f - v^(1/alpha)
    tau dq/dt = f E(f) / E0 - v^(1/alpha) q / v,   E(f) = 1 - (1 - E0)^(1/f)
    BOLD = V0 [k1 (1 - q) + k2 (1 - q/v) + k3 (1 - v)]

Checks in tests/test_p5_populations.py:
    balloon_windkessel_rhs   (s, f, v, q) = (0, 1, 1, 1) is a fixed point at z = 0
    bold_signal              zero at rest
    both together            a 1 s burst of drive gives a positive BOLD peak 3-8 s later
"""

import numpy as np

# Commonly used values (Friston et al. 2000); time in seconds.
BALLOON_DEFAULTS = dict(
    kappa=0.65,  # signal decay, 1/s
    gamma=0.41,  # flow-dependent elimination, 1/s
    tau=0.98,  # haemodynamic transit time, s
    alpha=0.32,  # Grubb's exponent
    E0=0.34,  # resting oxygen extraction fraction
    V0=0.02,  # resting blood volume fraction
)


def wilson_cowan_rhs(E, I, w_EE, w_EI, w_IE, w_II, h_E, h_I, tau_E=1.0, tau_I=1.0, S=None):
    """Right-hand side of the Wilson-Cowan equations. Returns (dE/dt, dI/dt).

    S is the sigmoid; default to the logistic function if None.
    """
    raise NotImplementedError


def balloon_windkessel_rhs(state, z, params=BALLOON_DEFAULTS):
    """Time derivative of (s, f, v, q) for neural drive z. Returns an array of 4."""
    raise NotImplementedError


def bold_signal(v, q, params=BALLOON_DEFAULTS):
    """BOLD signal from blood volume v and deoxyhaemoglobin q.

    Use k1 = 7 E0, k2 = 2, k3 = 2 E0 - 0.2.
    """
    raise NotImplementedError
