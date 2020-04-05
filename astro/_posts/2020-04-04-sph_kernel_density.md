---
layout: post
title: "SPH Kernel Density"
date:   2020-04-05 18:10:24 -0800
categories: dm cholla
---

**From the Gadget2 paper:**

The kernel as a function of distance $$r$$ and smoothing length $$h$$ is given by:

$$W(r, h)=\frac{8}{\pi h^{3}}\left\{\begin{array}{ll}
1-6\left(\frac{r}{h}\right)^{2}+6\left(\frac{r}{h}\right)^{3}, & 0 \leqslant \frac{r}{h} \leqslant \frac{1}{2} \\
2\left(1-\frac{r}{h}\right)^{3}, & \frac{1}{2}<\frac{r}{h} \leqslant 1 \\
0, & \frac{r}{h}>1
\end{array}\right.$$ 


> 
Of fundamental importance for any SPH formulation is the density estimate, which GADGET-2 does in the form
$$\rho_{i}=\sum_{j=1}^{N} m_{j} W\left(\left|\boldsymbol{r}_{i j}\right|, h_{i}\right)$$

>
where $$r_{ij} ≡ r_i − r_j$$ , and $$W(r, h)$$ is the SPH smoothing kernel
defined in equation (4).2 In our ‘entropy formulation’ of SPH, the
adaptive smoothing lengths $$h_i$$ of each particle are defined such
that their kernel volumes contain a constant mass for the estimated
density, i.e. the smoothing lengths and the estimated densities obey
the (implicit) equations
$$\frac{4 \pi}{3} h_{i}^{3} \rho_{i}=N_{\mathrm{sph}} \bar{m}$$
where $$N_{\mathrm{sph}} $$ is the typical number of smoothing neighbours, and $$\bar{m}$$
is an average particle mass.

**Some things to notice:**

The density at the $$i$$ particle position is computed by:

$$\rho_{i}=\sum_{j=1}^{N} m_{j} W\left(\left|\boldsymbol{r}_{i j}\right|, h_{i}\right)$$,

note that the smoothing length used is $$h_i$$ and not the smoothing length of the neighbors.


### Measuring $$N_{\mathrm{sph}}$$


From the equation:

$$\frac{4 \pi}{3} h_{i}^{3} \rho_{i}=N_{\mathrm{sph}} \bar{m}$$

I can use the values of $$\rho_i$$ and $$h_i$$ from the file to compute $$N_{\mathrm{sph}}$$, this is the distribution of values that I get.



<img src="{{ site.url }}assets/images/n_smmoth.png"> 

So, it seems like $$N_{\mathrm{sph}} \approx 64$$

 

 

### Density Comparison

<img src="{{ site.url }}assets/images/density_kernel_0.png"> 


Now I show the distribution of the fractional differences

<img src="{{ site.url }}assets/images/density_difference_0.png"> 
