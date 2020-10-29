---
layout: post
title: "Single Cell T0 Model Comparison"
date:   2020-10-28 10:10:24 -0800
categorines: cholla
---

The model is solving:

$$\frac{d T}{d t}=-2 H T+\frac{2 T}{3 \Delta} \frac{d \Delta}{d t} - \frac{T}{\sum_i X_i }\frac{d \sum_i X_i}{dt}   +\frac{2}{3 k_{B} n_{t o t}} \frac{d Q}{d t} $$

<img src="{{ site.url }}assets/images/temp_evolution_Grackle.png">







Below is the evolution of the Density-Temperature distribution


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_uvb_comparison_balck.mp4" width="100%"  height="auto" controls preload> </video>
</div>