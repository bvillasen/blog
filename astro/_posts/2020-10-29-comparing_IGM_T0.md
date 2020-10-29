---
layout: post
title: "Single Cell T0 Model Comparison"
date:   2020-10-28 10:10:24 -0800
categorines: cholla
---

The model is solving:

$$\frac{d T}{d t}=-2 H T+\frac{2 T}{3 \Delta} \frac{d \Delta}{d t} - \frac{T}{\sum_i X_i }\frac{d \sum_i X_i}{dt}   +\frac{2}{3 k_{B} n_{t o t}} \frac{d Q}{d t} $$

<img src="{{ site.url }}assets/images/temp_evolution_Grackle.png">



The Cooling mechanisms for Bruno's model

* Collisional Excitation Cooling: 
- **HI + e:** Hui & Gnedin 97
- **HeII + e:** Hui & Gnedin 97


* Collisional Ionization Cooling: 
- **HI + e:** Katz et al 95
- **HeI + e:** Katz et al 95
- **HeII + e:** Katz et al 95


* Collisional Ionization Rates: 
- **HI + e:** Hui & Gnedin 97
- **HeI + e:** Abel et al. 97
- **HeII + e:** Abel et al. 97
- **HI + HI:** Lenzuni et at. 91
- **HII + HI:** Lenzuni et at. 91
- **HeI + HI:** Lenzuni et at. 91

* Recombination Cooling:
- **HII:** Hui & Gnedin 97
- **HeII:** Hui & Gnedin 97
- **HeII dielectronic:** Hui & Gnedin 97
- **HeIII:** Hui & Gnedin 97

* Recombination Rates:
- **HII:** Hui & Gnedin 97
- **HeII:** Hui & Gnedin 97
- **HeII dielectronic:**  Hui & Gnedin 97
- **HeIII:** Katz et al 95


* Bremsstrahlung Cooling: Katz et al 95
 
* CMB Compton Cooling: Milles & Ostriker 2001



Below is the evolution of the Density-Temperature distribution


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_uvb_comparison_balck.mp4" width="100%"  height="auto" controls preload> </video>
</div>