---
layout: post
title:  "Cholla_PM: Gravity Test"
date:   2019-12-12 17:10:24 -0800
categories: cholla gravity
---

## Self-Gravity

The **Spherical_Collapse** consists of  simple test for which a sphere of uniform density on a low density background is left to collapse only under its own gravitational attraction. Initially the fluid is static and the pressure is uniform across the entire box. The gravity will cause the sphere to collapse.

The initial density of the fluid is set to $$\rho=1$$ and for simplicity **the gravitational constant is set $$G=1$$**. The following animation shows the collapse as a function of time. If the pressure forces are ignores, then it's easy to compute the velocity of the gas at any radius  of the sphere as a function of time from energy conservation, the velocity as a function of time can be integrated to obtain the radius of the sphere as a function of time. This analytical estimate of a the evolution of the radius is shown as a white circle in the animation bellow, it's important to keep in mind that the approximation is made for a pressure-less fluid, for this reason this approximation is only valid when the pressure gradients are small. 

This test was run on a 256$^3$ grid, on 8 GPUs using the **VL** integrator, **HLLC** Riemann solver, and **PPMP** reconstruction. 

The animation below shows the evolution of the density at the single central slide of the box, as expected the density increases as the sphere collapses and the density remains mostly uniform during the simulation.  

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/spherical_collapse.mp4" width="100%"  height="auto" controls preload> </video>
</div>

## Now with Particles

Particles can be included for the **Spherical_Collapse** test, in this case the initial positions of the particles are randomly generated on a sphere such that the density is quasi-uniform ( there will be local density fluctuations due to the random assignment of the positions ). Initial velocities of the particles are set to zero. 

For this case the density of the particles in the sphere is set to $$\rho_p \approx  1 $$ on top of the fluid density $$\rho_g=1$$ so that the total density is now $$\rho=2$$, this will cause the sphere to collapse faster.


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/spherical_collapse_particles.mp4" width="100%"  height="auto" controls preload> </video>
</div>