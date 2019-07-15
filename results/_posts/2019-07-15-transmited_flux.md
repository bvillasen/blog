---
layout: post
title:  "Simulated Lya Spectra"
date:   2019-07-15 17:10:24 
categories: "results"
---


## Ly-$$\alpha$$ Forest from Cholla Simulations

### Single Absorber 

The opacity $$\tau_{\nu}$$ for cold interstellar gas can be approximated by:

$$
\tau_{\nu}=\frac{\pi e^{2}}{m_{e} c} f_{\ell u} N_{\ell} \phi_{\nu}
$$


The line profile function $$\phi_{\nu}$$ is generally a Voigt profile, meaning that it has a Gaussian
core and Lorentzian damping wings. If we focus on the  Gaussian core, we can approximate
$$\phi_{\nu}$$ by a pure Gaussian, 

$$
\phi_{\nu}=\frac{1}{\sqrt{\pi} b} e^{-\left(1-\nu / \nu_{0}\right)^{2} /(b / c)^{2}} ; \quad b \equiv \sqrt{2} \sigma_{v}
$$

where $$b$$ is the **Doppler broadening parameter**. This has a maximum value of $$1/\sqrt{\pi b}$$
at line center $$\nu=\nu_0$$ , so the (maximum) line center optical depth is:

$$
\tau_{0}=\sqrt{\pi} \frac{e^{2}}{m_{e} c} \frac{f_{\ell u} \lambda_{u \ell} N_{\ell}}{b}=0.758\left(\frac{N_{\ell}}{10^{13} \mathrm{cm}^{-2}}\right)\left(\frac{f_{\ell u}}{0.4162}\right)\left(\frac{\lambda_{u \ell}}{1215.7 \mathrm{A}}\right)\left(\frac{10 \mathrm{km} \mathrm{s}^{-1}}{b}\right)
$$

where **$$\lambda_{u \ell} = c/\nu_0$$** , and the normalization quantities are
those appropriate for the Lyman-$$\alpha$$ line of hydrogen. The optical depth in the
Gaussian part of the line profile is then

$$
\tau_{\nu}=\tau_{0} e^{-u^{2} / b^{2}}
$$

where **$$u=c(\nu_0 - \nu)/\nu $$** is the velocity shift required to produce a frequency shift **$$\nu$$**.