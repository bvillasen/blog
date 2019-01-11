---
layout: post
title:  "CHOLLA_PM Test: Results for Dual Energy simulations"
date:   2018-05-03 17:10:24 -0800
categories: cholla
---

##Effect of applying a lower limit in the internal energy


### Physical mean Internal Energy vs. redshift


**Using DUAL ENERGY**

Also applying a lower limit to the internal Energy ( floor ) at $$u=2.0 km^2/s^2$$
<img src="{{ site.url }}assets/images/internal_energy_DE_pot2_floor.png">



A link for the code file were the lower limit is applied [HERE](https://github.com/bvillasen/cholla/blob/particles/src/hydro_cuda.cu).  Look for the kernel: **Apply_Internal_Energy_Floor**
