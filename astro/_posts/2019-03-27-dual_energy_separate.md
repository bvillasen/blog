---
layout: post
title:  "CHOLLA_PM: Dual energy separate total and avdected internal energy"
date:   2019-03-27 17:10:24 -0800
categories: cholla
---

**Column 1:**  ENZO

**Next three columns:** CHOLLA computing pressure from total internal energy or advacted internal enegy using $$\eta_1=0.001 $$ and $$\eta_2 =0.1$$ ( same as Bryan 2014 )

**Column 2:**  Phase diagram for All Gas ( top ) and Neutral Hydrogen ( bottom ). Temperature is internaly computed by Grackle on run time.

**Column 3:**  Phase diagram for the fraction of the gas that uses the Total Internal Energy to compute pressure.

**Column 4:**  Phase diagram for the fraction of the gas that uses the Adavected Internal Energy to compute pressure.


**Last three columns:** CHOLLA computing pressure from total internal energy or advacted internal enegy using $$\eta_1=0.02 $$ and $$\eta_2 =0.1$$ 


**Column 5:**  Phase diagram for All Gas ( top ) and Neutral Hydrogen ( bottom ). Temperature is internaly computed by Grackle on run time.

**Column 6:**  Phase diagram for the fraction of the gas that uses the Total Internal Energy to compute pressure.

**Column 7:**  Phase diagram for the fraction of the gas that uses the Adavected Internal Energy to compute pressure.


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_separateDE.mp4" width="500" height="500" controls preload> </video>
</div>



### Same as the previous diagrams but using the change in Kinetic Energy as the gravitational term on the Total Energy




<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_separateDE_delta_Ek.mp4" width="500" height="500" controls preload> </video>
</div>