---
layout: post
title:  "Cholla_PM: Zeldovich Reconstruction Comparison"
date:   2019-08-11 17:10:24 -0800
categories: cholla
---

Here is the comparison for Zeldovich test using different reconstruction methods after the shock is developed, all cases use **HLLC**  and  **VL**, the Dual Energy parameters are:

**$$\eta_1 = 0.001 $$**  **$$\eta_2 = 0.030 $$**


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_z1.mp4" width="100%"  height="auto" controls preload> </video>
</div>

Here using **PPMP**:


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_PPMP.mp4" width="100%"  height="auto" controls preload> </video>
</div>


### PPMC Reconstruction:

From the **CHOLLA** paper:

*Our implementation of this method closely follows that outlined in Stone et al. (2008).* 

$$
\begin{aligned} \boldsymbol{W}_{L, A} &=\frac{1}{2}\left(\boldsymbol{w}_{i}+\boldsymbol{w}_{i-1}\right)-\frac{1}{6}\left(\delta \boldsymbol{w}_{i}-\delta \boldsymbol{w}_{i-1}\right) \\ \boldsymbol{W}_{R, A} &=\frac{1}{2}\left(\boldsymbol{w}_{i+1}+\boldsymbol{w}_{i}\right)-\frac{1}{6}\left(\delta \boldsymbol{w}_{i+1}-\delta \boldsymbol{w}_{i}\right) \end{aligned}
$$

But from **Stone et al. (2008)**  equation 46:

$$
\begin{array}{l}{\boldsymbol{w}_{L, i}=\left(\boldsymbol{w}_{i}+\boldsymbol{w}_{i-1}\right) / 2-\left(\delta \boldsymbol{w}_{i}^{m}+\delta \boldsymbol{w}_{i-1}^{m}\right) / 6} \\ {\boldsymbol{w}_{R, i}=\left(\boldsymbol{w}_{i+1}+\boldsymbol{w}_{i}\right) / 2-\left(\delta \boldsymbol{w}_{i+1}^{m}+\delta \boldsymbol{w}_{i}^{m}\right) / 6}\end{array}
$$

The signs are different. Changing the signs in **ppmc_cuda.cu** to match Stone (2008), I get the next result:

 
<div style="text-align: center">
<video src="{{ site.url }}assets/videos/zeldovich_PPMC.mp4" width="100%"  height="auto" controls preload> </video>
</div>


Seems similar to the evolution using **PPMP**, looks like there is an inconsistency between reconstruction methods.

