---
layout: post
title:  "Quantum Turbulence"
date:   2020-01-07 17:10:24 -0800
categories: "projects"
permalink: /projects/quantum_turbulence/
---



[GitHub Repository:   https://github.com/bvillasen/qTurbulence](GitHub Repository: https://github.com/bvillasen/qTurbulence)

Using pyCUDA I developed software to solve the evolution of a Bose-Einstein condensate, which is a gas  cooled to temperatures near the absolute zero (-217 C), at this extreme temperature the gas becomes a super-fluid which means that the fluid has zero viscosity. The animation below shows the density of a simulated BEC on a rotating frame of reference, the tubular structures correspond to vortices where the gas is rotating and the density decreases. On a super-fluid the rotational energy of this vortices is not dissipated as in a regular fluid. 

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/quantum_turbulence.mp4" width="100%"  height="auto" controls preload> </video>
</div>

The animation above is a real-time volumetric render of the simulation, this means that the software that I developed is using the  GPU to solve the physics equations that govern the dynamics of a quantum fluid and simultaneously the GPU is running a ray-tracing algorithm to generate a 3D render of the simulated volume.   

From the data obtained from simulations I studied the properties of the turbulent motion of the gas and compared to known properties of turbulence in regular fluids, in particular I showed that the energy power spectrum on the quantum fluid scales as the well known Kolmogorov relation for turbulence in viscous fluids. This work resulted in the following publication where we propose a mechanism for developing a turbulent flow in a Bose-Einstein Condensate:

[**B. Villaseñor**, R. Zamora-Zamora, D. Bernal, and V. Romero-Rochín, ”*Quantum turbulence by
vortex stirring in a spinor Bose-Einstein condensate*”, 2014, Phys. Rev. A 89, 033611.](https://ui.adsabs.harvard.edu/abs/2014PhRvA..89c3611V/abstract)
