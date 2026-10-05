# Phase 6 · Neural coding, inference and closed-loop control

The read-out and control side: estimating brain state from recordings and choosing stimulation to steer it, the core of a closed-loop mTMS platform. fMRI gives a second, slower read-out alongside EEG.

**Notes:** [Poisson GLM](../../notes/poisson-glm.md) · [fMRI GLM](../../notes/fmri-glm.md) · [Fisher information](../../notes/fisher-information.md) · [state space and LQR](../../notes/state-space-lqr.md) · [DCM](../../notes/dcm.md)

**Code:** `src/compneuro/coding.py` · checks in `tests/test_p6_coding.py`

| Derive | Implement | Read |
| --- | --- | --- |
| Tuning curves; reverse correlation; encoding models; the fMRI GLM as a Gaussian encoding model | STA on a simulated LNP neuron; refit a task-fMRI GLM and read it as an encoding model | Dayan & Abbott ch. 1–2; Poldrack, Mumford & Nichols |
| Poisson GLM; concavity of the log-likelihood; regularization | GLM with a spike-history filter fitted to simulated data | Dayan & Abbott ch. 2–3; Pillow et al. 2008 |
| Fisher information; Cramér–Rao bound; mutual information; cross-validated linear decoding | Decoding error vs population size against the bound; an MVPA decoder on task-fMRI data | Dayan & Abbott ch. 3–4; Haxby et al. 2001 |
| Linear-Gaussian state-space models; Kalman filter; EM for system identification; DCM as a bilinear state-space model with a hemodynamic observation | Online phase estimation from a noisy EEG-like signal (Phase 5 model); simulate a two-region DCM and recover its coupling (own estimator or SPM) | Särkkä, *Bayesian Filtering and Smoothing*; Friston, Harrison & Penny 2003 |
| LQR and MPC; phase-based control using the Phase 3 PRC; closed-loop time scales: EEG-phase TMS vs real-time fMRI neurofeedback | Closed loop: phase-triggered pulses into the Jansen–Rit or whole-brain model; repeat with a BOLD-delayed read-out and compare | Zrenner et al. 2018; Sitaram et al. 2017 |

Analyses of your own task-fMRI data go in the private repo; simulations and open data stay here.

## Self-test (optional)

- [ ] Derive the GLM log-likelihood and prove it is concave for the exponential link
- [ ] Explain why Fisher information vanishes at a tuning-curve peak
- [ ] Recover the coupling of a simulated two-region DCM and say which parameters are hard to identify
- [ ] Run a closed loop that estimates phase online and report how accurately it hits a target phase
- [ ] Explain what a BOLD-fed controller can and can't control, given the hemodynamic delay

## Log

<!-- A line now and then: what you derived, what you built, where you got stuck. -->
