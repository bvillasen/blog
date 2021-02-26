---
layout: post
title: "P(k) MCMC Fit to Boss Data "
date:   2021-02-24 11:21:24 -0800
categorines: cholla
---


From a set of 8 $$1024^3$$ simulations where the parameters are:


$$\beta_{\mathrm{He}} = [0.3 \,\,\,\, 0.9   ] $$
$$\beta_{\mathrm{H}} = [0.6 \,\,\,\, 1.0   ] $$
$$\Delta z_{\mathrm{He}} = [0.0 \,\,\,\, 0.8   ] $$


First I fit each redshift independently:

<img src="{{ site.url }}assets/images/flux_ps_sampling_large_individual_fits.png">

The 95% Highest Probability Interval from the posterior distribution of the fitted parameters ( as a function of redshift, since each redshift is fitted independently ) is shown below, **there are no constrains for the Helium parameters**:

<img src="{{ site.url }}assets/images/params_fit_single.png">



Now I fit all the redshifts simultaneously:

<img src="{{ site.url }}assets/images/flux_ps_sampling_large_all.png">


And the posterior distribution of the parameters are:


<img src="{{ site.url }}assets/images/corner.png">

**Resulting in a delayed Helium reionization but with High photoheating and photoinization rates.** 