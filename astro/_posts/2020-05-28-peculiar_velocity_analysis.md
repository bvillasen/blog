---
layout: post
title: "Peculiar Velocity Analysis"
date:   2020-05-28 10:10:24 -0800
categorines: dm cholla
---


Here I show the Overdensity-Velocity distribution measured from the SPH particles from Ewalds simulation snapshots:

## Without $$\sqrt{a}$$ factor
<img src="{{ site.url }}assets/images/dens_vel_distribution_ewald.png">



## With $$\sqrt{a}$$ factor
<img src="{{ site.url }}assets/images/dens_vel_distribution_ewald_sqrta.png">


I ran adiabatic simulations ( without a UVB but I dont think this will affect significantly the peculiar velocities ) for the same initial conditions on a 50 Mpc/h box and $$256^3$$ particles-cells usning Cholla, Enzo and Gadget. Below I show the evolution of the Overdensity-Velocity distribution for the 3 simulations as well as the distribution of the DM particles velocities.

**Note that I added the $$\sqrt{a}$$ factor to the  Gadget peculiar velocities when loading them.**

<video src="{{ site.url }}assets/videos/dens_vel_distribution_comparison.mp4" width="100%"  height="auto" controls preload> </video>


I think that the peculiar velocities on the snapshots provided by Ewald already include the $$\sqrt{a}$$ factor, multiplying again by $$\sqrt{a}$$ leads to incorrect low peculiar velocities. 