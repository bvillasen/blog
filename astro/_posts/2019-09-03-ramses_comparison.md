---
layout: post
title:  "Cholla_PM: Ramses Comparison"
date:   2019-09-02 17:10:24 -0800
categories: cholla
---
Here is the Comparison against Ramses:

## DM Only Comparison:

Initially this was the power spectrum comparison:

<img src="{{ site.url }}assets/images/power_dm_ramses_0.png">


Surprisingly RAMSES has ~30% more power then Cholla on small scales. For reference, Cholla has ~25% more power than Enzo on similar scales. 

On the Ramses paper they say: **Using the potential, the acceleration is computed on the
mesh using the 5-points finite difference approximation of
the gradient.**

I changed the way the gravitational field is computed from the potential, originally I was using  3 point finite differences for  the derivatives for the gradient :

$$\frac{\partial \phi_{i,j,k}}{\partial x}  = \frac{1}{2 \Delta x} \left(  \phi_{i+1,j,k} - \phi_{i-1,j,k}  \right)$$

I changed for the 5 point finite differences: 

$$\frac{\partial \phi_{i,j,k}}{\partial x}  = \frac{1}{12 \Delta x} \left( -\phi_{i+2,j,k} + 8\phi_{i+1,j,k} - 8\phi_{i-1,j,k} + \phi_{i-2,j,k}  \right)$$

Now the results are much better:

<img src="{{ site.url }}assets/images/power_dm_ramses_2.png">

Differences are <~1%.

## Hydro Comparison:

I still have the temperature issue in Ramses:

<img src="{{ site.url }}assets/images/temperature_comparison.png">

 
