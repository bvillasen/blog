---
layout: post
title: "Comparison to Ewald Simulation (Complete)"
date:   2020-05-7 10:10:24 -0800
categorines: dm cholla
---

## Cholla Simulations:

Box Size = 50 Mpc/h
Numerical Size:  Uniform Grid $$2048^3$$ cells,  and $$2048^3$$ dark matter particles


## SPH Simulations:

Box Size = 10 Mpc/h
Numerical Size:  $$512^3$$ gas particles,  and $$512^3$$ dark matter particles


### Interpolation to the Grid


To interpolate the particle data obto the grid, I use the kernel function used in Gadget2. The kernel as a function of distance $$r$$ and smoothing length $$h$$ is given by:

$$W(r, h)=\frac{8}{\pi h^{3}}\left\{\begin{array}{ll}
1-6\left(\frac{r}{h}\right)^{2}+6\left(\frac{r}{h}\right)^{3}, & 0 \leqslant \frac{r}{h} \leqslant \frac{1}{2} \\
2\left(1-\frac{r}{h}\right)^{3}, & \frac{1}{2}<\frac{r}{h} \leqslant 1 \\
0, & \frac{r}{h}>1
\end{array}\right.$$ 


I interpolate the particle data onto a grid ( $$512^3$$ cells ). For the interpolation I used two different methods:

**Gather 64:** Measure the distance that encloses 64 neighboring particles and use that distance as the smoothing length when computing the kernel weights.

**Scatter:** Use the smoothing lengths of the neighboring particles when computing the kernel weights. 



### Phase Diagram Comparison

After interpolating the particle data into a uniform grid, I measure the volume weighted temperature-density distribution for the two snapshots and compare to the ones from the Cholla Simulation:

#### z = 5
<img src="{{ site.url }}assets/images/phase_diagram_sph_grid_z5.png"> 


#### z= 5.5
<img src="{{ site.url }}assets/images/phase_diagram_sph_grid_z5.5.png">

**Both simulations have almost identical power law temperature-density relations.**


### Density Distribution Comparison

Next I measured the **gas density** and the **neutral hydrogen density** distributions on the Grid-SPH data and compared to the ones in the Cholla simulation ( only for z=5):

**Left Panel:** Gas density distribution.

**Center Panel:** HI density distribution.

**Right Panel:** Neutral fraction distribution.


<img src="{{ site.url }}assets/images/density_distribution.png"> 


**The density distributions for both simulations are surprisingly similar.** 


### Transmitted Flux Calculation:


The following figure shows the Optical Depth $$\tau$$  and transmitted flux $$F$$  for a single skewer from the Cholla simulation at z=5:

<img src="{{ site.url }}assets/images/transmited_flux_pchw18_z=5.png"> 

The optical depth $$\tau$$ is computed from the integral of a Gaussian profile for each absorber, this is given by:



$$\tau_{j} = \frac{\pi e^{2} \lambda_0 f_{12}}{m_{e}  c H} \sum_i  n_{\mathrm{HI},i} \frac{ erf(y_{j+1/2,i})  - erf(y_{j-1/2,i}) }{2} $$

$$y_{j+1/2,i} = ( v_{j+1/2} - v_{\mathrm{H},i} - v_{\mathrm{LOS},i} )/b_i$$

$$y_{j-1/2,i} = ( v_{j-1/2} - v_{\mathrm{H},i} - v_{\mathrm{LOS},i} )/b_i$$


**View appendix at the end for a discussion about using a Voigt profile instead of a Gaussian profile**


