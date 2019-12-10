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


> To calculate the cooling and heating contribution from metals, we run each of the above models twice, once with the full complement of elements and once with only H and He. For every point in each version of the model, we extract all cooling/heating components contributing at least $$10^{−10}$$ of the total rate. We then remove all components that appear in both the full and H/He models, leaving only the contributions of the metals. All of the data are organized in HDF5 files. The structure and discoverability of HDF5 files allow the data to be easily used for other applications. 

To compute the cooling and heating tables for metals, I compute cooling and heating rates for Solar composition and subtract the cooling and heating rates from the previously computed *H and He only* cooling/heating rates.  

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/cooling_tables_metals.mp4" width="100%"  height="auto" controls preload> </video>
</div>


## Simulation Comparison 

Here is the power spectrum of the gas and neutral Hydrogen for a simulation that used the cloudy tables for primordial cooling/heating compared to the same simulation using the Grackle tables. Differences are due to the different cooling/heating rates from the cloudy results.

### Changing Primordial Tables
<img src="{{ site.url }}assets/images/ps_256_cool_uv_cloudy_primordial.png"> 



### Changing Primordial Tables and Metals Tables

<img src="{{ site.url }}assets/images/ps_256_cool_uv_cloudy_metals_on.png"> 


## Cloudy Parameter Example For Primordial Composition

```
                                                          Cloudy 17.01
                                                        www.nublado.org

                      **************************************17Jun01**************************************
                      *                                                                                 *
                      * stop zone 1                                                                     *
                      * iterate to convergence                                                          *
                      * hden -10.0                                                                      *
                      * constant temperature T = 1.122018e+01 linear                                    *
                      * table HM12 redshift 0.0                                                         *
                      * #<<  HM12 GALAXY model    1 read.         z =          0.00                 >>> *
                      * #<< FINAL:       z =          0.00                                          >>> *
                      * element Lithium abundance -30                                                   *
                      * element Beryllium abundance -30                                                 *
                      * element Boron abundance -30                                                     *
                      * element Carbon abundance -30                                                    *
                      * element Nitrogen abundance -30                                                  *
                      * element Oxygen abundance -30                                                    *
                      * element Fluorine abundance -30                                                  *
                      * element Neon abundance -30                                                      *
                      * element Sodium abundance -30                                                    *
                      * element Magnesium abundance -30                                                 *
                      * element Aluminum abundance -30                                                  *
                      * element Silicon abundance -30                                                   *
                      * element Phosphorus abundance -30                                                *
                      * element Sulphur abundance -30                                                   *
                      * element Chlorine abundance -30                                                  *
                      * element Argon abundance -30                                                     *
                      * element Potassium abundance -30                                                 *
                      * element Calcium abundance -30                                                   *
                      * element Scandium abundance -30                                                  *
                      * element Titanium abundance -30                                                  *
                      * element Vanadium abundance -30                                                  *
                      * element Chromium abundance -30                                                  *
                      * element Manganese abundance -30                                                 *
                      * element Iron abundance -30                                                      *
                      * element Cobalt abundance -30                                                    *
                      * element Nickel abundance -30                                                    *
                      * element Copper abundance -30                                                    *
                      * element Zinc abundance -30                                                      *
                      * element Lithium off                                                             *
                      * element Beryllium off                                                           *
                      * element Boron off                                                               *
                      * element Carbon off                                                              *
                      * element Nitrogen off                                                            *
                      * element Oxygen off                                                              *
                      * element Fluorine off                                                            *
                      * element Neon off                                                                *
                      * element Sodium off                                                              *
                      * element Magnesium off                                                           *
                      * element Aluminum off                                                            *
                      * element Silicon off                                                             *
                      * element Phosphorus off                                                          *
                      * element Sulphur off                                                             *
                      * element Chlorine off                                                            *
                      * element Argon off                                                               *
                      * element Potassium off                                                           *
                      * element Calcium off                                                             *
                      * element Scandium off                                                            *
                      * element Titanium off                                                            *
                      * element Vanadium off                                                            *
                      * element Chromium off                                                            *
                      * element Manganese off                                                           *
                      * element Iron off                                                                *
                      * element Cobalt off                                                              *
                      * element Nickel off                                                              *
                      * element Copper off                                                              *
                      * element Zinc off                                                                *
                      * metals 1e-30                                                                    *
                      * no molecules                                                                    *
                      * punch last cooling file = "/home/bruno/Desktop/Dropbox/Developer/cooling_tools/cloudy_tools/primordial_uv/run_0//cooling_run_run0.cooling.temp"*
                      * punch last heating file = "/home/bruno/Desktop/Dropbox/Developer/cooling_tools/cloudy_tools/primordial_uv/run_0//cooling_run_run0.heating.temp"*
                      * punch last abundance file = "/home/bruno/Desktop/Dropbox/Developer/cooling_tools/cloudy_tools/primordial_uv/run_0//cooling_run_run0.abundance.temp"*
                      * punch last ionization means file = "/home/bruno/Desktop/Dropbox/Developer/cooling_tools/cloudy_tools/primordial_uv/run_0//cooling_run_run0.ionization.temp"*
                      * punch last physical conditions file = "/home/bruno/Desktop/Dropbox/Developer/cooling_tools/cloudy_tools/primordial_uv/run_0//cooling_run_run0.physical.temp"*
```

