---
layout: post
title: "Cholla Chemistry solver compared to Grackle "
date:   2022-01-11 010:00:24 -0800
categorines: cholla
---

### Single zone test

First I compare a "single zone" test where the simulation is a small box with uniform density, zero velocities and uniform temperature. I compare the same simulation but in one case I use Grackle for the Chemistry/Cooling and for the other case I use the solver that I have implemented into Cholla. 

The evolution of the temperature and the abundances of the chemical species are shown below:

<img src="{{ site.url }}assets/images/cholla_chem_validation/single_cell_comparison.png">

There are small differences in the temperature, this might be because the some differences in the Cooling rates used. Also some differences in the HI and HeI fractions are shown at $$z \sim 6$$ these differences are at the end of Hydrogen reionization, and the reason could be that Grackle uses some special trick to handle the transition to photoionization equilibrium.  


### Density-Temperature distribution

Now I run a full cosmological simulation ( $$L=50 h^{-1} \mathrm{Mpc}$$, $$N=256^3$$ ). Below I compare the evolution of the density temperature distribution

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_grackle_cholla.mp4" width="100%"  height="auto" controls preload> </video>
</div>


### Lya Transmitted Flux along skewers

From a higher resolution simulation  ( $$L=50 h^{-1} \mathrm{Mpc}$$, $$N=1024^3$$ ), I measure the Lya transmitted flux along some skewers crossing the box, the comparison for several redshift values is below

#### $$z = 5.0$$
<img src="{{ site.url }}assets/images/cholla_chem_validation/skewers_comparison_0.png">

#### $$z = 4.0$$
<img src="{{ site.url }}assets/images/cholla_chem_validation/skewers_comparison_1.png">

#### $$z = 3.0$$
<img src="{{ site.url }}assets/images/cholla_chem_validation/skewers_comparison_2.png">

#### $$z = 2.0$$
<img src="{{ site.url }}assets/images/cholla_chem_validation/skewers_comparison_3.png">
