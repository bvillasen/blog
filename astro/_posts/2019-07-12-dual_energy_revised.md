---
layout: post
title:  "Cholla_PM: Dual Energy Corrected"
date:   2019-07-13 17:10:24 -0800
categories: cholla
---

This is the new implementation of Dual Energy, following Bryan 2013:

The pressure is computed using the next condition:

$$
p=\left\{\begin{array}{ll}{\rho(\gamma-1)\left(E-\mathbf{v}^{2} / 2\right),} & {\left(E-\mathbf{v}^{2} / 2\right) / E>\eta_{1}} \\ {\rho(\gamma-1) e,} & {\left(E-\mathbf{v}^{2} / 2\right) / E<\eta_{1}}\end{array}\right.
$$

The Internal Energy is synchronized using **only** the next condition:

$$
e=\left\{\begin{array}{ll}{\left(E-\mathbf{v}^{2} / 2\right),} & {\rho\left(E-\mathbf{v}^{2} / 2\right) / \max \left(\rho_{j-1} E_{j-1}, \rho_{j} E_{j}, \rho_{j+1} E_{j+1}\right)>\eta_{2}} \\ {e,} & {\rho\left(E-\mathbf{v}^{2} / 2\right) / \max \left(\rho_{j-1} E_{j-1}, \rho_{j} E_{j}, \rho_{j+1} E_{j+1}\right)<\eta_{2}}\end{array}\right.
$$

## Comparison: VL and SIMPLE Integrators

Both simulations are using the next Dual Energy parameters: **$$\eta_1 = 0.001$$    $$\eta_2=0.03$$**

**Row 1:** SIMPLE Integrator

**Row 2:** VL Integrator

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_DE_VL.mp4" width="100%"  height="auto" controls preload> </video>
</div>

Let's forget about VL integrator.


## Changing $$\eta_2$$:

### Phase Diagram

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_several_eta2.mp4" width="100%"  height="auto" controls preload> </video>
</div>


### Power Spectrum

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/ps_128_eta2.mp4" width="100%"  height="auto" controls preload> </video>
</div>


### Cell Difference

Here is the L1 Distance defined for a field $$x$$ as:

$$
D_{L1} = \frac{1}{N} \sum \frac{ |  x_{i}^{cholla} - x_{i}^{enzo} |  }{ x_{i}^{enzo} }
$$

**NOTE:** The scale for each field is different.


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/l1_difference_eta2.mp4" width="100%"  height="auto" controls preload> </video>
</div>

## Projections

Dual Energy parameters used for Cholla: **$$\eta_1 = 0.001$$    $$\eta_2=0.03$$**


Now the projected distance is 25 Mpc/h  and **the difference ranges from [-1, 1].**

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/projections_eta2.mp4" width="100%"  height="auto" controls preload> </video>
</div>



## Zeldovich Pancake Revised

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_eta2.mp4" width="100%"  height="auto" controls preload> </video>
</div>


Now only for **$$\eta_2=0.03$$**


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_eta2_0.030.mp4" width="100%"  height="auto" controls preload> </video>
</div>

