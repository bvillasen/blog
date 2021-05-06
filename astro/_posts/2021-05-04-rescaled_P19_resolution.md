---
layout: post
title: "Rescaled P19 Simulations: Resolution Analysis "
date:   2021-05-04 08:00:24 -0800
categorines: cholla
---

Comparison of the measurements of the thermal history, effective optical depth and Lya flux power spectrum from 3 simulations, all using our current fiducial rescaled P19 model:

$$\beta_{\mathrm{He}} = 0.46$$

$$\beta_{\mathrm{H}} = 0.78$$

$$\Delta z_{\mathrm{He}} = 0.28$$

$$\Delta z_{\mathrm{H}} = 0.04$$ 

## Thermal History
<img src="{{ site.url }}assets/images/fig_thermal_history_res.png">


## Effective Optical Depth
<img src="{{ site.url }}assets/images/fig_tau_res_rescaledP19.png">


## Lya Flux Power Spectrum
<img src="{{ site.url }}assets/images/flux_power_spectrum_grid_all_res.png">

<img src="{{ site.url }}assets/images/flux_power_spectrum_grid_all_highZ_res.png">


The P(k) from the low resolution simulation has significant differences from the higher resolution simulations for $$z>3.2$$,  the optical depth also is different at those redshifts. We might need to do a higher resolution simulation ($$4094^3$$) if we want to use a $$200^3$$ Mpc/h volume.
