---
layout: post
title: "Optical Depth: Turbulence Boost"
date:   2020-05-6 10:10:24 -0800
categorines: dm cholla
---

Here I explore the effect of increasing the Doppler parameter $$b$$ because of turbulent velocities simply by multiplying the thermal Doppler parameter by a factor to include a *turbulence boost*, this is expressed as:


$$b = b_{\mathrm{thermal}} \times ( 1 + t_{boost} ) $$

I measure the Transmitted Fluxes for all the skewers at z=5 (in redshift space), the figure below shows the distribution for different values of $$t_{boost}$$

<img src="{{ site.url }}assets/images/optical_depth_distribution_turbulence.png">

Computing the Effective Optical Depth $$\tau_{eff}$$ from the average Transmitted Flux over all the skewers, I obtain the following numerical values:


$$\tau_{eff}(t_{boost} = 0.0 ) = 1.51$$
$$\tau_{eff}(t_{boost} = 0.1 ) = 1.54$$
$$\tau_{eff}(t_{boost} = 0.25 ) = 1.57$$
$$\tau_{eff}(t_{boost} = 0.5 ) = 1.63$$


There is an increase in the Effective Optical Depth but it's not that significant even for $$t_{boost}=0.25$$ 

