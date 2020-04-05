---
layout: post
title: "SPH Kernel Density"
date:   2020-04-05 18:10:24 -0800
categories: dm cholla
---

From the Gadget2 paper:

The kernel as a function of distance $$r$$ and smoothing length $$h$$ is given by:

$$W(r, h)=\frac{8}{\pi h^{3}}\left\{\begin{array}{ll}
1-6\left(\frac{r}{h}\right)^{2}+6\left(\frac{r}{h}\right)^{3}, & 0 \leqslant \frac{r}{h} \leqslant \frac{1}{2} \\
2\left(1-\frac{r}{h}\right)^{3}, & \frac{1}{2}<\frac{r}{h} \leqslant 1 \\
0, & \frac{r}{h}>1
\end{array}\right.$$ 






### Density Comparison

<img src="{{ site.url }}assets/images/density_kernel_0.png"> 


Now I show the distribution of the fractional differences

<img src="{{ site.url }}assets/images/density_difference_0.png"> 
