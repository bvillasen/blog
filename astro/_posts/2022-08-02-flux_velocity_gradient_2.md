---
layout: post
title: "Flux calculation: Velocity gradient REVISEFD"
date:   2022-08-01 010:00:24 -0800
categorines: cholla
---

The equation using Hubble velocity along the line of sight to do the integral:


$$\tau_{u_{0}}=\frac{\pi e^{2} \lambda_{0}}{m_{e} c } f_{12} \int \frac{n_{\mathrm{HI}}}{\sqrt{\pi} b} \exp \left[-\left(\frac{u-u_{0}}{b}\right)^{2}\right]  \frac{1}{H} \, dv $$, where $$dv = H dr$$ 


The equation using the gas velocity $$Hr + u_\mathrm{pec}$$ to do the integral:

$$\tau_{u_{0}}=\frac{\pi e^{2} \lambda_{0}}{m_{e} c } f_{12} \int \frac{n_{\mathrm{HI}}}{\sqrt{\pi} b} \exp \left[-\left(\frac{u-u_{0}}{b}\right)^{2}\right] \left|\frac{1}{ H + \nabla u_\mathrm{pec}}  \right| d u$$,

where  $$du =  | H dr + \Delta  u_\mathrm{pec} | $$

$$Note that an absolute value around $$du$$ is needed to avoid negative values.**   

Numerically the gradient and the difference are evaluated: 

$$ \nabla  u_\mathrm{pec} = \frac{u_\mathrm{pec}^{i+1} - u_\mathrm{pec}^{i-1}{2 dr} $$

$$ \Delta  u_\mathrm{pec} = \frac{u_\mathrm{pec}^{i+1} - u_\mathrm{pec}^{i-1}{2 } $$  


The comparison between the two calculations is below.

<img src="{{ site.url }}assets/images/flux_pec_vel/skewer_flux_33_new.png">


The fractional differences in the Flux are $$\lesssim 10^{-11}$$!!!


