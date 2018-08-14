---
layout: post
title:  "CHOLLA_PM Test: Difference to Enzo Results"
date:   2018-08-12 17:10:24 -0800
categories: cholla
---

## Difference in power spectrum compared to Enzo results

### Dual Energy is OFF on Cholla, Dual Energy is ON in Enzo
<img src="{{ site.url }}assets/images/power_enzo_error_noDE.png">




### Dual Energy is ON on Cholla , Dual Energy is ON in Enzo
<img src="{{ site.url }}assets/images/power_enzo_error_DE.png">




## Mean Temperature comparison

*Cholla_DE:* Cholla with Dual Energy ON


*Cholla_DE_E:* Cholla with Dual Energy ON, internal energy measured from Total Energy


*Cholla_noDE:* Cholla with Dual Energy OFF,  mean temperature is negative for most of the simulation

<img src="{{ site.url }}assets/images/internal_energy_enzo.png">



<img src="{{ site.url }}assets/images/internal_energy_error.png">
