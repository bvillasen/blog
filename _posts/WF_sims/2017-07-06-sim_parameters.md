---
layout: post
title:  "WFIRST Simulation parameters"
date:   2017-07-10 17:10:24 -0800
categories: cosmology wfirst
---

Parameters used for Millenium simulations [Here](http://gavo.mpa-garching.mpg.de/Millennium/Help/simulation)

**Softening**
From *Power et al 2003 numerical convergence criteria*, in order to get a well resolved halo:

$$ \epsilon_{opt} \, = \,  \frac{4r_{200}}{\sqrt{N_{200}}} $$


The size of the box is **115 Mpc/h**

| $$N_{part}$$ |  $$\epsilon$$ [kpc/h]  |
| :------: | --------------: |
| $$128^3$$    |   19.41  |
| $$256^3$$    |   9.70   |
| $$512^3$$    |    4.85  |
| $$1024^3$$   |    2.42  |
| $$2048^3$$   |    1.21 |
| $$4096^3$$   |    0.61 |


Results for $$256^3$$ simulation using $$\epsilon=9.7$$:


<img src="{{ site.url }}assets/images/dens_53_soft10.png">

<img src="{{ site.url }}assets/images/massFunc_53_soft10.png">
