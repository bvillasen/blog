---
layout: post
title: "Paper Summary: Boera et al. 2019"
date:   2020-03-21 17:10:24 -0800
categories: dm cholla
---


[Link to paper here](https://ui.adsabs.harvard.edu/abs/2019ApJ...872..101B/abstract)

They ran a suite of 30 simulations most of them consist of a 10 Mpc/h box and $$2 \times 512^3$$ gas and dark matter particles. The simulations differ on the amplitude of and time of start for the photoheating rates ( they don't explicitly mention that they also changed the photoionization rates ), they heating rates are just the original HM12 rates multiplied by a constant $$\epsilon_{i}=\zeta \epsilon_{i}^{H M 12}$$, where $$\zeta$$ takes the following values [ 0.3, 0.55, 1.0, 1.8, 3.3 ], the start redshift for reionization $$z_{OT}$$ takes the possible values [ 7, 9, 12, 15, 19 ]. The next figure shows the effect of varying $$\zeta$$ and $$z_{OT}$$ on $$t_0$$ and the integrated integrated heating per unit mass $$u_0$$.


<img src="{{ site.url }}assets/images/boera_0.png">

Then they artificially extend their simulation by changing $$T_0$$, $$\gamma$$, $$\tau_eff$$, and $$u_0$$ as postprocesing, the next figure shows the effect that changing this values has on the Flux Power Spectrum.


<img src="{{ site.url }}assets/images/boera_1.png">
