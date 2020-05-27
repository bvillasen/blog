---
layout: post
title: "SPH Skewers Direct Comparison Revisited"
date:   2020-05-26 10:10:24 -0800
categorines: dm cholla
---


After adding the $$\sqrt{a}$$ factor to the particles velocities., I can reproduce the optical depth of the skewers provided by Ewald. The blue lines are the Skewers that I compute and the orange lines correspond to the LOS data provided by Ewald, differences on the effective optical depth for each skewers are less than 1%

## Skewer 1
<img src="{{ site.url }}assets/images/skewer_0_12_1.png">

## Skewer 2
<img src="{{ site.url }}assets/images/skewer_1_12_1.png">


## Skewer 3
<img src="{{ site.url }}assets/images/skewer_2_12_1.png">


## Skewer 4
<img src="{{ site.url }}assets/images/skewer_3_12_1.png">

## Skewer 5
<img src="{{ site.url }}assets/images/skewer_5_12_1.png">


After adding the factor of $$\sqrt{a}$$, the value of $$\tau_{eff}$$ that I measure from the skewers computed from the SPH simulation also matches the value of $$\tau_{eff}$$ reported in Puchwein etal. 2019. But after including the $$\sqrt{a}$$ factor on the SPH particle velocities, then the peculiar velocities on the Cholla simulation are higher than the peculiar velocities in the SPH simulation.

The figure below shows the Density-LOSVelocity distribution for 5000 skewers from the Cholla simulation compared to same distribution computed from 5000 skewers from the SPH simulation  at z=5, **the peculiar velocities of the sph skewers includes the $$\sqrt{a}$$ factor.**
 
<img src="{{ site.url }}assets/images/dens_vel_distribution_12.png">


Now if I multiply the Cholla peculiar velocities by   $$\sqrt{a}$$ the velocities are very similar to the SPH skewer LOS velocities, as shown in the figure below:

<img src="{{ site.url }}assets/images/dens_vel_distribution_factor_12.png">


**Then the question is: Am I missing a factor of $$\sqrt{a}$$ when interpreting the Cholla gas peculiar velocities?** 


If I add the $$\sqrt{a}$$ factor, the effective optical depth is shown in the figure below:

<img src="{{ site.url }}assets/images/optical_depth_uvb_log_space_multiple_axis_new_sqrta.png">

