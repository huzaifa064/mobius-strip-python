# Möbius Strip in Python

This project generates a 3D Möbius strip using its parametric equations.

## Parametric Equation

The Möbius strip is defined as:

\[
x = (R + u\sin(v/2))\cos(v)
\]

\[
y = (R + u\sin(v/2))\sin(v)
\]

\[
z = u\cos(v/2)
\]

where:

- \(u \in [-a,a]\)
- \(v \in [0,2\pi)\)
- \(R\) is the radius
- \(a\) is the half-width of the strip

## Requirements

Python 3 is required.

Install the necessary libraries:

```bash
pip install numpy matplotlib