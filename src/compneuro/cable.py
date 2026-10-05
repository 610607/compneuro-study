"""Phase 2: cable theory and extracellular / TMS stimulation.

Checks in tests/test_p2_cable.py:
    steady_state_cable    away from the injection site, V decays as exp(-|x| / lambda)
    activating_function   zero inside a straight fiber in a uniform field;
                          equal to -a for a field growing linearly as E = a s
"""

import numpy as np


def steady_state_cable(n, dx, lam, inject_at, amplitude=1.0):
    """Finite-difference steady state of a passive cable with sealed ends.

    Solves  lam^2 V'' - V = -amplitude * delta(x - x_inject)  on n nodes spaced dx,
    with zero axial current at both ends (sealed-end boundary conditions).
    Units are arbitrary but consistent (e.g. dx and lam in the same length unit).
    Returns V at the n nodes.
    """
    raise NotImplementedError


def activating_function(E_parallel, ds):
    """Rattay's activating function along a fiber, f(s) = -dE_parallel/ds.

    E_parallel : field component along the fiber at each node
    ds         : node spacing
    Returns f at each node. Interior nodes use a central difference; decide
    (and note in notes/activating-function.md) what you return at the two ends.
    """
    raise NotImplementedError
