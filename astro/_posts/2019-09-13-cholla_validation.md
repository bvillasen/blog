---
layout: post
title:  "Cholla_PM: Validation"
date:   2019-09-12 17:10:24 -0800
categories: cholla
---

# Zeldovich Pancake

<img src="{{ site.url }}assets/images/zeldovich_78.png">



# Cosmological Simulations

For all the tests the box is a 50 Mpc/h box on a $$256^3$$ cells grid.

## Dark Matter Only

First the comparison against **Nyx**, both Nyx and Cholla use the second order stencil for the gradient of the potential

<img src="{{ site.url }}assets/images/power_dm_nyx_50Mpc.png">


Now the comparison against **Ramses**, both Ramses and Cholla use the fourth order stencial for the gradient of the potential.

<img src="{{ site.url }}assets/images/power_dm_ramses.png">

Now the comparison against **Enzo**, both Enzo and Cholla use the fourth order stencial for the gradient of the potential.


<img src="{{ site.url }}assets/images/power_dm_enzo_grav4.png">

## Adiabatic Hydro Simulation.

Comparison against **Enzo** using $$eta==0.005$$ for Dual Energy

<img src="{{ site.url }}assets/images/ps_256_hydro_enzo_SIMPLE_PPMP_eta0.005_beta0.00_grav4.png">


## Radiative Cooling and UV Background

Comparison against **Enzo** using $$eta==0.035$$ for Dual Energy

<img src="{{ site.url }}assets/images/ps_256_SIMPLE_PPMP_eta0.035_beta0.00_grav4.png">


### Phase Diagram

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_256_cool_grav4.mp4" width="100%"  height="auto" controls preload> </video>
</div>


<img src="{{ site.url }}assets/images/phase_diagram_33.png">



