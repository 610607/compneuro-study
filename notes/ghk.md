# Goldman–Hodgkin–Katz voltage equation

Phase [1 · Membrane and Hodgkin–Huxley](../phases/p1-membrane-hh/README.md) · status: not started

## Statement

```math
V_\text{rest} = \frac{RT}{F}\ln\frac{P_K[K]_o + P_{Na}[Na]_o + P_{Cl}[Cl]_i}{P_K[K]_i + P_{Na}[Na]_i + P_{Cl}[Cl]_o}
```

$P$ relative permeabilities. Note where the Cl⁻ concentrations sit, and why.

## Derivation

<!-- Work it by hand first, then write the steps here. -->

## Assumptions

## Units and typical values

## Analytic limits and checks

## Code

`compneuro.membrane.ghk_voltage` · test: [`tests/test_p1_membrane.py`](../tests/test_p1_membrane.py)

## Related

- [Nernst potential](nernst.md)
- [Nernst–Planck equation](nernst-planck.md)
- [Hodgkin–Huxley membrane equation](hodgkin-huxley.md)
