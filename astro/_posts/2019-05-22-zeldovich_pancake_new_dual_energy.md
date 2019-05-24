---
layout: post
title:  "CHOLLA_PM: Zeldovich Pancake new Dual Energy Scheme"
date:   2019-05-22 17:10:24 -0800
categories: cholla
---


Using the new Dual Energy Scheme From Teyssier 2015, for PPMC + HLLC + SIMPLE:

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_enzo_simple_beta.mp4" width="500" height="500" controls preload> </video>
</div>  

The Total Internal energy is used where $$\Delta v \approx 0$$ and the delay in the formation of the shock is still there.


Comparing to the Evolution when not Using Dual Energy:


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_enzo_simple_beta_noDE.mp4" width="500" height="500" controls preload> </video>
</div>  

Using The Gravitational Work to update the Total Energy and Teyssier scheme:
  

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_enzo_simple_beta_gravWork.mp4" width="500" height="500" controls preload> </video>
</div>    

Using The both Dual Energy Conditions ( Enzo and Teyssier):
  

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_enzo_simple_beta_convDE.mp4" width="500" height="500" controls preload> </video>
</div>    