---
layout: post
title:  "HYDRO: Solution to the Sod Sock Tube Problem"
date:   2017-12-08 17:10:24 -0800
categories: cholla
---

Here is my solution to the Sod Shock Tube problem using a 1D Hydro-solver based on a Godunov method that I programmed using Julia for my Hydrodynamics class.

The space grid is a regular grid discretized into 5000 cells and the simulation took 7000 iterations of the time-step to complete, this took 45 seconds to run in my laptop.  

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/shock_tube_anim.mp4" width="400" height="800" controls preload> </video>
</div>
