---
layout: post
title:  "HM12 Cooling Tables"
date:   2019-12-01 17:10:24 -0800
categories: cholla grackle
---

## HM12 Ionization Rates

Grackle takes the photoionization rates as a function of redshift for the different chemical species. 

<img src="{{ site.url }}assets/images/hm12_ionization_rates.png"> 


## Grackle Cooling Tables

Additionally grackle takes in 3-dimensional tables for cooling and heating rates and mean-molecular-weight as a function of H-density, temperature and redshift. Here is a comparison of the tables included with Grackle for the HM12 UV background (first column) and the tables that I generate using Cloudy (second column), the third column shows the fractional difference. 


### Tables for Primordial Composition

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/cooling_tables_primordial.mp4" width="100%"  height="auto" controls preload> </video>
</div>

### Tables for Metals

The cooling/heating rates for the metal component are passed as separate tables:

```
To calculate the cooling and heating contribution from metals, we run each of the above models twice, once with the full complement of elements and once with only H and He. For every point in each version of the model, we extract all cooling/heating components contributing at least $$10^{−10}$$ of the total rate. We then
remove all components that appear in both the full and H/He models, leaving only the contributions of the metals. All of the data are organized in HDF5 files. The structure and discoverability of HDF5 files allow the data to be easily used for other applications. 
```

## Simulation Comparison 

Here is the power spectrum of the gas and neutral Hydrogen for a simulation that used the cloudy tables for primordial cooling/heating compared to the same simulation using the Grackle tables. Differences are due to the different cooling/heating rates from the cloudy results.


<img src="{{ site.url }}assets/images/ps_256_cool_uv_cloudy_primordial.png"> 

