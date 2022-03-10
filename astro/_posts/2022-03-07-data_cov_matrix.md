---
layout: post
title: "Covariance Matrices of P(k) data"
date:   2022-03-06 010:00:24 -0800
categorines: cholla
---


### Boera et al. 
<img src="{{ site.url }}assets/images/thermal_covariance_matrix_data/covariance_matrix_boera_normalized.png">


### Irsic et al. 
<img src="{{ site.url }}assets/images/thermal_covariance_matrix_data/covariance_matrix_irsic_normalized.png">

Irsic et al. provides the full covariance across all the redshift bins, instead of just for each independent redshift bin.
<img src="{{ site.url }}assets/images/thermal_covariance_matrix_data/covariance_matrix_irsic_full_normalized.png">

### BOSS. 
<img src="{{ site.url }}assets/images/thermal_covariance_matrix_data/covariance_matrix_boss_normalized.png">


## Full Covariance Matrix used for the fit

Combining all the different matrices I build the full covariance matrix that I will use for the new MCMC fit


<img src="{{ site.url }}assets/images/thermal_covariance_matrix_data/covariance_matrix_normalized.png">

The inverse of the full covariance matrix is shown below:

<img src="{{ site.url }}assets/images/thermal_covariance_matrix_data/covariance_matrix_inverse_normalized.png">

     