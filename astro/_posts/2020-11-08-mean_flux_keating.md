---
layout: post
title: "Mean Transmitted Flux Keating et al. 2020"
date:   2020-11-08 10:10:24 -0800
categorines: cholla
---


From her papaer [here](https://ui.adsabs.harvard.edu/abs/2020MNRAS.491.1736K/abstract), this is the measurement of the Mean Transmitted Flux in their Simulations


<img src="{{ site.url }}assets/images/mean_flux_keating.png">

Here compared to other datasets:

<img src="{{ site.url }}assets/images/grid_optical_depth_data.png">



I choose the following data points to fit to:


<img src="{{ site.url }}assets/images/mcmc_tau_fit.png">



After sampling the MCMC for the scale_H parameter, this is the posterior distribution:

<img src="{{ site.url }}assets/images/scale_H.png">



Here is the Effective Optical depth for the obtained distribution of scale_H:


<img src="{{ site.url }}assets/images/mcmc_tau.png">


