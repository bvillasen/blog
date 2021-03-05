---
layout: post
title: "Particles timing CPU vs. GPU "
date:   2021-02-24 11:21:24 -0800
categorines: cholla
---

The comparison is for a $$256^3$$ dark matter simulation run in 8 GPUs and using the **PARIS** Poisson solver.

Below are the times of each of the main steps for the **PARTICLES_CPU** simulation:


<img src="{{ site.url }}assets/images/particles_time_cpu.png">



Now below are the times of each of the main steps for the **PARTICLES_GPU** simulation:


<img src="{{ site.url }}assets/images/particles_time_gpu.png">


