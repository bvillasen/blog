---
layout: post
title: "Transmitted Flux Calculation "
date:   2020-04-23 19:10:24 -0800
categorines: dm cholla
---

<img src="{{ site.url }}assets/images/transmited_flux_pchw18.png"> 

**Most equations were taken from this paper:  [Lukic et al. 2016](https://arxiv.org/abs/1406.6361)**


The optical depth $$\tau$$ for Ly$$\alpha$$ scattering is given by:

$$\tau_{\nu}=\int n_{\mathrm{HI}} \sigma_{\nu} dr$$
 
 where $$\nu$$ is the frequency, $$n_{\mathrm{HI}}$$ is the number density of neutral hydrogen, $$\sigma_{\nu}$$ is the cross section of the interaction and $$dr$$ is the proper path element. Assuming a Doppler line profile, the optical depth is given by:
 
 
$$\tau_{\nu}=\frac{\pi e^{2}}{m_{e} c} f_{12} \int \frac{n_{\mathrm{HI}}}{\Delta \nu_{\mathrm{D}}} \frac{\exp \left[-\left(\frac{\nu-\nu_{0}}{\Delta \nu_{\mathrm{D}}}\right)^{2}\right]}{\sqrt{\pi}} d r $$

where $$\Delta \nu_{\mathrm{D}}=(b/c)\nu_0$$ is the Doppler width with the Doppler parameter due to thermal motions $$b=\sqrt{2k_bT/m_H}$$, and $$f_{12}$$ is the is the upward oscillator strength of the Ly$$\alpha$$ resonance transition of frequency $$\nu_0$$.

*In the Optical depth equation they define $$\tau_{\nu}$$ as an integral over $$\nu$$ which I think is misused notation, I think that equation defines the optical depth at the frequency $$\nu_{\mathrm{obs}}$$ which corresponds to the frequency in the frame of the observer that maps to the Ly$$\alpha$$ frequency $$\nu_0$$ when converted to the frame of the absorber.*


Not lets think of about an specific absorber that is moving with velocity $$u_0$$, if we set ourselves on the frame of the absorber, then we will see that our neighboring  gas elements are are moving with respect to us with velocity $$\Delta u$$( that depends on the distance to the neighbor, ignoring peculiar velocities ), since our neighbor is moving with respect to us then due to Doppler effect the frequency in which our neighbor will absorb is shifted with respect to our frequency of a absorption (which corresponds to $$\nu_0$$ ).  In the frame of the absober, the frequency of absorption of our neighbor is given by Doppler effect:

$$\nu=\nu_{0}\left(1-\frac{\Delta u}{c}\right)$$


If we make a variable change from frequency to velocity in the optical depth equation and using the expansion of the universe to transform $$dr$$ to $$du$$ by $$du = H dr$$, we obtain:

$$\tau=\frac{\pi e^{2}}{m_{e}  \nu_0 H} f_{12} \int \frac{n_{\mathrm{HI}}}{b} \frac{\exp \left[-\left(\frac{\Delta u}{b}\right)^{2}\right]}{\sqrt{\pi}} d u $$

where $$\Delta u = u-u_{0}$$ is the relative velocity to the absorber. This can be rewritten as:

$$\tau=\frac{\pi e^{2} \lambda_0}{m_{e}  c H} \frac{f_{12}}{\sqrt{\pi}} \int \frac{n_{\mathrm{HI}}}{b} \exp \left[-\left(\frac{u-u_{0}}{b}\right)^{2}\right] d u $$

This will give the optical depth at the velocity coordinate of the absorber $$u_0$$.
 
  