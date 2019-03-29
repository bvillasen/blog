---
layout: post
title:  "CHOLLA_PM: Dual energy separate total and avdected internal energy updated"
date:   2019-03-28 17:10:24 -0800
categories: cholla
---

Now the Advected Internal Energy $$ge_{advected}$$ is set equal to the internal energy computed from the total energy $$ge_{total}$$ when $${ge_total}$$ is used to compute the pressure. 

**Column 1:**  ENZO

**Column 2:**  Phase diagram for All Gas ( top ) and Neutral Hydrogen ( bottom ). Temperature is internally computed by Grackle on run time.

**Column 3:**  Phase diagram for the fraction of the gas that uses the Total Internal Energy to compute pressure.

**Column 4:**  Phase diagram for the fraction of the gas that uses the Adavected Internal Energy to compute pressure.


**Column 5:**  Phase diagram showing the temperature computed from the Total Internal Energy for ALL the gas.

**Column 6:**  Phase diagram showing the temperature computed from the Advected Internal Energy for ALL the gas.

**First 2 rows:** CHOLLA computing pressure from total internal energy or advacted internal enegy using $$\eta_1=0.001 $$ and $$\eta_2 =0.1$$ ( same as Bryan 2014 )

**Last 2 rows:** CHOLLA computing pressure from total internal energy or advacted internal enegy using $$\eta_1=0.02 $$ and $$\eta_2 =0.1$$ 

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_separateDE_new.mp4" width="500" height="500" controls preload> </video>
</div>


