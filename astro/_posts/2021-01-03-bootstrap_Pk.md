---
layout: post
title: "Bootstrap P(k)"
date:   2021-01-03 11:21:24 -0800
categorines: cholla
---


From a total of $$N_{T}=60000$$ skewers randomly chosen from the simulations I bootstrap the mean $$P(k)$$ by selecting samples of $$N_s$$ skewers and computing the mean from each sample, this is iterated 10000 times and from the obtained distribution of $$\overline{P(k)}$$ the covariance matrix is computed.

Below is the normalized ( $$C_{i,j} / \sqrt{C_{i,i} \,C_{j,j}}$$ ) covariance matrix for the $$N_s=50000$$ bootstrap at $$z=2$$ and $$z=5$$.

<img src="{{ site.url }}assets/images/cov_matrix.png">

The standard deviation of the power spectrum  is computed from the diagonal of the covariance matrix, below I show the fraction of $$\sigma$$ to $$P(k)$$        


<img src="{{ site.url }}assets/images/ps_sigma.png">


As shown the standard deviation is proportional to $$1/\sqrt{N_s}$$, if I choose the $$\sigma$$ from the $$N=5000$$ bootstrap then $$\sigma/P(k) \sim 0.1$$.

Below is the comparison to the data using $$\sigma$$ from the $$N_s=5000$$ bootstrap.


<img src="{{ site.url }}assets/images/flux_power_spectrum_grid_review.png">
 


<img src="{{ site.url }}assets/images/flux_power_spectrum_grid_review_BOSS.png">
 

