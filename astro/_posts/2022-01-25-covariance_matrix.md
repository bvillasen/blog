---
layout: post
title: "Covariance matrices from WDM simulations"
date:   2022-01-25 010:00:24 -0800
categorines: cholla
---


## Covariance Matrices from Boera et al 2019:

These are the covariance matrices obtained directly from the publication from Boera et al

<img src="{{ site.url }}assets/images/covariance_matrix/covariance_matrix.png">

Normalized covariance matrix given by: $$ \tilde{C}_{i,j} = C_{i,j} / \sqrt{C_{i,i} \,C_{j,j}}$$ 

<img src="{{ site.url }}assets/images/covariance_matrix/covariance_matrix_normalized.png">



## Covariance Matrices from different simulations:

From our WDM grid of simulations I show the covariance matrices from several models:

To see the effects of changing the parameters independently, I change only one of the parameters while leaving the other equal to the default parameters below:


### Changing $$m_{\mathrm{WDM}}$$

#### At $$z= 5.0$$
<img src="{{ site.url }}assets/images/covariance_matrix/snap_25/cm_multiple_wdm_mass_normalized.png">
#### At $$z= 4.6$$
<img src="{{ site.url }}assets/images/covariance_matrix/snap_29/cm_multiple_wdm_mass_normalized.png">
#### At $$z= 4.2$$
<img src="{{ site.url }}assets/images/covariance_matrix/snap_33/cm_multiple_wdm_mass_normalized.png">

### Changing $$\beta_{\mathrm{H}}^{\mathrm{ion}}$$

#### At $$z= 5.0$$
<img src="{{ site.url }}assets/images/covariance_matrix/snap_25/cm_multiple_scale_H_ion_normalized.png">
#### At $$z= 4.6$$
<img src="{{ site.url }}assets/images/covariance_matrix/snap_29/cm_multiple_scale_H_ion_normalized.png">
#### At $$z= 4.2$$
<img src="{{ site.url }}assets/images/covariance_matrix/snap_33/cm_multiple_scale_H_ion_normalized.png">

### Changing $$\alpha E_{\mathrm{He}}$$

#### At $$z= 5.0$$
<img src="{{ site.url }}assets/images/covariance_matrix/snap_25/cm_multiple_scale_H_Eheat_normalized.png">
#### At $$z= 4.6$$
<img src="{{ site.url }}assets/images/covariance_matrix/snap_29/cm_multiple_scale_H_Eheat_normalized.png">
#### At $$z= 4.2$$
<img src="{{ site.url }}assets/images/covariance_matrix/snap_33/cm_multiple_scale_H_Eheat_normalized.png">

### Changing $$\Delta z_{\mathrm{H}}$$

#### At $$z= 5.0$$
<img src="{{ site.url }}assets/images/covariance_matrix/snap_25/cm_multiple_deltaZ_H_normalized.png">
#### At $$z= 4.6$$
<img src="{{ site.url }}assets/images/covariance_matrix/snap_29/cm_multiple_deltaZ_H_normalized.png">
#### At $$z= 4.2$$
<img src="{{ site.url }}assets/images/covariance_matrix/snap_33/cm_multiple_deltaZ_H_normalized.png">











