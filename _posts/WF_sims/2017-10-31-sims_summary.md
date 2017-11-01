---
layout: post
title:  "WFIRST: Simulations summary"
date:   2017-10-31 17:10:24 -0800
categories: cosmology wfirst
---

**SIMULATIONS PARAMETERS:**

Box size:  115 Mpc/h

Simulations Details:


| Num Particles | Particle Mass [M_sun/h] |  Softening Length [kpc/h] |
| ------------- | ----------------------- | ------------------------- |
|        1      |              1e4        |               36          |
{:.mbtablestyle}

  * 512:  4.9 kpc/h

  * 1024:  2.4 kpc/h

  * 2048:  1.2 kpc/h





Cosmology from Plank (2016)[Here](https://arxiv.org/abs/1502.01589)


---------------------------------------------------

Cosmology:

  * Omega_m   = 0.3089

  * Omega_L   = 0.6911

  * Omega_b   = 0.0486

  * H0        = 67.74

  * sigma_8   = 0.8159

  * nspec     = 0.967

  * transfer  = eisenstein

--------------------------------------------------

Initial Conditions:

  * Z = 100

  * Power spectrum from Eisenstein & Hu transfer function





Mass function at z=0 using ROCKSTAR halo catalogs for halo masses:


<img src="{{ site.url }}assets/images/massFunc_all_Warren.png">


Density projection using Brant's code (image-snapshot):


<img src="{{ site.url }}assets/images/density_512.png">


**UPDATE**

File with data for plotting mass functions from above [Here](https://github.com/bvillasen/blog/blob/master/assets/files/mass_funtion.dat)

Script for plotting mass functions from data file [Here](https://github.com/bvillasen/blog/blob/master/assets/files/plot_mass_function_1.py)


Data file: density projection [Here](https://github.com/bvillasen/blog/blob/master/assets/files/image.056.dat)

Data file: potential [Here](https://github.com/bvillasen/blog/blob/master/assets/files/image.pot.056.dat)
