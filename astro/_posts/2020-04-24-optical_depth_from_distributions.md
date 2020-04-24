---
layout: post
title: "Effective Optical Depth from Density Distributions"
date:   2020-04-24 11:10:24 -0800
categorines: dm cholla
---


From the volume weighted density distributions below  it's possible to compute an approximate value for the effective optical depth in the simulations 

<img src="{{ site.url }}assets/images/density_distribution_new.png"> 



**From [Bolton et al. 2009](https://arxiv.org/abs/0901.3966)**


Assuming the IGM is highly ionised and in photoionisation equilibrium with the metagalactic UV background, and the low density IGM $$(\Delta = \rho/ \langle \rho /\rangle \leq 10)$$ follows a power-law temperature density relation, $$T = T_0  \Delta^{\gamma -1} $$ (Hui & Gnedin 1997; Valageas et al. 2002), the Lyα optical depth at z >∼2 may be written as: 

$$\begin{aligned}
\tau \simeq & 1.0 \frac{\left(1+\chi_{\mathrm{He}}\right)}{\Gamma_{-12}}\left(\frac{T_{0}}{10^{4} \mathrm{K}}\right)^{-0.7}\left(\frac{\Omega_{\mathrm{b}} h^{2}}{0.024}\right)^{2}\left(\frac{\Omega_{\mathrm{m}} h^{2}}{0.135}\right)^{-1 / 2}  \left(\frac{1+z}{4}\right)^{9 / 2} \Delta^{2-0.7(\gamma-1)}
\end{aligned}$$