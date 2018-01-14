---
layout: post
title:  "CHOLLA_PM: Gadget Comparison "
date:   2018-01-08 17:10:24 -0800
categories:
---
Cosmological Simulations $$256^3$$ particles, 115 Mpc/h box.

**Left: Gadget**


**Right: Cholla_PM**

**Updated:** Now every pair of images has the same dynamical range for the colormap and all the images are density projections of the CIC mass interporlation into a 256^3 grid

## Case 1:

Gadget:  $$\epsilon \, = \,9.7 \,kpc/h$$

Cholla:  $$cellSize \, = \,  449.2 \,kpc/h$$


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/density_cosmo_256_gadget_cholla.mp4" width="800" height="400" controls preload> </video>
</div>


## Case 2:

For this one the force resolution of Gadget was decreased to match the cell_size used for Cholla

Gadget:  $$\epsilon \, = \,449.2 \,kpc/h$$

Cholla:  $$cellSize \, = \,  449.2 \,kpc/h$$


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/density_cosmo_256_gadgetLow_cholla.mp4" width="800" height="400" controls preload> </video>
</div>


## Case 3:

For this one the force grid of Cholla is $$512^3$$ and is compared to Gadget original high resolution one.

Gadget:  $$\epsilon \, = \,9.7 \,kpc/h$$

Cholla:  $$cellSize \, = \,  224.6 \,kpc/h$$


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/density_cosmo_256_gadget_chollaHigh.mp4" width="800" height="400" controls preload> </video>
</div>
