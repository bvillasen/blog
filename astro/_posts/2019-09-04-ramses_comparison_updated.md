---
layout: post
title:  "Cholla_PM: Ramses Comparison Updated"
date:   2019-09-04 17:10:24 -0800
categories: cholla
---
Here is the Comparison against Ramses:

## DM Only Comparison:

For a 256^3 particles on a 50 Mpc/h box the power spectrum is very similar: 

<img src="{{ site.url }}assets/images/power_dm_256_ramses.png">

Differences are < 0.5%.

## Hydro Comparison:

After changing to the parameters suggested by Romain:

 
<img src="{{ site.url }}assets/images/temperature_comparison_0.png">


After changing Dual Energy in Cholla to add the Truncation Error condition.

<img src="{{ site.url }}assets/images/temperature_comparison_beta0.3_slope1.png">

I compared the gas power spectrum using several parameters, the best match was when setting the slope limiter in ramses to 1 and $$\beta=0.2$$  $$\eta=0.3$$.

```
slope_limiter = Type of slope limiter used in the Godunov scheme for the piecewise linear reconstruction: slope_type=0: First order scheme, slope_type=1: MinMod limiter, slope_type=2: MonCen limiter, slope_type=3: Multi-dimensional MonCen limiter. 
```

<img src="{{ site.url }}assets/images/ps_128_hydro_ramses_PLMC_beta0.20_eta0.030_slope1.png">

I tried running Ramses+Grackle but it seems like Ramses is not doing the advection of the chemical species and only pases neutral hydrogen and helium density based on hydrogen fraction X, seems like ionized fractions are always 0.
