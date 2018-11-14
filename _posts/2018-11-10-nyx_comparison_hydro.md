---
layout: post
title:  "CHOLLA_PM Test: Hydro Nyx Comparison"
date:   2018-11-10 17:10:24 -0800
categories: cholla
---




### Updated DM-ONLY power spectrum:

The gravitational constant was different from the one in Nyx at the 5th digit, here are the new results, max differences are 0.25%

<img src="{{ site.url }}assets/images/power_dm_nyx_256_1.png">


### Gas Temperature:


**Cholla gravWork :** The energy update is $$\Delta E = dt \rho(  v \cdot  g) $$

**Cholla deltaEk :** The energy update is equal to the change in kinetic energy after the gravity update on the momentum.

**Cholla uniform :** Evolution of a uniform gas under adiabatic cosmological expansion, it follows the $$(1+z)^2 $$ scaling expected for a $$\gamma = 5/3 $$ gas.

<img src="{{ site.url }}assets/images/temp_nyx_vol.png">

<img src="{{ site.url }}assets/images/temp_nyx_mass.png">

### Density - Temperature Slices:

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/density_temp.mp4" width="500" height="500" controls preload> </video>
</div>

### Phase diagram:


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/thermal_history_1.mp4" width="500" height="500" controls preload> </video>
</div>
