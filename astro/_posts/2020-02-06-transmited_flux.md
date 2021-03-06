---
layout: post
title:  "Transmitted Flux"
date:   2020-02-06 17:10:24 -0800
categories: gas cholla
---

The optical depth $$\tau$$ for Ly$$\alpha$$ photon scattering is

$$\tau_{v}=\int n_{\mathrm{HI}} \sigma_{v} d r$$

where $$v$$ is the frequency, $$n_{\mathrm{HI}}$$ is the number density of neutral hydrogen,
$$\sigma_{v}$$ is the cross section of the interaction, and $$dr$$ is the proper path
length element. Assuming a Doppler line profile, the resulting optical depth is

$$ \tau_{v}=\frac{\pi e^{2}}{m_{e} c} f_{12} \int \frac{n_{\mathrm{HI}}}{\Delta v_{D}} \frac{\exp \left[-\left(\frac{v-v_{0}}{\Delta v_{D}}\right)^{2}\right]}{\sqrt{\pi}} d r ,$$

where $$\Delta v_{D}= (b/c)v_{0} $$ is the Doppler width with the Doppler parameter
 $$b = b_\mathrm{thermal} = \sqrt{2k_\mathrm{B} T / m_\mathrm{H}} $$, and $$f_{12}$$ is the upward oscillator strength of the Ly$$\alpha$$ resonance transition of frequency $$v_0$$.
 
The path length in the sight line integration is then $$dr = a dx =  dv/H$$, where $$r$$ is the proper distance, $$x$$ is the comoving distance, $$v$$ is the
Hubble flow velocity, and $$H$$ is the Hubble expansion rate at that redshift. In
velocity coordinates, the optical depth is

$$\tau_{v}=\frac{\pi e^{2} f_{12} \lambda_{0}}{m_{e} c H} \int n_{\mathrm{HI}} \frac{1}{\sqrt{\pi} b} \exp \left[-\left(\frac{v-v_{0}}{b}\right)^{2}\right] d v$$

<!-- 
Although the gas data is fixed at the grid resolution, we can choose an arbitrary spectral resolution $$N_\mathrm{pix}$$ along the LOS. We also take the gas values as
constant across each cell. With $$i$$ as the cell index, and $$j$$ as the pixel index,
the discretized version of the optical depth is -->


Using the following numerical values:


$$ f_{12} = 0.416 $$,   $$ \lambda_{\mathrm{Lya}} = 1.21567  \times 10^{-5}   \mathrm{cm} $$ 



### Single Absorber


<img src="{{ site.url }}assets/images/single_absorber.png">


### Simulated spectra


<img src="{{ site.url }}assets/images/transmited_flux_hm12_147.png">

 
<!-- <img src="{{ site.url }}assets/images/transmited_flux_130.png"> -->
