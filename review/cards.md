# Review cards

Spaced review, two kinds of card. **Equation cards:** read the name, write the equation from memory, then open the answer. **Question cards:** answer in your own words first; fill in the answer only once you have worked it out.

Suggested rhythm: a few cards a week, revisit the ones you missed sooner.

## Equation cards

<details><summary><b>Ornstein–Uhlenbeck process</b> · <a href="../notes/ornstein-uhlenbeck.md">note</a></summary>

```math
dX = -\frac{X}{\tau}\,dt + \sigma\,dW
```

</details>

<details><summary><b>Nernst–Planck equation</b> · <a href="../notes/nernst-planck.md">note</a></summary>

```math
\mathbf{J}_k = -D_k\left(\nabla c_k + \frac{z_k F}{RT}\,c_k\nabla\phi\right)
```

</details>

<details><summary><b>Nernst potential</b> · <a href="../notes/nernst.md">note</a></summary>

```math
E_k = \frac{RT}{z_k F}\ln\frac{[k]_o}{[k]_i}
```

</details>

<details><summary><b>Goldman–Hodgkin–Katz voltage equation</b> · <a href="../notes/ghk.md">note</a></summary>

```math
V_\text{rest} = \frac{RT}{F}\ln\frac{P_K[K]_o + P_{Na}[Na]_o + P_{Cl}[Cl]_i}{P_K[K]_i + P_{Na}[Na]_i + P_{Cl}[Cl]_o}
```

</details>

<details><summary><b>Hodgkin–Huxley membrane equation</b> · <a href="../notes/hodgkin-huxley.md">note</a></summary>

```math
C_m\frac{dV}{dt} = -\bar g_{Na}m^3h\,(V-E_{Na}) - \bar g_K n^4\,(V-E_K) - g_L(V-E_L) + I
```

</details>

<details><summary><b>Gating kinetics</b> · <a href="../notes/gating-kinetics.md">note</a></summary>

```math
\dot x = \alpha_x(V)(1-x) - \beta_x(V)\,x = \frac{x_\infty(V) - x}{\tau_x(V)},\qquad x\in\{m,h,n\}
```

</details>

<details><summary><b>Cable equation with extracellular drive</b> · <a href="../notes/cable-equation.md">note</a></summary>

```math
\lambda^2\frac{\partial^2V_m}{\partial s^2} - \tau_m\frac{\partial V_m}{\partial t} - V_m = -\lambda^2\frac{\partial^2\psi}{\partial s^2},\qquad \lambda=\sqrt{\frac{R_m d}{4R_i}},\quad \tau_m = R_m C_m
```

</details>

<details><summary><b>Activating function and quasipotential</b> · <a href="../notes/activating-function.md">note</a></summary>

```math
\psi(s) = -\int^{s}\mathbf E\cdot d\mathbf s,\qquad f(s) = \frac{\partial^2\psi}{\partial s^2} = -\frac{\partial E_\parallel}{\partial s}
```

</details>

<details><summary><b>FitzHugh–Nagumo model</b> · <a href="../notes/fitzhugh-nagumo.md">note</a></summary>

```math
\dot v = v - \tfrac{v^3}{3} - w + I,\qquad \dot w = \varepsilon\,(v + a - b\,w)
```

</details>

<details><summary><b>Theta neuron (SNIC normal form)</b> · <a href="../notes/theta-neuron.md">note</a></summary>

```math
\dot\theta = (1-\cos\theta) + (1+\cos\theta)\,I
```

</details>

<details><summary><b>Phase reduction and the phase response curve</b> · <a href="../notes/phase-reduction.md">note</a></summary>

```math
\dot\theta = \omega + Z(\theta)\,I(t)
```

</details>

<details><summary><b>Leaky integrate-and-fire neuron</b> · <a href="../notes/lif.md">note</a></summary>

```math
\tau_m\dot V = -(V - E_L) + R\,I(t),\qquad V \ge V_{th}\;\Rightarrow\;V \to V_{reset}
```

</details>

<details><summary><b>Fokker–Planck equation for a noisy LIF population</b> · <a href="../notes/fokker-planck-lif.md">note</a></summary>

```math
\tau\,\partial_t P = \partial_V\big[(V-\mu)P\big] + \tfrac{\sigma^2}{2}\,\partial_V^2 P,\qquad P(V_{th},t) = 0,\quad \nu(t) = -\tfrac{\sigma^2}{2\tau}\,\partial_V P\big|_{V_{th}}
```

</details>

<details><summary><b>Wilson–Cowan equations</b> · <a href="../notes/wilson-cowan.md">note</a></summary>

```math
\tau_E\dot E = -E + S(w_{EE}E - w_{EI}I + h_E),\qquad \tau_I\dot I = -I + S(w_{IE}E - w_{II}I + h_I)
```

</details>

<details><summary><b>Exact mean field for QIF networks (Montbrió–Pazó–Roxin)</b> · <a href="../notes/mpr-mean-field.md">note</a></summary>

```math
\tau\dot r = \frac{\Delta}{\pi\tau} + 2rv,\qquad \tau\dot v = v^2 + \bar\eta + J\tau r + I(t) - (\pi\tau r)^2
```

</details>

<details><summary><b>Amari neural field</b> · <a href="../notes/amari-neural-field.md">note</a></summary>

```math
\tau\,\partial_t u(\mathbf x,t) = -u + \int w(\mathbf x-\mathbf x')\,f\big(u(\mathbf x',t)\big)\,d\mathbf x' + h(\mathbf x,t)
```

</details>

<details><summary><b>Connectome-coupled whole-brain model</b> · <a href="../notes/whole-brain-network.md">note</a></summary>

```math
\dot{\mathbf x}_i = F(\mathbf x_i) + G\sum_j C_{ij}\,\mathbf x_j(t - d_{ij}/v) + \boldsymbol\xi_i(t)
```

</details>

<details><summary><b>Balloon–Windkessel haemodynamic model</b> · <a href="../notes/balloon-windkessel.md">note</a></summary>

```math
\dot s = z - \kappa s - \gamma(f-1),\quad \dot f = s,\quad \tau\dot v = f - v^{1/\alpha},\quad \tau\dot q = \frac{f\,E(f)}{E_0} - \frac{v^{1/\alpha}q}{v},\quad E(f) = 1-(1-E_0)^{1/f}
```

```math
y_{BOLD} = V_0\big[k_1(1-q) + k_2(1-q/v) + k_3(1-v)\big]
```

</details>

<details><summary><b>Poisson GLM for spike trains</b> · <a href="../notes/poisson-glm.md">note</a></summary>

```math
\lambda(t) = \exp\big(\mathbf k\cdot\mathbf x(t) + \mathbf h\cdot\mathbf y_{hist}(t) + b\big),\qquad \log\mathcal L = \sum_t\big[y_t\log(\lambda_t\Delta) - \lambda_t\Delta\big]
```

</details>

<details><summary><b>Mass-univariate fMRI GLM</b> · <a href="../notes/fmri-glm.md">note</a></summary>

```math
\mathbf y = X\boldsymbol\beta + \boldsymbol\varepsilon,\qquad X_{:,j} = u_j * h
```

</details>

<details><summary><b>Fisher information and the Cramér–Rao bound</b> · <a href="../notes/fisher-information.md">note</a></summary>

```math
\mathrm{Var}(\hat s) \ge \frac{1}{I_F(s)},\qquad I_F(s) = T\sum_i\frac{f_i'(s)^2}{f_i(s)},\qquad I(S;R) = H(R) - H(R\mid S)
```

</details>

<details><summary><b>Linear-Gaussian state space, Kalman filter and LQR</b> · <a href="../notes/state-space-lqr.md">note</a></summary>

```math
\mathbf x_{t+1} = A\mathbf x_t + B\mathbf u_t + \mathbf w_t,\qquad \mathbf y_t = C\mathbf x_t + \mathbf v_t,\qquad J = \sum_t\big(\mathbf x_t^\top Q\,\mathbf x_t + \mathbf u_t^\top R\,\mathbf u_t\big)
```

</details>

<details><summary><b>Dynamic causal modelling</b> · <a href="../notes/dcm.md">note</a></summary>

```math
\dot{\mathbf z} = \Big(A + \sum_j u_j B^{(j)}\Big)\mathbf z + C\mathbf u,\qquad \mathbf y = g(\mathbf z, \theta_h) + \boldsymbol\varepsilon
```

</details>

<details><summary><b>Oja's rule</b> · <a href="../notes/oja.md">note</a></summary>

```math
\dot{\mathbf w} = \eta\,y\,(\mathbf x - y\,\mathbf w),\qquad y = \mathbf w\cdot\mathbf x
```

</details>

<details><summary><b>Spike-timing-dependent plasticity</b> · <a href="../notes/stdp.md">note</a></summary>

```math
\Delta w = \begin{cases} A_+e^{-\Delta t/\tau_+} & \Delta t > 0 \\ -A_-e^{\Delta t/\tau_-} & \Delta t < 0 \end{cases},\qquad \Delta t = t_{post} - t_{pre}
```

</details>

## Question cards

### Phase 0 · Setup and math warm-up

<details><summary>Integrate a stiff 2D linear system with explicit Euler and with an implicit solver, and explain why one blows up</summary>

_Your answer, once you have one._

</details>

<details><summary>Simulate an Ornstein–Uhlenbeck process and match its stationary variance to the analytic value</summary>

_Your answer, once you have one._

</details>

### Phase 1 · Membrane biophysics and Hodgkin–Huxley

<details><summary>Write GHK and HH from memory, with units for every term</summary>

_Your answer, once you have one._

</details>

<details><summary>Reproduce threshold, refractoriness, anode-break excitation and the f–I curve</summary>

_Your answer, once you have one._

</details>

<details><summary>Set τ_n = τ_m, simulate, and explain what happens to the spike</summary>

_Your answer, once you have one._

</details>

<details><summary>Explain why the Cl⁻ concentrations are swapped in GHK</summary>

_Your answer, once you have one._

</details>

### Phase 2 · Cable theory and extracellular / TMS stimulation

<details><summary>Derive the cable equation with extracellular drive, including the sealed-end boundary condition</summary>

_Your answer, once you have one._

</details>

<details><summary>Predict, before simulating, where a straight and a bent axon depolarize and hyperpolarize in a uniform field</summary>

_Your answer, once you have one._

</details>

<details><summary>Reproduce the Roth & Basser threshold trend</summary>

_Your answer, once you have one._

</details>

<details><summary>A1: one plot of threshold error vs E-field error, FEM vs surrogate</summary>

_Your answer, once you have one._

</details>

### Phase 3 · Nonlinear dynamics and reduced neuron models

<details><summary>Classify a new 2D model's excitability class from its phase plane alone</summary>

_Your answer, once you have one._

</details>

<details><summary>Compute a PRC two ways and show that they agree</summary>

_Your answer, once you have one._

</details>

<details><summary>Explain why a class I neuron can fire arbitrarily slowly but a class II neuron can't</summary>

_Your answer, once you have one._

</details>

<details><summary>Predict the phase at which a pulse train locks an oscillator, then confirm it by simulation</summary>

_Your answer, once you have one._

</details>

### Phase 4 · Stochastic neurons and spiking networks

<details><summary>Derive the LIF interspike interval and the Fokker–Planck boundary conditions</summary>

_Your answer, once you have one._

</details>

<details><summary>Match the Fokker–Planck firing rate to a simulated population, and explain any gap</summary>

_Your answer, once you have one._

</details>

<details><summary>Reproduce Brunel's main network states (synchronous regular, asynchronous irregular, synchronous irregular)</summary>

_Your answer, once you have one._

</details>

### Phase 5 · Multi-level brain modeling

<details><summary>Show numerically where the exact mean field matches the spiking network and where it fails (finite size, heterogeneity)</summary>

_Your answer, once you have one._

</details>

<details><summary>For each level in the table, name one question it answers and one it can't</summary>

_Your answer, once you have one._

</details>

<details><summary>Derive the HRF from the linearized Balloon–Windkessel model and match it to your pipeline's canonical HRF</summary>

_Your answer, once you have one._

</details>

<details><summary>Fit global coupling so simulated FC matches resting-state FC, and report the fit</summary>

_Your answer, once you have one._

</details>

<details><summary>Simulate a pulse-evoked response in a whole-brain model and compute both its EEG (through a lead field) and its BOLD</summary>

_Your answer, once you have one._

</details>

### Phase 6 · Neural coding, inference and closed-loop control

<details><summary>Derive the GLM log-likelihood and prove it is concave for the exponential link</summary>

_Your answer, once you have one._

</details>

<details><summary>Explain why Fisher information vanishes at a tuning-curve peak</summary>

_Your answer, once you have one._

</details>

<details><summary>Recover the coupling of a simulated two-region DCM and say which parameters are hard to identify</summary>

_Your answer, once you have one._

</details>

<details><summary>Run a closed loop that estimates phase online and report how accurately it hits a target phase</summary>

_Your answer, once you have one._

</details>

<details><summary>Explain what a BOLD-fed controller can and can't control, given the hemodynamic delay</summary>

_Your answer, once you have one._

</details>

### Phase 7 · Plasticity and learning

<details><summary>Prove that Oja's rule drives ‖w‖ to 1</summary>

_Your answer, once you have one._

</details>

<details><summary>Show in simulation how pulse timing relative to postsynaptic spikes flips the sign of Δw</summary>

_Your answer, once you have one._

</details>
