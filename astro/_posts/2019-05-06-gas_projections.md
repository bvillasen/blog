---
layout: post
title:  "CHOLLA_PM: Conserved Projections"
date:   2019-05-06 17:10:24 -0800
categories: cholla
---

The phase_diagram using a uniform initial velocity $$vx = vy = vz = 160 km/s $$ and no gravity ( cooling is on ) and $$\eta=0$$ (always using total internal energy):

**Row 1:** Normal pressure on the flux of E and momentum

**Row 2:** No pressure on the flux of E and momentum


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_uniform_vel.mp4" width="500" height="500" controls preload> </video>
</div>
 
No spurious heating of the gas!  

To track the differences on the hydro conserved variables I plot projections ( 5 Mpc deep );

I used PPCM for the reconstruction and HLLC for the Reimann solver.

First using $$\eta = 0.001$$ same as enzo:

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/projections_de001.mp4" width="500" height="500" controls preload> </video>
</div>


Now using $$\eta =0.02$$, here we are using more of the advected internal energy


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/projections_de02.mp4" width="500" height="500" controls preload> </video>
</div>


Now using $$\eta=1$$ always using advected internal energy and not synchronizing the total internal energy to see the independent evolution of the total internal energy.


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/projections_de1.mp4" width="500" height="500" controls preload> </video>
</div>


 Here is the phase diagram for the simulation using $$\eta=1$$ (only advected internal energy )

 <div style="text-align: center">
 <video src="{{ site.url }}assets/videos/phase_diagram_de1.mp4" width="500" height="500" controls preload> </video>
 </div>
  
 