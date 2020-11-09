---
layout: post
title: "T0 and tau_eff: Rescaling HeII rates"
date:   2020-11-01 10:10:24 -0800
categorines: cholla
---


<img src="{{ site.url }}assets/images/grid_phase_diagram.png">



Comapred to the results from my one-cell analytical model:

<img src="{{ site.url }}assets/images/new_temp_evolution_HeII_scale.png">

From an MCMC sampling over the **scale_He** parameter the posterior distribution is shown below, vertical lines show the mean and the 2-sigma interval: 


<img src="{{ site.url }}assets/images/scale_He.png">



If I sample T0 from the the **scale_He** distribution obtained and compare to the data:



<img src="{{ site.url }}assets/images/mcmc_phase_diagram.png">





Finally, for the fit I only compared against the Gaikwad T0 data since the effect of  changing **scale_He** in the optical depth is not very significant but I'll extend to fit against $$\tau_{eff}$$ when doing the multi-parameter fit:


<img src="{{ site.url }}assets/images/grid_optical_depth.png">


