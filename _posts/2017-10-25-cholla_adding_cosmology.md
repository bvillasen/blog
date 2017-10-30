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

$$ \phi \, = \, \Phi +  \frac{H_0^2}{2} \big( \Omega_\Lambda - \frac{1}{2}a^{-3} \Omega_m \big) r^2 ,$$
