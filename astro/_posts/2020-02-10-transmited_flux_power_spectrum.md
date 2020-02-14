---
layout: post
title:  "Transmitted Flux Power Spectrum"
date:   2020-02-10 17:10:24 -0800
categories: gas cholla
---

The input to the Flux Power Spectrum  is then flux as function of velocity, i.e. F (v), over some
velocity interval $$V$$ (in the data set this interval is chosen so that
one avoids the Lyman-$$\beta$$ forest, the quasar near zone, and potentially some strong absorbers; in the simulations it is set by the linear
extent of the simulated volume).

Given F and its mean, $$\langle F \rangle$$, we calculate the ‘normalized flux’

$$\delta_{F} \equiv \frac{F-\langle F\rangle}{\langle F\rangle} $$

The FPS is written in terms of the dimensionless variance $$\Delta_F^2(k)$$ (strictly speaking a variance in $$\delta_F$$ per dex in $$k$$), defined by


<!-- From **Whalther+2018**: We perform our power spectrum measurement on the flux contrast

$$\delta_{F}=\frac{F-\bar{F}}{\bar{F}}$$

with $$\bar{F}$$ being the mean transmission of the Lya forest, $$\bar{F}=\exp \left(-\tau_{\mathrm{eff}}\right)$$ with 

$$\tau_{\mathrm{eff}}=C+\tau_{0}\left(\frac{1+z}{1+z_{0}}\right)^{\beta}$$

following the functional form and parameters from Becker
et al. (2013): The best-fitting parameters are [$$\tau_0, \beta, C$$] = [0.751, 2.90, −0.132], for $$z_0  = 3.5$$.

\tau_{\mathrm{eff}}=C+\tau_{0}\left(\frac{1+z}{1+z_{0}}\right)^{\beta}
 -->



$$\Delta_{F}^{2}(k)=\frac{1}{\pi} k P_{F}(k) $$

$$P_{F}(k)=V  \bigg \langle  \left|\tilde{\delta}_{F}(k)\right|^{2}  \bigg \rangle $$

$$\tilde{\delta}_{F}(k)=\frac{1}{V} \int_{0}^{V} d v e^{-i k v} \delta_{F}(v)$$

Here, $$\langle \cdot \rangle$$ denotes the ensemble average, and $$k = 2\pi/v$$ is the
Fourier ‘frequency’ corresponding to $$v$$ and has dimensions of (s/km).




### Power Spectrum for several redshifts 


<img src="{{ site.url }}assets/images/flux_power_spectrum_all.png">

Now limiting the range in $$k$$


<img src="{{ site.url }}assets/images/flux_power_spectrum_all_zoom.png">


Compared to results from [Walther+2019](https://ui.adsabs.harvard.edu/abs/2019ApJ...872...13W/abstract)


<img src="{{ site.url }}assets/images/flux_power_spectrum_walther2019.png">
