---
layout: post
title: "MCMC Fitting using covariance matrix"
date:   2022-01-26 011:00:24 -0800
categorines: cholla
---


Here I fit the Power Spectrum from our 600 simulation grid to the observational data from Boera et al 2019 and I compare the results from fitting using only the uncertainty $$\sigma$$ against using the full covariance matrix from Boera et al. for the likelihood calculation.  


### Joint Fit to all redshifts
<img src="{{ site.url }}assets/images/wdm_fit_covmatrix/corner_all.png">


### Fit only to $$z=4.2$$
<img src="{{ site.url }}assets/images/wdm_fit_covmatrix/corner_r0.png">

### Fit only to $$z=4.6$$
<img src="{{ site.url }}assets/images/wdm_fit_covmatrix/corner_r1.png">

### Fit only to $$z=5.0$$
<img src="{{ site.url }}assets/images/wdm_fit_covmatrix/corner_r2.png">
