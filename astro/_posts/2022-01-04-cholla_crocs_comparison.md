---
layout: post
title: "Crocs - Cholla Halos comparison "
date:   2022-01-02 010:00:24 -0800
categorines: cholla
---

I ran Rockstar on the 40 Mpc/h and N=1024$$^3$$ Dark Matter Only simulation and compare the halo mass function from the Cholla halo catalog to the Crocs halo catalog:

Here is the mass function **including Subhalos**

<img src="{{ site.url }}assets/images/crocs_comparison/mass_function_comparison_crocs_raw.png">


Clearly the is a multiplicative offset. If I rescale the Crocs halo masses by $$h^{-1}$$ the result is much better.

<img src="{{ site.url }}assets/images/crocs_comparison/mass_function_comparison.png">



Conclusions:

1. Seems like there is a factor of $h$ missing from the halo masses in one of the catalogs.
2. There are more low mass halos in the Cholla catalogs, note that all this have sizes smaller than one cell of the uniform grid. 


