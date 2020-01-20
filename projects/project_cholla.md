---
layout: page
permalink: /projects/cholla/
---


### CHOLLA: Large Scale Cosmological Hydrodynamical Simulations on Multiple GPUs 

[GitHub Repository: https://github.com/bvillasen/cholla](https://github.com/bvillasen/cholla)


Originally Cholla was a hydrodynamics solver that runs in multiple GPUs. For my Ph.D. thesis I have extended Cholla to run cosmological simulations, I added several physics modules: \\
 - A distributed FFT based Poisson solver to  include the self-gravity of the fluid. \\
 - A Particle-Mesh scheme to solve the collisionless dynamics of the dark matter particles.\\
 - Integration with Grackle, an open source library to solve the chemical network and track the ionization states of Hydrogen and Helium on the simulation. Also include a uniform time-dependent UV background to account for the reionization of the universe.
 
 
 The animation bellow shows the evolution of the dark matter for a Cholla simulation, the initial conditions are mostly uniform except for tiny perturbations corresponding to the quantum perturbations of the early universe, as time progresses the regions where the density is slightly higher exerts a gravitational pull over the surrounding material causing the growth of large dark matter structures called halos shown in yellow in the animation, the regions connecting the halos form the cosmic web. Galaxies are formed in the inner parts of dark matter halos.        

 <div style="text-align: center">
 <video src="{{ site.url }}assets/videos/dm_50Mpc_3D.mp4" width="100%"  height="auto" controls preload> </video>
 </div>
 
 The image below shows several components of a cosmological hydrodynamical simulation, the first column corresponds to the dark matter density, the second column shows the gas density, the third column correspond to the neutral hydrogen density and finally the last column shows the temperature of the gas. The top row shows the results from a simulation evolved using a popular code called [Enzo](https://enzo-project.org/) and the bottom show shows the result from an analogous simulation that I ran using Cholla on 8 Nvidia P100 GPUs.
  
 <img src="{{ site.url }}assets/images/projection_deep_1.png">



Cholla uses MPI, CUDA and OpenMP to leverage the computing power of the largest computers in the world. I have used Cholla to run cosmological simulations in Summit (ORNL, number one in the top500) where I measured the performance of the code obtaining near perfect scaling when used in up to 16,000 GPUs. The image below shows a near perfect weak scaling when using Cholla on Summit. 


<img src="{{ site.url }}assets/images/weak_scaling.png">