---
layout: post
title:  "Cholla_PM: UVB Comparison"
date:   2019-12-26 17:10:24 -0800
categories: puchwein uv
---

Here is the comparison for Cholla simulations using different UV Backgrounds:

The simulations are 256$$^3$$ cells/particles on a 50 Mpc/h box.

The cosmological parameters, [Plank 2018](https://arxiv.org/pdf/1807.06209.pdf):

$$H_0 = 67.66$$ \\
$$\Omega_\Lambda = 0.6889$$ \\
$$\Omega_m = 0.3111$$ \\
$$\Omega_b = 0.0497$$ \\
$$\sigma_8 = 0.8102$$ \\
$$n_s = 0.9665$$

### UVB Tables:

**HM12_Grackle**: Original table for HM12 model, included with Grackle.

**HM12_Cloudy**: Recomputed table for HM12 model, computed with Cloudy C17.

**Puchwein18_Cloudy**: Table for Puchwein18 model, computed with Cloudy C17.

## Phase Diagram

The phase diagram as a function of redshift for the three cases:

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_uvb_comparison.mp4" width="100%"  height="auto" controls preload> </video>
</div>

## Average Temperature

The **mass weighted average temperature** as a function of redshift for the three cases:


<img src="{{ site.url }}assets/images/avrg_temperature_uvb_comparison.png"> 


## Ionization Fraction

The ionization fractions for H and He separately as a function of redshift for the three cases:


<img src="{{ site.url }}assets/images/ionization_fraction_uvb_comparison.png"> 

