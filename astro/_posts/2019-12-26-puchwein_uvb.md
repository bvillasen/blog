---
layout: post
title:  "Plan for Summit Simulations"
date:   2019-12-27 17:10:24 -0800
categories: cholla summit
---

## Simulations

The will be three simulations, first a Dark Matter Only simulation followed by two Hydrodynamical simulations, one using the HM12_Cloudy table for the UVB and the other for the Puchwein18_Cloudy table.

## Parameters

The simulations will consist of 2048$$^3$$ cells/particles on a 50Mpc/h box.

The cosmological parameters, [Plank 2018](https://arxiv.org/pdf/1807.06209.pdf):

$$H_0 = 67.66$$ \\
$$\Omega_\Lambda = 0.6889$$ \\
$$\Omega_m = 0.3111$$ \\
$$\Omega_b = 0.0497$$ \\
$$\sigma_8 = 0.8102$$ \\
$$n_s = 0.9665$$

## The Outputs

Redshift Range: [ 100, 16 ]   20 outputs ( uniform in scale factor ) \\
Redshift Range: [ 16,  10 ]   20 outputs ( uniform in scale factor ) \\
Redshift Range: [ 10,  7  ]   30 outputs ( uniform in scale factor ) \\
Redshift Range: [ 7,   5  ]   30 outputs ( uniform in scale factor ) \\ 
Redshift Range: [ 5,   3  ]   30 outputs ( uniform in scale factor ) \\
Redshift Range: [ 3,   2  ]   30 outputs ( uniform in scale factor )

### Fields to save:

**DM**: Density

**Gas**: Density, HI_density, Temperature

Space per Field per Snapshot: 69 GB 

Space for DM simulation: 10.1 TB (160 Snapshots)

Space for Hydro simulation: 43.9 TB (160 Snapshots)

Snapshots could be saved in single precision cutting the required space by half. ??


## The Plan

First run the DM simulation and measure the power spectrum, if everything looks fine then run the first Hydro simulation for the HM12 UVB and measure the Power Spectrum and gas properties. Finally if the HM12 simulation was successful, run the Puchwein18 simulation.

The simulations will run on 512 GPUs ( 256$$^3$$ cells/particles per GPU ), requiring 86 nodes. For this number of nodes the maximum wall-time allowed is 6 hrs, this means that simulations will have to be restarted every 6 hrs.

My estimate for the run time of each Hydro simulation is about 30hrs and about 12hrs for the DM simulation, this will be about 2600 node-hr for each hydro simulation and 1000 node-hr for the DM simulation. Currently we have 13500 node-hr on our DD allocation so we should be fine for this estimate. 


