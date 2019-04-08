---
layout: post
title:  "CHOLLA_PM: Dual energy advection test"
date:   2019-04-06 17:10:24 -0800
categories: cholla
---


**Column 1:**  ENZO

**Column 2:**  Phase diagram for All Gas ( top ) and Neutral Hydrogen ( bottom ). Temperature is internally computed by Grackle on run time.

**Column 3:**  Phase diagram for the fraction of the gas that uses the Total Internal Energy to compute pressure.

**Column 4:**  Phase diagram for the fraction of the gas that uses the Adavected Internal Energy to compute pressure.


**Column 5:**  Phase diagram showing the temperature computed from the Total Internal Energy for ALL the gas.

**Column 6:**  Phase diagram showing the temperature computed from the Advected Internal Energy for ALL the gas.

**Column 7:**  Advected test scalar initially set equal to the density.

This is the first test to compare the evolution of an advected extra scalar field to the density.


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_extra_scalar.mp4" width="500" height="500" controls preload> </video>
</div>

The advected extra scalar field follows the same evolution as the density. To test if the advection on the internal energy $$ge_{advected}$$ is correct I set the Internal Energy to be allways equal to the advected internal energy in all the box and removed the $$p \nabla \cdot \mathbf{v} $$ term from the advected internal energy integration. 

To account for the reionization heating, after $$z_{reionization}~15$$ I measure the average temperature and compute the heat energy needed to bring the average temperature up to $$3\times 10^3 K$$ and I apply this amount to all the cells on the box at each timestep, this keeps the average temperature at  $$3\times 10^3K$$, if the advection part is correct the temperature should remain uniform, ad it does!

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_temperature_unifrom.mp4" width="500" height="500" controls preload> </video>
</div>

Now I add the pressure term $$p \nabla \cdot \mathbf{v} $$ to the integration of the advected energy to see the effect of this term on the evolution of the advected internal energy (I multiplied the pressure term by $$1/5$$) 

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_temperature_pressure_5.mp4" width="500" height="500" controls preload> </video>
</div>




Now I set a temperature floor at $$300K$$ after the hydro step and before the cooling. The absence of flase adiabats on lower temperatures indicates that the cooling step is unlikely to cause those false adiabats.

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_tempFloor.mp4" width="500" height="500" controls preload> </video>
</div>
