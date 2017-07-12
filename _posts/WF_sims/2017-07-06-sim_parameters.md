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

Gadget parameter file [HERE](https://github.com/bvillasen/blog/blob/master/assets/files/test_256.param)


<img src="{{ site.url }}assets/images/dens_53_soft10.png">

<img src="{{ site.url }}assets/images/massFunc_53_soft10.png">

From Gadget_guide:

>Gravity is softened with a spline, as outlined in the code paper. The softenings quoted here
>all refer to 2, the roughly equivalent Plummer softening length. Note that for the spline that is
>actually used, the force will be exactly Newtonian beyond h = 2.82. **The softening lengths are
>in internal length units**. For comoving integration, the softening refers to the one employed in
>comoving coordinates, which usually stays fixed during the simulation. However, employing
>the **MaxPhys** parameters described below the code can also be asked to switch to a fixed
>softening in physical scale below a certain redshift.

>In cosmological simulations, one sometimes wants to start a simulation with a softening 2 com
>that is fixed in comoving coordinates (where the physical softening, 2 phys = a2 com , then grows
>proportional to the scale factor a), but at a certain redshift one wants to freeze the resulting
>growth of the physical softening 2 max
>phys at a maximum value. These maximum softening lengths
>are specified by the Softening*MaxPhys parameters. In the actual implementation, the
>code uses 2 0 com = min(2 com , 2 max
>phys /a) as comoving softening.
