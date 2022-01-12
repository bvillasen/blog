---
layout: post
title: "WDM Simulations: MCMC fit using covariance matrix"
date:   2022-01-10 010:00:24 -0800
categorines: cholla
---

Now I fit out grid of 600 simulations using the $$P(k)$$ covariance matrix from Boera et al., below are the posterior distributions comparing to the distributions when only the uncertainty in the data $$sigma$$ is used for the likelihood. To check the implementation I also include the result of using a simplified matrix where only the diagonal elements are non-zero which should yield the same result as when using $$sigma$$.


<img src="{{ site.url }}assets/images/wdm_mcmc_fit_new/corner_multiple.png">


The distributions when using the covariance matrix suggest that a $$m_\mathrm{WDM}~4$$ is preferred over $$CDM$$ which is interesting     



<img src="{{ site.url }}assets/images/wdm_mcmc_fit_new/corner_covMatrix.png">


Below is the evolution of the temperature after marginalizing over the distributions obtained using the covariance matrix for the likelihood calculation



<img src="{{ site.url }}assets/images/wdm_mcmc_fit_new/fig_T0_wdm_covMatrix.png">
