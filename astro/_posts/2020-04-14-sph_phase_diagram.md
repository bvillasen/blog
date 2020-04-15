---
layout: post
title: "Phase Diagram from SPH Puchwein Simulations"
date:   2020-04-05 18:10:24 -0800
categories: dm cholla
---

For the SPH simulation, the phase diagram is computed from the gas density and temperature interpolated onto a grid ( $$512^3$$ cells ). For the interpolation I used two different methods:

**Gather 64:** Measure the distance that encloses 64 neighboring particles and use that distance as the smoothing length when computing the kernel weights.

**Scatter:** Use the smoothing lengths of the neighboring particles when computing the kernel weights. 

Below I show the phase diagram from the two interpolation methods and compare to the phase diagram from the Cholla simulation


### z= 5

<img src="{{ site.url }}assets/images/phase_diagram_sph_grid_z5.png"> 






### z= 5.5


<img src="{{ site.url }}assets/images/phase_diagram_sph_grid_z5.5.png">