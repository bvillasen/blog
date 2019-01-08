---
layout: post
title:  "Phy9 Project: Analysis of Dark Matter Simulations"
date:   2019-01-07 17:10:24 -0800
categories: dark-matter project
---

## Dark Matter

Dark matter is a kind of matter that scientists believe to exist and accounts for about 85% of all the mass in the universe. Ordinary matter is the kind of matter that forms stars, planets, humans, hydrogen, protons, electrons, etc. Ordinary matter is called baryonic matter. Dark matter differs from baryonic matter in that dark matter doesn't interact with light, this means that dark matter doesn't emit any light and it is completely transparent, for this reason we can't "see" dark matter in the regular sense.

The way we "observe" dark matter and infer its existence is by measuring its gravitational influence on stars, galaxies and light itself. In this sense, dark matter is a source of gravity that we aren't able to see and so far we still can't detect, but we see its gravitational pull on other massive objects like stars and galaxies.

The actual evidence points to our Universe having a lot more dark matter than baryonic matter, as a result the gravitational pull from dark matter is much more dominant. This have very important effects, because of its gravitational attraction dark matter clump together forming very massive clumps, this clumps are called **dark matter halos**, at the same time the gravity from the dark matter pulls the baryonic matter in to the center of the halos, in these regions the gravitational pull is strong enough to give rise to very high densities of baryonic matter, densities become so high that hydrogen atoms fuse together emitting a lot of energy in form of light, this results in the formation of a star. In the interior of dark matter halos millions of stars are formed and all these stars form a galaxy.

Another important role of dark matter is on its influence in the expansion of the universe, due its gravitational attraction the amount of dark matter in the Universe is directly linked to the expansion of the Universe.


## Dark Matter Simulations

In order to study how dark matter affects the formation of galaxies, scientists use supercomputers to run **Dark Matter Cosmological Simulations** in which the dynamical evolution of the dark matter in a very large volume of the Universe ( thousands of galaxies ) is calculated, in other words, we calculate the movement of dark matter elements in response to their gravitational attraction resulting in the time evolution of the dark matter density field.

The animation below shows the time 3D evolution of the dark matter in a cosmological simulation. Shown in the animation is the dark matter density, the regions of bright color are regions were the density is high and dark regions is were the density is low. As you can see in the animation the simulation starts with the dark matter distributed almost uniformly in all the box except for some inhomogeneities and as time advances the inhomogeneities where the density is slightly higher become brighter and brighter, this means that they become more dense (more massive) due their gravitational attraction. After the first half of the animation you can see that all the volume is populated by bright clumps, these are the dark matter halos and in the inner parts of those clumps is where galaxies form.

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/cosmo_10.mp4" height="600" width="600" controls preload> </video>
</div>

## Dark Matter Halos

So now we know that regions where the dark matter density is high ( higher to a certain threshold ) are called halos. In the figure below you can see a projection of the dark matter density that corresponds to a small part of the volume shown in the animation above ( somewhat like a zoom-in to a small region of the entire box ), again the bright yellowish regions are high density regions ( halos ) and the dark purplish regions are low density regions. On the right panel you can see the same region but here the halos are highlighted with white circles, the radius of the circle is proportional to the mass of the halo.

<img src="{{ site.url }}assets/images/density_halos.png">



## The Project

The goal of this project will be to identify the dark matter halos in a cosmological simulation and then do some analysis on the evolution and formation history  as well statistical analysis of all the halos in the simulation.


For the project:

<ul>

<li> We will understand fundamental concepts of cosmology and galaxy formation. </li>

<li> We will learn the basics of Phyton programming and its application to scientific programming. </li>

<li> We will learn how to read and write data files, including formats for efficient storage for large data files (HDF5). </li>

<li> Using the mass and positions of the Dark Matter particles we will compute the density field of the Dark Matter and plot the evolution of the density field as a function of time. This will result in a nice animation. </li>

<li> We will use ROCKSTAR to locate the dark matter halos resulting on halo catalogs of the simulation. </li>

<li> Depending on the progress and the time available we will perform some halo analysis, beginning with the halo mass function and then analyzing the halo merger trees to study the halos formation histories. </li>


</ul>
