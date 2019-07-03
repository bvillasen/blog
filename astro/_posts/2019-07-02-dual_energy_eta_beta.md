---
layout: post
title:  "Cholla_PM: Dual Energy Eta Beta and Pressure Jump"
date:   2019-07-02 17:10:24 -0800
categories: cholla
---

The simulations are $$128^3$$ and 50Mpc.

**Dual Energy Parameters:** $$\eta=0.005$$    $$\beta_0 = 0.25$$     $$\beta_1 = 0.0$$

### Shock Detection

**Pressure Jump:**

From Fryxell 200 the Pressure Jump Condition for shock detection is:

 $$\frac{\left|\langle P\rangle_{i+1}^{n}-\langle P\rangle_{i-1}^{n}\right|}{\min \left(\langle P\rangle_{i+1}^{n},\langle P\rangle_{i-1}^{n}\right)}> \alpha \gamma \frac{\left|\langle\rho\rangle_{i+1}^{n}-\langle\rho\rangle_{i-1}^{n}\right|}{\min \left(\langle\rho\rangle_{i+1}^{n},\langle\rho\rangle_{i-1}^{n}\right)}$$
 
 Their implementation uses $$\alpha = 0.1$$
 
 To ignore fluctuations due to noise a condition in the density is also applied:
 
 $$\frac{\left|\langle\rho\rangle_{i+1}^{n}-\langle\rho\rangle_{i-1}^{n}\right|}{\min \left(\langle\rho\rangle_{i+1}^{n},\langle\rho\rangle_{i-1}^{n}\right)}<0.01 $$
 
 
### Phase Diagram

**Row 1:** Without Pressure Jump Condition

Now Using Pressure Jump condition:

**Row 2:** Using $$\alpha=0.1$$

Now only using the Total Internal Energy  if  $$U_{total} > U_{advected}$$ 

**Row 3:** Using $$\alpha=1.0$$

**Row 4:** Using $$\alpha=10.0$$

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_DE_beta_simple_Pressure10.mp4" width="500" height="500" controls preload> </video>
</div>



### Chemistry Projection

**No Pressure Jump Condition**


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/chemistry_DE_beta_simple.mp4" width="500" height="500" controls preload> </video>
</div>


**Using Pressure Jump Condition** $$\alpha=10.0$$

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/chemistry_DE_beta_simple_Pressure10.mp4" width="500" height="500" controls preload> </video>
</div>



### Power Spectrum


**No Pressure Jump Condition**

 <img src="{{ site.url }}assets/images/ps_0.005_cooling_uv_PPMC_HLLC_SIMPLE_eta0.005_beta0.250_0.000.png">


**Using Pressure Jump Condition**  $$\alpha=10.0$$

 <img src="{{ site.url }}assets/images/ps_0.005_cooling_uv_PPMC_HLLC_SIMPLE_eta0.005_beta0.250_0.000_PressureJump10.png">





 