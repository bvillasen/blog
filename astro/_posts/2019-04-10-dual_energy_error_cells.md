---
layout: post
title:  "CHOLLA_PM: Dual energy: error cells"
date:   2019-04-09 17:10:24 -0800
categories: cholla
---


**Column 1:**  ENZO

**Column 2:**  Phase diagram for All Gas ( top ) and Neutral Hydrogen ( bottom ). Temperature is internally computed by Grackle on run time.

**Column 3:**  Phase diagram for the fraction of the gas that uses the Total Internal Energy to compute pressure.

**Column 4:**  Phase diagram for the fraction of the gas that uses the Adavected Internal Energy to compute pressure.


**Column 5:**  Phase diagram showing the temperature computed from the Total Internal Energy for ALL the gas.

**Column 6:**  Phase diagram showing the temperature computed from the Advected Internal Energy for ALL the gas.

First I limit the max fractional change of the advected internal energy to 0.5, the comparison is below, the first row is the evolution without restricting the max change and the second row is limiting the max change. 

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_limitChangeDE.mp4" width="500" height="500" controls preload> </video>
</div>

Now I track the first 5 cells to hit the temperature floor, here are their last steps ( cells marked in red ): 


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_error_cells.mp4" width="500" height="500" controls preload> </video>
</div>

From the  last snapshots I get the Advected Internal Energy ( U_advected ). also I write the change in Internal energy corresponding to the Advection term ( $$\Delta$$ advc_term ) and the change due to the divergence of the velocity ( $$\Delta$$ P Div(v) ).

The values as a function of time are shown below:

<img src="{{ site.url }}assets/images/error_cells_0.png">

The change due to the divergence term is always positive!

The Conclusion is that the divergence term is not causing the cooling of the gas, the error is coming from the advection term. 


