---
layout: post
title:  "Cholla_PM: Zeldovich Error"
date:   2019-07-16 17:10:24 -0800
categories: cholla
---

The Zeldovich Pancake test is physically  a **1D** problem, but I run a **3D** simulation and I choose a main axis along which the physical problem is solved ( X axis ); 

On the 3D simulation each 1D line along the axis X axis should have exactly the same values as all the other lines, but that is not the case, in the plot below I plot all the 1D lines along the 3D simulation and they are different!.


**Simulation Parameters:**

Lx = Ly = Lz = 64 Mpc/h

nx = ny = nz = 256   

Reconstruction: PPMC

Riemann: HLLC

Integrator: VL


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_error_256.mp4" width="100%"  height="auto" controls preload> </video>
</div>



Also the **Z** and **Y** components of the velocity are non-zero! 

The first suspect is the Gravitational Source, I will output and plot the potential, but it seems like for every line with an excess Y or Z velocity there is another line with the same excess in the other direction, this seems like a fluxes problem. 

