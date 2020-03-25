---
layout: post
title: "Flux Power Spectrum Revisited"
date:   2020-03-23 17:10:24 -0800
categories: dm cholla
---


Originally when computing the flux fluctuations for a line of sight, I was taking $$\langle F \rangle$$ as the flux average over the line of sight. I think that the correct way of doing it is to normalize by the transmitted flux averaged over all the line of sights for a given redshift.

Additionally I was making a mistake when selecting the snapshot index that corresponded to a given redshift and I was choosing a snapshot with a slightly higher redshift.

After correcting this two mistakes the new normalization of the flux fluctuations changes the power spectrum and now the Puchwein model doesn't match the data as well as it did before.

Here are the new measurements:

**Small $$k$$:**

<img src="{{ site.url }}assets/images/flux_power_spectrum_all_data_z2.png">


<img src="{{ site.url }}assets/images/flux_power_spectrum_all_data_z5.png">



**Large $$k$$:**

<img src="{{ site.url }}assets/images/flux_power_spectrum_all_data_black_z2_boss.png">


<img src="{{ site.url }}assets/images/flux_power_spectrum_all_data_black_z4_boss.png">
  