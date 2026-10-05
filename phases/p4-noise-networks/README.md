# Phase 4 · Stochastic neurons and spiking networks

From one neuron to many: noise, population density and network states.

*Bio recap:* synapses are conductance changes triggered by presynaptic spikes. Cortex mixes roughly 80% excitatory and 20% inhibitory neurons.

**Notes:** [leaky integrate-and-fire](../../notes/lif.md) · [Fokker–Planck for LIF](../../notes/fokker-planck-lif.md) · [Ornstein–Uhlenbeck](../../notes/ornstein-uhlenbeck.md)

**Code:** `src/compneuro/spiking.py` · checks in `tests/test_p4_spiking.py`

| Derive | Implement | Read |
| --- | --- | --- |
| LIF interspike interval; f–I curve | LIF from scratch, checked against the analytic interval | Gerstner ch. 1, 5 |
| Spike-train statistics: Poisson, ISI, CV, Fano factor; renewal processes | Spike-train analysis toolkit on simulated data | Dayan & Abbott ch. 1; Gerstner ch. 7 |
| Diffusion approximation; Ornstein–Uhlenbeck; Fokker–Planck with absorbing threshold and reinjection at reset; Siegert rate formula | Fokker–Planck solver vs a Monte Carlo LIF population | Gerstner ch. 8, 13 |
| Conductance synapses; balanced E/I networks; asynchronous irregular state | Brunel network in Brian2: map network states vs inhibition strength and external rate | Brunel 2000; Gerstner ch. 12 |

## Self-test (optional)

- [ ] Derive the LIF interspike interval and the Fokker–Planck boundary conditions
- [ ] Match the Fokker–Planck firing rate to a simulated population, and explain any gap
- [ ] Reproduce Brunel's main network states (synchronous regular, asynchronous irregular, synchronous irregular)

## Log

<!-- A line now and then: what you derived, what you built, where you got stuck. -->
