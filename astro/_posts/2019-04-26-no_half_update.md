---
layout: post
title:  "CHOLLA_PM: No half update"
date:   2019-04-24 17:10:24 -0800
categories: cholla
---


**Column 1:**  ENZO

**Column 2:**  Phase diagram for All Gas ( top ) and Neutral Hydrogen ( bottom ). Temperature is internally computed by Grackle on run time.

**Column 3:**  Phase diagram for the fraction of the gas that uses the Total Internal Energy to compute pressure.

**Column 4:**  Phase diagram for the fraction of the gas that uses the Adavected Internal Energy to compute pressure.


**Column 5:**  Phase diagram showing the temperature computed from the Total Internal Energy for ALL the gas.

**Column 6:**  Phase diagram showing the temperature computed from the Advected Internal Energy for ALL the gas.

Here is a comparison of the phase diagram using PLMP reconstruction changing the way the Advected Internal Energy is evolved.

**Row 1:** PCM with half step update

**Row 2:** PCM **without** half step update

**Row 3:** PLMP with half step update

**Row 4:** PLMP **without** half step update


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_noFirst.mp4" width="500" height="500" controls preload> </video>
</div>
