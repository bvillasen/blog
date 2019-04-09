---
layout: post
title:  "CHOLLA_PM: Dual energy revised pressure term"
date:   2019-04-07 17:10:24 -0800
categories: cholla
---


**Column 1:**  ENZO

**Column 2:**  Phase diagram for All Gas ( top ) and Neutral Hydrogen ( bottom ). Temperature is internally computed by Grackle on run time.

**Column 3:**  Phase diagram for the fraction of the gas that uses the Total Internal Energy to compute pressure.

**Column 4:**  Phase diagram for the fraction of the gas that uses the Adavected Internal Energy to compute pressure.


**Column 5:**  Phase diagram showing the temperature computed from the Total Internal Energy for ALL the gas.

**Column 6:**  Phase diagram showing the temperature computed from the Advected Internal Energy for ALL the gas.


For all the simulations below the advected internal energy and the total internal energy are synchronized and the advected internal energy is used for the condition with $$\eta_1=0.02$$

First I want to make sure that our conclusion about the false adiabats is correct, for this I turn on grackle cooling and after Reionization I don't apply the cooling update to cells which temperature is below 300K, as expected several cells move to the temperature floor but without them being heated by the UV background they don't move to form the false adiabats.


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_de02_oldP_tempLimit.mp4" width="500" height="500" controls preload> </video>
</div>

Now I changed the pressure term on for the advected internal energy on cholla to:

$$p_{j}^{n}\left(\frac{\overline{v}_{j+1 / 2}-\overline{v}_{j-1 / 2}}{\Delta x_{j}}\right)$$

and the comparison is below:

**Row 1** Evolution with the previous form of the pressure term on the advected internal energy.

**Row 2** Evolution with the revised form of the pressure term on the advected internal energy.

**Row 3** Evolution with the previous form of the pressure term but using a time step 10 times smaller $$\Delta a = 0.0001$$.


There's practically no difference when changing the pressure term, and using a small time step reduces the lower temperature deviations but not completely. 

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_testP.mp4" width="500" height="500" controls preload> </video>
</div>
