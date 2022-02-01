---
layout: post
title: "Cholla Chemistry solver compared to Grackle Revised "
date:   2022-01-28 010:00:24 -0800
categorines: cholla
---

After rewriting the solver to closely follow the methodology from Grackle the results are very good.

### Single zone test

First I compare a "single zone" test where the simulation is a small box with uniform density, zero velocities and uniform temperature. I compare the same simulation but in one case I use Grackle for the Chemistry/Cooling and for the other case I use the solver that I have implemented into Cholla. 

The evolution of the temperature and the abundances of the chemical species are shown below:

<img src="{{ site.url }}assets/images/cholla_chem_validation_fixed/single_cell_comparison_new.png">
  
There are some small differences around 2% in the temperature. The ionization states of H and He seem extremely close showing differences smaller than 0.002% !!!

### Density-Temperature distribution

Now I run a full cosmological simulation ( $$L=50 h^{-1} \mathrm{Mpc}$$, $$N=256^3$$ ). Below I compare the evolution of the density temperature distribution

<div style="text-align: center">
<video src="{{ site.url }}assets/images/cholla_chem_validation_fixed/phase_diagram_grackle_cholla.mp4" width="100%"  height="auto" controls preload> </video>
</div>


### Lya Transmitted Flux along skewers

From a higher resolution simulation  ( $$L=50 h^{-1} \mathrm{Mpc}$$, $$N=1024^3$$ ), I measure the Lya transmitted flux along some skewers crossing the box, the comparison for several redshift values is below

#### $$z = 5.0$$
<img src="{{ site.url }}assets/images/cholla_chem_validation_fixed/skewers_comparison_0.png">

#### $$z = 4.0$$
<img src="{{ site.url }}assets/images/cholla_chem_validation_fixed/skewers_comparison_1.png">

#### $$z = 3.0$$
<img src="{{ site.url }}assets/images/cholla_chem_validation_fixed/skewers_comparison_2.png">

#### $$z = 2.0$$
<img src="{{ site.url }}assets/images/cholla_chem_validation_fixed/skewers_comparison_3.png">



### Lya Flux Power Spectrum

From the ( $$L=50 h^{-1} \mathrm{Mpc}$$, $$N=1024^3$$ ) simulation, I measure the evolution of the Lya Flux Power Spectrum, the comparison is below:

<img src="{{ site.url }}assets/images/cholla_chem_validation_fixed/ps_comparison.png">

Only small differences on the highest $$k$$ bin. 


### Slices from the Simulations 

#### z=5.4
<img src="{{ site.url }}assets/images/cholla_chem_validation_fixed/slices_comparison_1.png">

#### z=4.0
<img src="{{ site.url }}assets/images/cholla_chem_validation_fixed/slices_comparison_5.png">

#### z=3.0
<img src="{{ site.url }}assets/images/cholla_chem_validation_fixed/slices_comparison_10.png">

#### z=2.0
<img src="{{ site.url }}assets/images/cholla_chem_validation_fixed/slices_comparison_15.png">
      