"""From-scratch models for a self-study path through computational neuroscience.

One module per phase. Every model function starts as a stub that raises
NotImplementedError; its test in tests/ skips until the stub is filled in.

    integrators   Phase 0  ODE and SDE solvers
    membrane      Phase 1  Nernst, GHK, Hodgkin-Huxley
    cable         Phase 2  passive cable, activating function
    dynamics      Phase 3  FitzHugh-Nagumo, theta neuron
    spiking       Phase 4  leaky integrate-and-fire
    populations   Phase 5  Wilson-Cowan, Balloon-Windkessel
    coding        Phase 6  Poisson GLM, Kalman filter
    plasticity    Phase 7  Oja's rule, STDP
    testing       helpers for the tests (already implemented)
"""

__version__ = "0.1.0"
