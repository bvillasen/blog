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

The result was that the pressure term is cooling some of the cells and bringing them to temperatures below the temperature floor of $$1K$$ and then my simple heating scheme is heating those cells, look on the low temperature cells and you will see how they are moving over the temperature floor. My conclusion is that the false adiabats we have been seeing are the result of gas cooled to the temperature floor $$1k$$ on the Hydro step and then heated by the UV background, since the heating rate must have a dependency on the density that must be the origin of the slope on the false adiabats.




Now I set a temperature floor at $$300K$$ after the hydro step and before the cooling. The absence of flase adiabats on lower temperatures indicates that the cooling step is unlikely to cause those false adiabats.

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_tempFloor.mp4" width="500" height="500" controls preload> </video>
</div>


My conclusion is that the pressure term $$p \nabla \cdot \mathbf{v} $$ in the hydro step could be a source of error, in the ENZO paper they have:

$$\rho_{j}^{n+1} e_{j}^{n+1}=\rho_{j}^{n} e_{j}^{n}+\Delta t\left(\frac{\overline{\rho}_{j+1 / 2} \overline{v}_{j+1 / 2} \overline{e}_{j+1 / 2}-\overline{\rho}_{j-1 / 2} \overline{v}_{j-1 / 2} \overline{e}_{j-1 / 2}}{\Delta x_{j}}\right)-\Delta t p_{j}^{n}\left(\frac{\overline{v}_{j+1 / 2}-\overline{v}_{j-1 / 2}}{\Delta x_{j}}\right)$$

Following the equation above it seem like they use the values of the reconsructed velocities on the edges of the cell to compute $$ \nabla \cdot \mathbf{v} $$ while cholla is using the centered values on the neighboring cell

$$ p_{j}^{n}\left(\frac{\overline{v}_{j+1}-\overline{v}_{j-1}}{2*\Delta x_{j}}\right)$$