---
layout: post
title:  "Self Gravity: XSEDE report"
date:   2018-04-22 17:10:24 -0800
categories: cholla
---

In order to test the self-gravity implementation, I ran a $$512^3$$ adiabatic simulation of an ideal gas $$(\gamma = 5/3)$$ collapsing under it's own gravity.


The box size is $$L=1$$, the density in the box is $$\rho=0.1$$ and for the spherical region of $$R < 0.2 $$ there is an over-density of $$\rho=1$$. Initial velocities are uniform $$v=0$$ and pressure is uniform $$p=0.001$$.  


The next figures show density and potential center slices. The black circle corresponds to the analytical value for the radius of a uniform pressure-less system collapsing only under gravity.    

**Density**
<img src="{{ site.url }}assets/images/timelapse_collapse_dens.png">

**Potential**
<img src="{{ site.url }}assets/images/timelapse_collapse_pot.png">
