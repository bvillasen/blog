---
layout: post
title: "Particles timing CPU vs. GPU "
date:   2021-02-24 11:21:24 -0800
categorines: cholla
---

The comparison is for a $$256^3$$ dark matter simulation run in 8 GPUs and using the **PARIS** Poisson solver.

Below are the times of each of the main steps for the **PARTICLES_CPU** simulation, also  most of the particles steps use 10 OMP threads each:


<img src="{{ site.url }}assets/images/particles_time_cpu.png">



Now below are the times of each of the main steps for the **PARTICLES_GPU** simulation:


<img src="{{ site.url }}assets/images/particles_time_gpu.png">


Wiout counting the time for the Poisson solver (Time Grav Potential), the time for the potential boundaries transfer (Time Pot Boundaries)  and the time for the particles density boundaries transfer (Time Part Dens Transf) the total times of the CPU and GPU particles iteration is;


**Time Particles CPU = 182.8 ms**

**Time Particles CPU = 31.868 ms**

For this test the GPU version is ~5.7 times faster! 