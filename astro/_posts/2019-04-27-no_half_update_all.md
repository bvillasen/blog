---
layout: post
title:  "CHOLLA_PM: No half update"
date:   2019-04-26 17:10:24 -0800
categories: cholla
---


**Column 1:**  ENZO

**Column 2:**  Phase diagram for All Gas ( top ) and Neutral Hydrogen ( bottom ). Temperature is internally computed by Grackle on run time.

**Column 3:**  Phase diagram for the fraction of the gas that uses the Total Internal Energy to compute pressure.

**Column 4:**  Phase diagram for the fraction of the gas that uses the Adavected Internal Energy to compute pressure.


**Column 5:**  Phase diagram showing the temperature computed from the Total Internal Energy for ALL the gas.

**Column 6:**  Phase diagram showing the temperature computed from the Advected Internal Energy for ALL the gas.

Here is a comparison of the phase diagram using for all the reconstruction methods without the half-step update.

**Row 1:** PCM

**Row 2:** PLMP 

**Row 3:** PLMC

**Row 4:** PPMC

For some reason PPMP crashes immediately.

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_noFirst_all.mp4" width="500" height="500" controls preload> </video>
</div>

## Power Spectrum

### PCM



### PLMP 



### PLMC


### PPMC