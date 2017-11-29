---
layout: post
title:  "PM: Adding cosmology"
date:   2017-10-24 17:10:24 -0800
categories: cholla
---


**Mostly taken from Andrey's PM notes**

In proper coordinates, gravitational potential and equations of motion for particles:

$$\nabla^2 \Phi \, = 4 \pi G \rho_{tot} - \Lambda $$

$$\frac{d\textbf{r}}{dt} \, = \,\textbf{u}$$

$$\frac{d\textbf{u}}{dt} \, = \, - \nabla \Phi$$  

time and spatial derivatives are also with respect to proper coordinates.


Now we change to comoving variables and make them dimensionless:


$$ \tilde{\textbf{x}} \, \equiv  \, a^{-1} \frac{\textbf{r}}{r_0}, \,\,\, \tilde{\textbf{p}} \, \equiv  \, a \frac{\textbf{v}}{v_0}, \,\,\, \tilde{\phi} \, \equiv  \, \frac{\phi}{\phi_0},
 \,\,\,  \tilde{\rho} \, \equiv  \, a^3 \frac{\rho}{\rho_0},$$

where $$\tilde{\textbf{x}}$$, $$\textbf{v}  \, = \, \textbf{u} - H\textbf{r} \, = \, a\mathbf{ \dot{x} }$$  is the peculiar velocity and $$\phi$$ is the peculiar potential defined as (Peebles 1980)

$$ \phi \, = \, \Phi +  \frac{H_0^2}{2} \bigg( \Omega_\Lambda - \frac{1}{2}a^{-3} \Omega_m \bigg) r^2 ,$$

where

$$ \Omega_m  =  \frac{8 \pi G \rho_0}{3H_0^2} ; \, \, \Omega_\Lambda  =  \frac{\Lambda}{3H_0^2}  .$$

To make the variables dimensionless we define:

$$ r_0 \, \equiv \, \frac{L_{box}}{N_g}; \, \, N_g^3 \, = \, \text{total number of grid cells}, $$

$$ t_0 \, \equiv \, H_0^{-1} ,$$

$$ v_0 \, \equiv \, \frac{r_0}{t_0} ,$$

$$ \rho_0 \, \equiv \, \frac{3 H_0^2}{8 \pi G} \Omega_m ,$$

$$ \phi_0 \, \equiv \, \frac{r_0^2}{t_0^2} \, = \, v_0^2 ,$$

Now using the scale factor as the time variable, the Poisson equation and the equations of motion are:

$$\nabla^2 \phi  = 4 \pi G \Omega_m \rho_{crit} \frac{\delta}{a}, \;\;\; \delta  =  \frac{\rho - \bar{\rho}}{\bar{\rho}}  $$


$$\frac{d\textbf{p}}{da}  = - \frac{\nabla \phi}{\dot{a}}, \;\;\; \frac{d\textbf{x}}{da}  =  \frac{d\textbf{p}}{\dot{a}a^2},$$

here $$\delta$$ is the overdensity in comoving coordinates and $$\dot{a}$$ is given by:

$$\dot{a} = H_0 a^{-1/2} \sqrt{ \Omega_m + a\Omega_k + a^3\Omega_\Lambda  } ; \;\;\; \Omega_m + \Omega_k + \Omega_\Lambda = 1 $$  

In dimensionless variables these equations become:

$$\tilde{\nabla}^2 \tilde{\phi}  = \frac{3}{2}  \frac{\Omega_m}{a} \tilde{\delta},  $$


$$\frac{d\mathbf{\tilde{p}}}{da}  = - f(a)\tilde{\nabla} \tilde{\phi}, \;\;\; \frac{d\mathbf{\tilde{x}}}{da}  = f(a) \frac{d\mathbf{\tilde{p}}}{a^2},$$

where $$\tilde{\delta} = \tilde{\rho} - 1$$ and

$$ f(a) \equiv H_0/\dot{a} = [ a^{-1} ( \Omega_m + a\Omega_k + a^3\Omega_\Lambda ) ]^{-1/2} $$



To do the time evolution of the DM particles, these last equations are used in the three main steps of the PM code:

  * Solve the Poisson equation using the density field estimated with the current particle positions.

  * Advance the momentum of the particles using the new potential.

  * Update particle positions using the new momenta  ( Leap-Frog scheme ).
