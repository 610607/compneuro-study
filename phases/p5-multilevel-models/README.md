# Phase 5 · Multi-level brain modeling

From spiking networks to whole-brain models, so you can pick the right level for each question and know what each reduction throws away. It ends where fMRI work begins: simulated BOLD compared with measured connectivity.

| Level | Example model | Tool | Keeps | Drops |
| --- | --- | --- | --- | --- |
| Morphological neuron | Compartmental HH (Phases 1–2) | NEURON | Dendrites, axon geometry, field coupling | Network context |
| Microcircuit | Detailed cortical column | NEURON, NetPyNE | Cell types, layer-specific wiring | Whole-brain coupling |
| Spiking network | LIF or Izhikevich networks (Phase 4) | Brian2, NEST | Spike timing, variability | Morphology |
| Mean field / neural mass | Wilson–Cowan, Montbrió–Pazó–Roxin, Jansen–Rit | Own code | Population rates, oscillations, EEG-like signals | Individual spikes |
| Neural field | Amari | Own code | Waves and bumps across cortex | Discrete regions |
| Whole brain | Connectome-coupled neural masses | The Virtual Brain | Region interactions, delays, EEG/fMRI forward models | Within-region detail |

**Notes:** [Wilson–Cowan](../../notes/wilson-cowan.md) · [MPR mean field](../../notes/mpr-mean-field.md) · [Amari field](../../notes/amari-neural-field.md) · [whole-brain network](../../notes/whole-brain-network.md) · [Balloon–Windkessel](../../notes/balloon-windkessel.md)

**Code:** `src/compneuro/populations.py` · checks in `tests/test_p5_populations.py`

| Derive | Implement | Read |
| --- | --- | --- |
| Wilson–Cowan and Jansen–Rit; their fixed points and bifurcations | Jansen–Rit alpha rhythm and its evoked response to a pulse | Dayan & Abbott ch. 7; Ermentrout & Terman ch. 11; Deco et al. 2008 |
| Exact mean field for QIF networks (Montbrió–Pazó–Roxin) | Spiking QIF network and its mean-field equations side by side | Montbrió, Pazó & Roxin 2015 |
| Neural fields; travelling waves; stability of the homogeneous state | 1D neural field with a Mexican-hat kernel: bumps and waves | Ermentrout & Terman ch. 12; Gerstner ch. 18 |
| Neurovascular coupling; Balloon–Windkessel model; the HRF as its linearized impulse response | Balloon–Windkessel from scratch; compare its impulse response with the canonical HRF in your fMRI pipeline | Buxton et al. 1998; Friston et al. 2000 |
| Connectome coupling and conduction delays; EEG lead field and BOLD as two observation models of one brain model | TVB model on its default connectome (or one from your diffusion data); fit global coupling to resting-state FC; a TMS-like pulse to one region with simulated EEG and BOLD | Breakspear 2017; Honey et al. 2009; Nunez & Srinivasan; TVB documentation |

Fitting to your own resting-state data happens in the private repo (`compneuro-private/fmri/`); open datasets can be used here.

## Self-test (optional)

- [ ] Show numerically where the exact mean field matches the spiking network and where it fails (finite size, heterogeneity)
- [ ] For each level in the table, name one question it answers and one it can't
- [ ] Derive the HRF from the linearized Balloon–Windkessel model and match it to your pipeline's canonical HRF
- [ ] Fit global coupling so simulated FC matches resting-state FC, and report the fit
- [ ] Simulate a pulse-evoked response in a whole-brain model and compute both its EEG (through a lead field) and its BOLD

## Log

<!-- A line now and then: what you derived, what you built, where you got stuck. -->
