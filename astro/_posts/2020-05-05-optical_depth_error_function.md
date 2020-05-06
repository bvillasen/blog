---
layout: post
title: "Optical Depth Integrated (Error Function)"
date:   2020-05-5 10:10:24 -0800
categorines: dm cholla
---

The depth distribution of an absorber that corresponds to the $$i$$ cell with neutral hydrogen density $$n_{\mathrm{HI},i}$$, Doppler parameter $$b_i$$ and velocity $$v_i$$ can be expressed as a Gaussian given by:

$$\Phi_i(v) = n_{\mathrm{HI},i} \int \frac{1}{\sqrt{\pi} b_i} \mathrm{exp} \left[ -\left(\frac{v-v_i}{b_i} \right)^2 \right]  dv $$


Note that the velocity of the absorber $$v_i$$ includes the Hubble flow velocity at the position of cell $$i$$ and the peculiar velocity of the gas at that position:

$$v_i = v_{\mathrm{H},i} + v_{\mathrm{LOS},i} $$

This distribution is shown in the figure below

<img src="{{ site.url }}assets/images/gaussian_0.png">



To compute the contribution of the absorber $$i$$ to the optical depth at cell $$j$$ located at the velocity coordinate $$v_j$$ we must integrate the Gaussian profile over the cell $$j$$, this is:


$$\tau_{j,i} = \int_{v_{j-1/2}}^{v_{j+1/2}} \Phi_i(v)  dv $$

That integral corresponds to the area shown in the  figure below:

<img src="{{ site.url }}assets/images/gaussian_1.png">


The definition of the error function is given by:

$$\operatorname{erf} x=\frac{1}{\sqrt{\pi}} \int_{-x}^{x} e^{-t^{2}} d t$$


Defining $$y_{j+1/2} = ( v_{j+1/2} - v_i )/b_i$$,    then the error function evaluated at $$y_{j+1/2}$$ corresponds to the area in the figure below:


<img src="{{ site.url }}assets/images/gaussian_2.png">



Similarly for $$y_{j-1/2} = ( v_{j-1/2} - v_i )/b_i$$,    then the error function evaluated at $$y_{j-1/2}$$ corresponds to the area in the figure below:


<img src="{{ site.url }}assets/images/gaussian_3.png">


Then subtracting the integrals results in the area below:


<img src="{{ site.url }}assets/images/gaussian_4.png">



For this reason there is a factor of 2 that has to be included, this results in the contribution to the optical depth at cell $$j$$ from cell $$i$$ given by:


$$\tau_{j,i} = n_{\mathrm{HI},i} \frac{ erf(y_{j+1/2})  - erf(y_{j-1/2}) }{2} $$

