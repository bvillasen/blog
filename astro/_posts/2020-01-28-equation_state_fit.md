---
layout: post
title:  "Equation of State Fitting"
date:   2020-01-28 17:10:24 -0800
categories: gas cholla
---


Here I fit the phase diagram to the model:

$$ T(\Delta) = T_0 \Delta ^\gamma $$


First I do it by minimizing $-  \sum log[ P(\delta, T) ]$ with the help of scipy, this is the result:

<img src="{{ site.url }}assets/images/phase_diagram_fit_scipy.png"> 

Now, I run an MCMC top sample the space of parameters {$$T_0$$, $$gamma$$} that maximize the probability $\sum log[ P(\delta, T) ]$, I use the *pymc* package to do so and from the sampling I get the posterior distribution for the parameters: 

**Sampling for $$T_0$$:** 

<img src="{{ site.url }}assets/images/sampling_T0.png"> 

**Sampling for $$\gamma$$:** 

<img src="{{ site.url }}assets/images/sampling_gamma.png"> 



From the distributions I can get the mean and the standard deviation for the parameters:

$$ T_0 = 3.96875 \pm 0.00016$$

$$\gamma = 0.44024 \pm 0.00017 $$