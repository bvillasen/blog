---
layout: post
title:  "Cholla_PM: Ramses and Enzo Comparison"
date:   2019-09-10 18:10:24 -0800
categories: cholla
---

Here is the comparison for the average temperature in a cosmological simulation.**All codes are using the 4th order scheme for the potential gradient**. 

Cholla is using  **PPMP** **HLLC**  and  **SIMPLE**, $$\beta=0$$.

<img src="{{ site.url }}assets/images/temperature_comparison_enzo_ramses.png">


Now using Cooling and UV Background:

<img src="{{ site.url }}assets/images/temperature_comparison_enzo_ramses_uv.png">

## Power Spectrum

Here is the power spectrum for Cholla and Enzo without using Cooling/UV:

### $$\eta=0.005$$

<img src="{{ site.url }}assets/images/ps_128_hydro_enzo_SIMPLE_PPMP_eta0.005_beta0.00_grav4.png">

### $$\eta=0.010$$

<img src="{{ site.url }}assets/images/ps_128_hydro_enzo_SIMPLE_PPMP_eta0.010_beta0.00_grav4.png">

### $$\eta=0.035$$

<img src="{{ site.url }}assets/images/ps_128_hydro_enzo_SIMPLE_PPMP_eta0.035_beta0.00_grav4.png">

### $$\eta=0.035$$ and $$\beta=0.2$$:
**These where the parameters that best matched Ramses: Gas is much colder.**

<img src="{{ site.url }}assets/images/ps_128_hydro_enzo_SIMPLE_PPMP_eta0.035_beta0.20_grav4.png">


**Now using Cooling and UV Background:**

### $$\eta=0.010$$

<img src="{{ site.url }}assets/images/ps_128_SIMPLE_PPMP_eta0.010_beta0.00_grav4.png">


### $$\eta=0.035$$

<img src="{{ site.url }}assets/images/ps_128_SIMPLE_PPMP_eta0.035_beta0.00_grav4.png">
