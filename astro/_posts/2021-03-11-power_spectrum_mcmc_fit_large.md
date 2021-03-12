---
layout: post
title: "P(k) MCMC Fit to Boss and Walther Data "
date:   2021-03-11 11:21:24 -0800
categorines: cholla
---


From a set of 256 $$1024^3$$ simulations where the parameters are:


$$\beta_{\mathrm{He}} = [ 0.3, \, 0.53, \, 0.76, \, 1.0   ] $$

$$\beta_{\mathrm{H}} = [ 0.6, \, 0.73, \, 0.86, \, 1.0 ] $$

$$\Delta z_{\mathrm{He}} = [-0.1, \, 0.2, \, 0.5, \, 0.8  ] $$

$$\Delta z_{\mathrm{H}} = [ -0.6, \, -0.4, \, -0.2, \, 0.0   ] $$



The distributions from fitting to the **Boss** and **Walther** data separately are:
 
<img src="{{ site.url }}assets/images/corner_boss_walther.png">

When I fit to bot datasets simultaneously, the results are very different:

<img src="{{ site.url }}assets/images/corner_boss_walther_both.png">
 

Below is the evolution of the  temperature from the fitted posterior distribution of the parameters:

<img src="{{ site.url }}assets/images/fig_T0_sampling_boss_walther.png">



Below is the evolution of the  power spectrum from the fitted posterior distribution of the parameters:


<img src="{{ site.url }}assets/imagesflux_ps_sampling_large_boss_walter.png">
<img src="{{ site.url }}assets/imagesflux_ps_sampling_small_boss_walter.png">
<img src="{{ site.url }}assets/imagesflux_ps_sampling_middle_boss_walter.png">

 
 