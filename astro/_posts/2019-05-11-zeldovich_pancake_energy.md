---
layout: post
title:  "CHOLLA_PM: Zeldovich Pancake Energy Comparison"
date:   2019-05-06 17:10:24 -0800
categories: cholla
---


Here is the Zeldovich Pancake test for 4 different cases:

**1** Using Only **Advected** Internal Energy ( Blue Line )

**2** Using Only **Total** Internal Energy ( Orange Line )

**3** Using Only **Total** Internal Energy and **No Gravity** ( Green Line )

**4** Using Only **Total** Internal Energy and **No Gravity** and Initial Velocities Multiplied by 2 ( Red Line )

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_energy_1.mp4" width="500" height="500" controls preload> </video>
</div>

Without Gravity The Thermal Energy remains normal, but the kinetic energy is 10 times smaller. Possible conclusions: the gravity coupling is not correct for the total energy ( but it is correct for the momentum ) or in this regime where the kinetic energy is lower we don't see possible errors filtering from the kinetic energy in to the Internal energy. Since we see the same errors on the thermal energy when gravity is off and higher initial velocities then it appears like the high kinetic energy is the problem. 

To test if a smaller timestep makes a difference I ran the cases with no gravity for different initial velocities using $$\Delta a=1 \times 10^{-5}$$, here are the results:

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_energy_da00001.mp4" width="500" height="500" controls preload> </video>
</div>

Even when using a tiny timestep the high kinetic energy introduces errors on the thermal energy!
