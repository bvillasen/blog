---
layout: post
title: "Transmitted Flux Calculation "
date:   2020-04-23 19:10:24 -0800
categorines: dm cholla
---

<img src="{{ site.url }}assets/images/transmited_flux_pchw18.png"> 

Most equations were taken from this paper:  [Lukic 2016](https://arxiv.org/abs/1406.6361)


The optical depth $$\tau$$ for Ly$$alpha$$ scattering is given by:

$$\tau_{\nu}=\int n_{\mathrm{HI}} \sigma_{\nu} dr$$
 
 where $$\nu$$ is the frequency, $$n_{\mathrm{HI}}$$ is the number density of neutral hydrogen, $$\sigma_{\nu}$$ is the cross section of the interaction and $$dr$$ is the proper path element. Assuming a Doppler line profile, the optical depth is given by:
 
 
$$\tau_{\nu}=\frac{\pi e^{2}}{m_{e} c} f_{12} \int \frac{n_{\mathrm{HI}}}{\Delta \nu_{\mathrm{D}}} \frac{\exp \left[-\left(\frac{\nu-\nu_{0}}{\Delta \nu_{\mathrm{D}}}\right)^{2}\right]}{\sqrt{\pi}} d r $$

where $$\Delta \nu_{\mathrm{D}}=(b/c)\nu_0$$ is the Doppler width with the Doppler parameter due tu thermal motions $$b=\sqrt{2k_bT/m_H}$$, and $$f_12$$ is the is the upward oscillator strength of the Ly$$\alpha$$ resonance transition of frequency $$\nu_0$$.

*In the Optical depth equation they define $$\tau_{\nu}$$ as an integral over $$\nu$$ which I think is misused notation, I think that equation defines the optical depth at the frequency $$\nu_{\mathrm{obs}}$$ which corresponds to the frequency in the frame of the absorber that when corresponds to the Ly$$\alpha$$ frequency $$\nu_0$$.*  