---
layout: post
title:  "Primordial Cooling"
date:   2019-12-09 17:10:24 -0800
categories: cholla grackle
---

From [Katz et al. 1995](https://arxiv.org/abs/astro-ph/9509107) I get the cooling rates gas of primordial composition and no incident radiation. Here are the cooling rates for the different processes:


The composition dor the gas is: $$n_{H} = 1$$  $$n_{He} = 0.1$$  



<img src="{{ site.url }}assets/images/primordial_cooling.png"> 


Here is the comparison of the cooling rates from Katz+1995 the results from Cloudy and Grackle.

I tried using the older  Cloudy version c13 (instead of c17) and the cooling rates match the ones in the Grackle file, my guess is that Grackle used cloudy c13 to compute their tables. 

<img src="{{ site.url }}assets/images/primordial_cooling_comparison_convergence_cloudy13.png"> 

My guess is that the differences in the Cooling/Heating rates for the HM12 background computed before are due to the different Cloudy versions and not due to the methodology employed to compute the tables.

I tried to compute the cooling rates for the HM12 background using Cloudy C13 to make sure that I got the same thing that Grackle, but the HM12 spectrum is not included in that version of Cloudy and it seems like the format of the tables for the  radiation spectrum is different than the ones included in Cloudy c17, right now it seems like adding the HM12 tables to cloudy c13 just to check that I get the same answer will take some time and it will be kind of useless.

My suggestion is to assume that the differences on the Grackle and Cloudy17 tables for HM12 are only due to the Cloudy version used. Then use Cloudy17 to recompute the tables for HM12 ( which I already did) and for the Puchwein18 background. Finally run the simulations using the two new tables. 