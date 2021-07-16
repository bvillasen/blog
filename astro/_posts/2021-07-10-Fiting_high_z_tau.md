---
layout: post
title: "Fitting to High Redshift HI Optical Depth   "
date:   2021-07-10 08:00:24 -0800
categorines: cholla
---


Our model doesn't match the $$z > 5 $$ HI Effective Optical Depth, to fix it I will try to modify the HI photoionization rates to change the amount of neutral Hydrogen.

<img src="{{ site.url }}assets/images/fig_tau_HI_Boera_2021.png"> 


Fraction of neutral Hydrogen from the Modified P19 model and fraction rescaled to match the Effective Optical Depth from Bosman 2021 (SAZERAC).

<img src="{{ site.url }}assets/images/HI_fraction_P19m.png"> 

The goal now is to modify the HI photoionization rate to match the rescaled HI fraction.

### Rescale the rates separately:

First I try separating Gamma for $$ z < 5.8$$ and $$z > 5.8$$ then I allow to rescale by different amounts and I can shift the $$z > 5.8$$ part in Redshift.

  

<img src="{{ site.url }}assets/images/ionization_rate_HI_multiple_split.png">

The results:

 



### Analytical Fit to Gamma:



### 



### Reconstruct $$\Gamma$$ from the HI fraction


Take the evolution of HI fraction and use that to compute $$\Gamma$$

<img src="{{ site.url }}assets/images/fig_reconstructed_gamma_integral.png">


The solution is off by $$\sim 10^4$$ !!!!

I'm not taking into account recombination, recombination is almost as efficient as photoionization:


<img src="{{ site.url }}assets/images/fig_rates_fraction.png">


Actually the gas is probably in ionization Equilibrium. By equating:

**Collisional + Photo Ionization = Recombinatio** I can compute the photionization rate required to have the rescaled HI fractions.



<img src="{{ site.url }}assets/images/fig_reconstructed_gamma.png">


Now I run a $$1024^3$$ simulation with the new photoionization rate:


<img src="{{ site.url }}assets/images/fig_HI_tau_modified_gamma.png">

<img src="{{ site.url }}assets/images/flux_ps_grid_large_mod_gamma.png">
<img src="{{ site.url }}assets/images/flux_ps_grid_middle_mod_gamma.png">
<img src="{{ site.url }}assets/images/flux_ps_grid_small_mod_gamma.png">




