---
layout: post
title:  "Cholla_PM: Fixed Cross Flux Error"
date:   2019-07-26 17:10:24 -0800
categories: cholla
---


Now every row along the X axis has the exact same evolution and there are no cross fluxes. The issue was that originally for the $$p \nabla \cdot \mathbf{v} $$ term on the advected internal energy energy the value of  $$ \nabla \cdot \mathbf{v} $$  was computed on th same kernel were the conserved variables were updated, this means that there was a synchronization error because it was using values of the neighbors velocities to compute  $$ \nabla \cdot \mathbf{v} $$ and at the same time those velocities were being updated. 

The solution was to add the  $$p \nabla \cdot \mathbf{v} $$ term to the internal energy in a separate kernel before the Update_Conserved kernel.


## Zeldovich Pancake 

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_fixed_cross_flux.mp4" width="100%"  height="auto" controls preload> </video>
</div>

Now every row has the same values ( all overlap in the same line ) but the density still drops in the boundaries of the shock.

## Cosmological Simulation 

After fixing the bug, this are the results for the cosmological simulations using different values for $$eta_2$$:

### Phase Diagram 

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_new_eta2.mp4" width="100%"  height="auto" controls preload> </video>
</div>


### Power Spectrum

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/ps_128_eta2_new.mp4" width="100%"  height="auto" controls preload> </video>
</div>

