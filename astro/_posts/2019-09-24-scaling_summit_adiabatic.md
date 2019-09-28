---
layout: post
title:  "Cholla_PM: Scaling Tests on Summit ( Adiabatic Simulations )"
date:   2019-09-24 17:10:24 -0800
categories: cholla
---

## Scaling Test ( Adiabatic )

For this test every GPU evolves a 25Mpc/h sub-volume and every sub-volume has the exact same initial conditions. The times shown in the figure bellow are the averages over the first 30 timesteps of a cosmological simulation starting at $$z=100$$.  

<img src="{{ site.url }}assets/images/scaling_summit_adiabatic.png">

For this tests all the GPUs are evolving the same number of particles, because of this,  the computational load is balanced across all the processes. In this case the Poisson Solver dominates  the calculation time per timestep and increases as the volume of the computation increases due to the $$O(n\log{}n)$$ nature of the FFTs. I believe that a relaxation method implemented on the GPUs for thee Poisson solver could be faster, but this hasn't been implemented. 

## Cosmological Simulation ( Adiabatic )


On a realistic cosmological simulation the particles distribution becomes less uniform as the simulation progresses, this affects the computational load balance since processes that evolve regions that contain massive halos will have more particles than processes evolving under-dense regions. On a 1024$$^3$$ cell 50 Mpc/h simulation on 64 GPUs, the timestep at the end of the simulation took ~17% longer than at the beginning of the simulation.  



<img src="{{ site.url }}assets/images/timestep_summit_adiabatic_1024.png">



The previous figure shows the time per timestep as the simulation progresses. My guess is that this load balance issue will become more pronounced on a intrinsically non-uniform domain.