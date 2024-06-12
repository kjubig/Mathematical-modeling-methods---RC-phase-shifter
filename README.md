# Project - RC Phase Shifter
## Description
This project involves modeling and simulating an RC phase shifter electric circuit. The circuit consists of resistances R1 and R2, capacitors C1 and C2, and an external electromotive force U = u(t). The program allows the user to define all these parameters via the program menu, ensuring they are positive values.

## The simulation follows Kirchhoff's laws (voltage and current balance) and Ohm's law:
### Resistor: u=R⋅i
### Capacitor: i=C⋅ dt/du
​
### The program plots the current values of the indicated voltages u(t) and x2(t). It considers voltage excitation (external electromotive force u(t)) in the form of a step and a sinusoid.

## Features:
- Parameter Definition: Users can define the values of R1, R2, C1, C2, and the external electromotive force U via the program menu.
- Simulation and Plotting: The program simulates the RC phase shifter circuit and plots the current values of u(t), x1(t), and x2(t).
- Excitation Forms: Supports step and sinusoidal forms of voltage excitation.
