---
layout: post
title:  "Simulation analysis"
date:   2017-08-15 17:10:24 -0800
categories: cosmology wfirst
---

**SIMULATIONS PARAMETERS:**

Box size:  115 Mpc/h


Cosmology from Plank (2016)[Here](https://arxiv.org/abs/1502.01589)


Initial Conditions:

  * Z = 100

  * Power spectrum from Eisenstein & Hu transfer function


Force Resolution:

  * 512:  4.9 kpc/h

  * 1024:  2.4 kpc/h

  * 2048:  1.2 kpc/h



Mass function at z=0 using ROCKSTAR halo catalogs for halo masses:


<img src="{{ site.url }}assets/images/massFunc_all_Warren.png">


Density projection using Brant's code (image-snapshot):


<img src="{{ site.url }}assets/images/density_512.png">


**UPDATE**

File with data for plotting mass functions from above [Here](https://github.com/bvillasen/blog/blob/master/assets/files/mass_funtion.dat)

Script for plotting mass functions from data file [Here](https://github.com/bvillasen/blog/blob/master/assets/files/plot_mass_function_1.py)


Data file: density projection [Here](https://github.com/bvillasen/blog/blob/master/assets/files/image.056.dat)

Data file: potential [Here](https://github.com/bvillasen/blog/blob/master/assets/files/image.pot.056.dat)
