---
layout: post
title:  "Cholla_PM: Enzo without Dual Energy "
date:   2019-07-03 17:10:24 -0800
categories: cholla
---


The Enzo Simulation is not using Dual Energy

The Cholla Simulation is using the same Dual Energy parameters as described in Enzo paper
**Dual Energy Parameters:** $$\eta=0.001$$    $$\beta_0 = 0.00$$     $$\beta_1 = 0.0$$

 
 
### Phase Diagram

**Row 1:** Using Change in Kinetic Energy for Total Energy Gravity Update.

**Row 2:** Using Gravitational Work for Total Energy Gravity Update.

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_DE_beta_simple_beta0.00_noDE.mp4" width="500" height="500" controls preload> </video>
</div>


After Reionization Enzo is stuck in error messages. 