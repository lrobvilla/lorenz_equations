
## Lorenz system of differential equations also called the Lorenz strange attractor

This is an implementation and optimization of the code presented by the user Hevenicio [here](https://github.com/Hevenicio/3D-Lorenz-Attractor-simulation-with-python). The present version of this code was writted (except for the english comments) as part of a project for my differential equations course back in 2021; the investigation project(in spanish) can be found as one of the files.

The differences between this code and the one that served as inspiration are basicaly two:
1. I'm plotting several solutions with different initial conditions to explicitly show the sensitivity to initial conditions of this caotic system.
2. I'm plotting every "trajectory" only once and then updating the code in every step instead of plotting in every step. The tests made show that this way represents a consirable gain in the speed of the animation.

An explanation of the basic theory concerning this system of diffential equations can be found in the pdf file.