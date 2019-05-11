---
layout: post
title:  "CHOLLA_PM: Zeldovich Pancake"
date:   2019-05-06 17:10:24 -0800
categories: cholla
---

There is a Zeldovich Pancake test in Enzo using the next parameters

```
Lbox = 64 Mpc/h
n_cells = 256
H0 = 50 
Omega_m = 1
```

Setting the initial conditions ( z = 20 ) equal to the ones in Enzo and **Using the Only the Advected Internal Energy** the evolution is the following :


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_de1_enzo.mp4" width="500" height="500" controls preload> </video>
</div>

The evolution of the gas is very similar to enzo until the gas is very compressed and it is not shock heated because I am using the advected internal energy.

Now when I use the **Total Internal Energy** I get errors in the temperature almost immediately, as you can see below:

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_de001_enzo.mp4" width="500" height="500" controls preload> </video>
</div>

The error are not on the boundary conditions, if I move the peak the error still occur on the maxima and minima of the density field as you can see below:

 <img src="{{ site.url }}assets/images/zeldovich_4.png">
 
I conclude that since when using the advected internal energy the results are similar then overall the gravity and cosmology implementation are correct and there is still one error to find in the evolution of the total energy.

<!-- Now Setting the initial conditions to 

$$
\rho\left(x\right)=\rho_{0}\left[1-\frac{1+z_{i}}{1+z} \cos \left(k x\right)\right]^{-1} \\
v\left(x\right)=-H_{0} \frac{1+z_{i}}{(1+z)^{1 / 2}} \frac{\sin \left(k x\right)}{k} \\
T\left(x\right)=T_{\text {init}}\left[\frac{\rho\left(x\right)}{\overline{\rho}}\right]^{2 / 3}
$$

where $$k= 2 * \pi / L_{box}$$ , $$z_i=20 $$   -->