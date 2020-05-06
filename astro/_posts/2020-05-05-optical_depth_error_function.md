---
layout: post
title: "Optical Depth Integrated (Error Function)"
date:   2020-05-5 10:10:24 -0800
categorines: dm cholla
---

The depth distribution of an absorber that corresponds to the $$i$$ cell with neutral hydrogen density $$n_{mathrm{HI},i}$$, Doppler parameter $$b_i$$ and velocity $$v_i$$ can be expressed as a Gaussian given by:

$$\Phi_i(v) = n_{mathrm{HI},i} \int \frac{1}{\sqrt{\pi} b_i} e ^{ -(\frac{v-v_i}{b_i} )^2 }   dv $$

<img src="{{ site.url }}assets/images/gaussian_0.png">




<img src="{{ site.url }}assets/images/gaussian_1.png">


The definition of the error function is given by:

$$\operatorname{erf} x=\frac{1}{\sqrt{\pi}} \int_{-x}^{x} e^{-t^{2}} d t$$

<img src="{{ site.url }}assets/images/gaussian_2.png">

<img src="{{ site.url }}assets/images/gaussian_3.png">

<img src="{{ site.url }}assets/images/gaussian_4.png">

