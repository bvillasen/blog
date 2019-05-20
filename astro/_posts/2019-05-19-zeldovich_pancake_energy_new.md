---
layout: post
title:  "CHOLLA_PM: Zeldovich Pancake Enzo Comparison"
date:   2019-05-19 17:10:24 -0800
categories: cholla
---


Here is the Zeldovich Pancake compared against Enzo again, now I show differen Reconstruction and Solver combinations :

**Only Advected Internal Energy**

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_enzo_PPMC.mp4" width="500" height="500" controls preload> </video>
</div>

The Parabolic reconstruction methods look much more similar to the Enzo evolution

**Dual Energy Off:** Now I compare when Dual Energy is off on both codes

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_enzo_PPMC_noDE.mp4" width="500" height="500" controls preload> </video>
</div>

Surprisingly the evolutions are not that different.

If I set $$\eta=0.001$$ ( supposedly ) equal to the value used in Enzo I get that the gas that is using the **Total Internal Energy** follow the same evolution as the noDual_Energy enzo, this indicates that we are not using the same prescription for selecting which internal_energy to use that Enzo is using:   


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_enzo_PPMC_DE001.mp4" width="500" height="500" controls preload> </video>
</div>
