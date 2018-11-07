---
layout: post
title:  "CHOLLA_PM Test: Nyx Comparison"
date:   2018-11-06 17:10:24 -0800
categories: cholla
---




### Updated DM power spectrum:

Accidentally I was using Lepfrog for the particles update, now using Kick-Drift-Kick ( same as Nyx ) the max differences are 0.3%

<img src="{{ site.url }}assets/images/power_dm_nyx_251.png">


### Tmperature:

The initial temperature set by Nyx is $$1000 K$$ at $$z=100$$,  I believe this is too high, previously I always used $$170 K$$ for the initial temperature. Here is the mean temperature evolution for both codes, the green line is the $$a^{-2}$$ dependence expected for a $$\gamma = 5/3$$ under cosmological adiabatic expansion.

<img src="{{ site.url }}assets/images/temp_nyx.png">
