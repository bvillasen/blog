---
layout: post
title: "Effective Optical Depth from the Grid"
date:   2020-04-26 11:10:24 -0800
categorines: dm cholla
---


I compute the Effective Optical Depth from the full grid by averaging the transmitted flux of each cell:


$$e^{-\tau_{\mathrm{eff}}}= \frac{1}[N] \sum e^{-\tau(n_{\mathrm{HI}})} $$

where the optical depth of each cell is given by:

$$\tau(n_{\mathrm{HI}})=\frac{\pi e^{2} \lambda_0}{m_{e}  c H} f_{12} n_{\mathrm{HI}}  $$

Plotting the new measurement:


<img src="{{ site.url }}assets/images/optical_depth_uvb_log_grid.png"> 

The optical depth measured from the grid is higher compared to the one measured from the skewers for z>4 but it's lower for z<4, it's not clear whats happening.

The Numerical values of the optical depth at z=5 and z=5.5 are:

$$\tau_{\mathrm{eff}}(z=5) \aprox 1.7$$

$$\tau_{\mathrm{eff}}(z=5.5) \aprox 2.1$$

Comparing to the result from **Puchwein et al. 2019**, seems like for the new optical depths measured from the grid are consistent with the ones reported by Ewald, 

<img src="{{ site.url }}assets/images/puchwein_1.png"> 

The question is: what is happening at z<4 for the optical depth measured from the grid.