---
layout: post
title:  "CHOLLA_PM Test: Gas Internal Energy and Power Spectrum (UPDATE)"
date:   2018-04-17 17:10:24 -0800
categories: cholla
---


## Physical mean Internal Energy for early redshift

**CASE 1:** Zero initial velocities, no gravity acting on the gas

<img src="{{ site.url }}assets/images/internal_energy_z_v0_g0.png">



**CASE 2:** Initial velocities, NO gravity acting on the gas

<img src="{{ site.url }}assets/images/internal_energy_z_v1_g0.png">

**CASE 3:** Initial velocities,  Now gravity is acting on the gas, and the gas cools very fast.

<img src="{{ site.url }}assets/images/internal_energy_z_v0_g1.png">

**From Initial Conditions**


Dens mean: 13.4874  


U mean: 0.00017072  $$km^2/s^2$$


Ek mean: 0.15950561  $$km^2/s^2$$




## Physical mean Internal Energy for the entire simulation

<img src="{{ site.url }}assets/images/internal_energy_v1_g1.png">


## Density Power Spectrum (update)

**PREVIOUS:** For this case the gravitational force acting on the Kinetic Energy of the gas was computed from the Virtual Work done by the gravitational force $$\Delta E = dt (-\rho \nabla \phi \cdot \overrightarrow{v}) $$

<img src="{{ site.url }}assets/images/power_dm_gas_update.png">


**NOW:** Instead of using the virtual work, I compute the change in momentum and use it to compute the change in Kinetic Energy
$$\Delta E= dt( \Delta (P^2) / ( 2\rho ) ) $$

<img src="{{ site.url }}assets/images/power_v1_g3.png">
