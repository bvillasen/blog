---
layout: post
title:  "Cholla_PM: Zeldovich Beta Condition"
date:   2019-09-10 17:10:24 -0800
categories: cholla
---

Here is the comparison for Zeldovich, all cases use  **PPMP** **HLLC**  and  **VL**, the Dual Energy parameters are:


Also, I found that Enzo can use the 4th order method to get the gradient of the potential, here I am using that method.

**$$\eta_1 = 0.001 $$**  **$$\eta_2 = 0.010 $$**
<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_eta0.01_beta0.00_grav4.mp4" width="100%"  height="auto" controls preload> </video>
</div>

Now also using the truncated error condition like Ramses using $$\beta=0.05$$ and same $$\eta_2$$

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_eta0.01_beta0.05_grav4.mp4" width="100%"  height="auto" controls preload> </video>
</div>