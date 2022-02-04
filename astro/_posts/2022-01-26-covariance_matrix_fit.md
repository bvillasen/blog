---
layout: post
title: "WDM MCMC Fitting using covariance matrix"
date:   2022-02-02 011:00:24 -0800
categorines: cholla
---


After recomputing the flux power spectrum natively on the same $$k$$-bins as Boera et al. (instead of interpolating) to avoid correlations on adjacent Fourier modes I redo the MCMC fitting.

Here I compare the fits that result from using the uncertainty $$sigma$$ against using the full covariance matrix from Boera et al. The results are not that different now.
  

### Joint Fit to all redshifts
<img src="{{ site.url }}assets/images/wdm_mcmc_fit_covariance_matrix/corner_all.png">


### Fit only to $$z=4.2$$
<img src="{{ site.url }}assets/images/wdm_mcmc_fit_covariance_matrix/corner_r0.png">

### Fit only to $$z=4.6$$
<img src="{{ site.url }}assets/images/wdm_mcmc_fit_covariance_matrix/corner_r1.png">

### Fit only to $$z=5.0$$
<img src="{{ site.url }}assets/images/wdm_mcmc_fit_covariance_matrix/corner_r2.png">
