---
layout: post
title:  "CHOLLA_PM Test: Nyx Comparison"
date:   2018-11-06 17:10:24 -0800
categories: cholla
---




### Updated DM-ONLY power spectrum:

Accidentally I was using Lepfrog for the particles update, now using Kick-Drift-Kick ( same as Nyx ) the max differences are 0.3%

<img src="{{ site.url }}assets/images/power_dm_nyx_251.png">


### Gas Temperature:

The initial temperature of the gas set by Nyx is $$1000 K$$ at $$z=100$$,  I believe this is too high, previously I always used $$170 K$$ for the initial temperature. Here is the mean temperature evolution for both codes, the green line is the $$a^{-2}$$ dependence expected for a $$\gamma = 5/3$$ gas under cosmological adiabatic expansion.

<img src="{{ site.url }}assets/images/temp_nyx.png">

### Thermal history:

Here is a plot of the thermal history for both codes, on the top of the figure you can see the redshift and the corresponding average Temperature


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/thermal_history.mp4" width="500" height="500" controls preload> </video>
</div>


### Hydro power spectrum:

Finally, the differences on the gas power spectrum are huge, I believe it's because of the large differences on the temperatures.


<img src="{{ site.url }}assets/images/power_hydro_nyx.png">


As a reference here are the latest results from comparing to Enzo:

<img src="{{ site.url }}assets/images/power_hydro_enzo.png">
