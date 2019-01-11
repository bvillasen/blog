---
layout: post
title:  "Pleiades Charging"
date:   2017-07-10 17:10:24 -0800
categories: cosmology wfirst
---

Parameters used for Millenium simulations [Here](http://gavo.mpa-garching.mpg.de/Millennium/Help/simulation)


The size of the box is **115 Mpc/h**

| $$N_{part}$$ |  $$\epsilon$$ [kpc/h]  |  CPU Time [Hrs] |  Wall Time  [Hrs]  |
|:------:|:--------------:|:----------------:|:-----------------:|
| $$128^3$$    |   19.41  |  6.0   |  0.4  |
| $$256^3$$    |   9.70   |  29.0  |  1.8  |
| $$512^3$$    |    4.85  |  165.5 |  10.3 |
| $$1024^3$$   |    2.42  |        |       |
| $$2048^3$$   |    1.21 |        |       |
| $$4096^3$$   |    0.61 |        |       |


**SBU rates: **

Broadwell	4.04
Haswell	3.34
Ivy Bridge	2.52
Sandy Bridge	1.82

pleiades_S or pleiades_ch3 (for Sandy Bridge nodes)
pleiades_I or pleiades_ch4 (for Ivy Bridge nodes)
pleiades_H or pleiades_ch6 (for Haswell nodes)
pleiades_B or pleiades_ch7 (for Pleiades Broadwell nodes)






CPU_TIME as function of N_PARTICLES:


<img src="{{ site.url }}assets/images/timming.png">
