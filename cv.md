---
layout: page_main
title: CV
permalink: /cv/
---

[**PDF Version HERE**]({{ site.url }}assets/files/CV_villasenor.pdf)

## Bruno Villasenor

Telephone: (+1) 831 212 3832\\
Email: bvillasen@gmail.com,  brvillas@ucsc.edu\\
GitHub: https://github.com/bvillasen

### Education

**University of California, Santa Cruz** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&emsp;&emsp;&ensp;&emsp;&emsp;&ensp; ( August 2016 - Expected Jun 2022 ) \\
Master of Science, Expected Ph.D. in Astronomy and Astrophysics                \\
Department of Astronomy and Astrophysics.  \\
Advisor:  Brant Robertson


**Universidad Nacional Autonoma de Mexico, UNAM** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  ( August 2010 - June 2016 ) \\
Bachelor of Science in Physics.                       Final Grade:  9.4 / 10    \\
Thesis:  “On the kinematics of the stellar component of satellite galaxies as tracer of their dark matter distribution”  
Advisor:  Vladimir Avila-Ress


### Technical Skills

**Basic Knowledge**   &emsp;&emsp;   &emsp;&emsp;&emsp;&emsp;  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; R, Matematica, Fortran \\
**Intermediate Knowledge** &emsp;&emsp;&emsp; Java, Matlab, HTML \\
**Advanced Knowledge**   &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   Python, C/C++, CUDA, MPI, OpenMP, Julia

### Work Experience

**Summer Intern at Fermilab**,  &emsp;&emsp;Fermi National Lab, &emsp;&emsp; Illinois, &emsp;&emsp;  Summer 2010 \\
Fellow at the Internship for Physics Majors at Fermi National Accelerator Laboratory. Developed software to analyze events from the Tevatron collider and  applied a new method to select Higgs Boson events from the WW decay, this algorithm was latter applied in the Higgs detection pipeline.\\
Advisor: Eric James.


**Summer Intern at Fermilab**, &emsp;&emsp;Fermi National Lab,&emsp;&emsp; Illinois,&emsp;&emsp; Summer 2011\\
Received a "come back" offer for further development of data analysis work done during the previous summer for the Higgs boson detection. Analyzed the Higgs Thrust from monte-carlo simulations and optimized the selection criteria for Higgs events from the Tevatron collider.\\
Advisor: Eric James & Sergo Jindariani

### Teaching Experience

**Teacher Assistant:** *Intro. to Scientific Computing*,  Astronomy Dept. UCSC. Winter 2016, Spring 2017 \\
**Teacher Assistant:** *Computational Physics, 7th semester*, UNAM. Semester: 2016-1.  \\
**Teacher Assistant:** *Electromagnetism I*, 4th semester, UNAM. Semester: 2012-2. \\
**Teacher Assistant:** *Scientific Computing Using GPU's*,  Advanced, UNAM. Semester: 2012-1. \\
**Teacher Assistant:** *Computation*,  1st semester, UNAM. Semesters: 2010-2, 2011-1, 2011-2, 2013-1.

### Mentoring Experience

**Python Bootcamp Instructor for the Lamat 2020 Participants**, UCSC, January 2020:\\
Participated as the instructor for the 2020 Python Bootcamp. A one week long intensive program where the participants of the 2020 Lamat summer program learned the basics of scientific programming using Python so that they will be prepared for conducting scientific research in astrophysics during the summer.       

**Graduate Student Instructor for Introduction to Research (ASTR 9)**,  UCSC, January 2019 - June 2019:\\
Mentored a team of four first year undergraduate students through an astronomy research project that I designed. We ran and analyzed a set of dark matter cosmological simulations, located the dark matter halos and studied their density profile.

### Honors and Awards


* **Excellence in Teaching**: UCSC Astronomy Department Award Recipient, 2017. 
* Second place at the III Mexican Olympiad of Astronomy, INAOE, Mexico, 2007. 
* Participant at the XXXVII International Physics Olympiad, Iran, 2007. 
* Participant at the XXXVI International Physics Olympiad, Singapore, 2006. 
* Silver medal at the X Ibero-American Physics Olympiad, Uruguay, 2005. 
* First place at the XVI Mexican Physics Olympiad, Merida, Mexico, 2005. 
* Second place at the XV Mexican Physics Olympiad, Zacatecas, Mexico, 2004. 

## Publications

[**B. Villaseñor**, R. Zamora-Zamora, D. Bernal, and V. Romero-Rochín, ”*Quantum turbulence by
vortex stirring in a spinor Bose-Einstein condensate*”, 2014, Phys. Rev. A 89, 033611.](https://ui.adsabs.harvard.edu/abs/2014PhRvA..89c3611V/abstract)

 
 
### Additional Education

* First Mexican AstroCosmoStatistics School, Guanajuato, Mexico, 2016
* Sixth Mexican Summer School of Nuclear Physics, ICN, UNAM, Mexico, 2010.
* Mexican delegate at the 2005 National Youth Science Camp, West Virginia, U.S. 2005.

#### &emsp;&emsp; Online Courses Taken:
 
* Algorithms and Data Structures, Microsoft. (EdX).
* Learn to Program in Java, Microsoft. (EdX).
* Object Oriented Programming in Java, Microsoft. (EdX).
* Designing a Technical Solution, Microsoft. (EdX).
* Algorithms: Design and Analysis, Part 1, Coursera. (Stanford). 
* Algorithms: Design and Analysis, Part 2, Coursera. (Stanford). 
* Heterogeneous Parallel Programming, Coursera. (University of Illinois). 
* Intro to Parallel programming, Udacity. (NVIDIA). 
* Machine Learning, Coursera. (Stanford). 
* Machine Learning Foundations: A Case Study Approach, (U Washington). 
* Coding the Matrix: Linear Algebra through CS Applications, Coursera. 
* Differential Equations in Action, Udacity. 



## Projects

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


### Inferring the Dark Matter Density Profiles of Satellite Galaxies from the Stellar Kinematics

For my undergraduate thesis, I analyzed a high resolution simulation of a system of galaxies similar to the local group, where the main galaxy had characteristics and dynamical properties similar to the Milky-Way ( mass, rotational velocity, thickness of the disk, etc. ). My work consisted of measuring the dynamical properties of the stars in the satellite galaxies and from those measurements I used Monte Carlo Markov Chains (MCMCs) to fit models to the density profiles of the dark matter halos that hosted those satellite galaxies. Then I compared the estimated density profiles to the real halo density profiles that I measured directly from the dark matter particles in the simulation, this allowed me to compare the results of statistical methods used in astronomy to estimate the dark matter profile of the halos from observed satellite galaxies to the actual profile in the simulation and evaluate how accurate are the estimates from observations. In particular I focused on the the density at the most inner part of the halos where currently there is a discrepancy between the theory and the observations, this is known as the Core-Cusp problem. 

<img src="{{ site.url }}assets/images/dm_stars_thesis.png">

The image above shows the Dark Matter (right) of the simulated local group and the stellar content (or galaxies) on the left. The dark matter halos are indicated with circles.


### Quantum Turbulence

[GitHub Repository:   https://github.com/bvillasen/qTurbulence](GitHub Repository: https://github.com/bvillasen/qTurbulence)

Using pyCUDA I developed software to solve the evolution of a Bose-Einstein condensate, which is a gas  cooled to temperatures near the absolute zero (-217 C), at this extreme temperature the gas becomes a super-fluid which means that the fluid has zero viscosity. The animation below shows the density of a simulated BEC on a rotating frame of reference, the tubular structures correspond to vortices where the gas is rotating and the density decreases. On a super-fluid the rotational energy of this vortices is not dissipated as in a regular fluid. 

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/quantum_turbulence.mp4" width="100%"  height="auto" controls preload> </video>
</div>

The animation above is a real-time volumetric render of the simulation, this means that the software that I developed is using the  GPU to solve the physics equations that govern the dynamics of a quantum fluid and simultaneously the GPU is running a ray-tracing algorithm to generate a 3D render of the simulated volume.   

From the data obtained from simulations I studied the properties of the turbulent motion of the gas and compared to known properties of turbulence in regular fluids, in particular I showed that the energy power spectrum on the quantum fluid scales as the well known Kolmogorov relation for turbulence in viscous fluids. This work resulted in the following publication where we propose a mechanism for developing a turbulent flow in a Bose-Einstein Condensate:

[**B. Villaseñor**, R. Zamora-Zamora, D. Bernal, and V. Romero-Rochín, ”*Quantum turbulence by
vortex stirring in a spinor Bose-Einstein condensate*”, 2014, Phys. Rev. A 89, 033611.](https://ui.adsabs.harvard.edu/abs/2014PhRvA..89c3611V/abstract)


### Volume Render 

[GitHub Repositoty: https://github.com/bvillasen/volumeRender](https://github.com/bvillasen/volumeRender)

[GitHub Repository: https://github.com/bvillasen/isingModel](https://github.com/bvillasen/isingModel)

I believe that visualization plays a very important role in understanding the physical phenomena that we study by using computers to numerically solve the equations that govern their evolution, this motivated me to apply my knowledge of GPU computing and visualization to develop a 3D volume render that I could use to visualize the physics that I was solving.

For this project I used **pyCUDA** to call CUDA kernels from python and run a ray-tracing algorithm over some volumetric data, then I used **pyOpenGL** to display the generated image and to record mouse or keyboard events, this allowed the user to interact with the simulation in real time. As a simple example, the animation bellow shows a 3D simulation of the "Ising Model" which is used to represent the orientations of the magnetic dipoles of atoms in  ferromagnetic materials, in this representation, the atomic "spins" can be in one of two states: pointing up or pointing down, the two states are represented as different colors in the visualization. Because of the thermal excitation of the material, each spin can change orientation whit a probability that increases with temperature, this means that when the temperature is low then the spins will tend to orient themselves and this will create a net magnetic field. In contrast, when the temperature increases the spins will start changing orientation randomly so that there is no net magnetic field.


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/ising_3D.mp4" width="100%"  height="auto" controls preload> </video>
</div>

The animation above shows the Ising model for a 3D volume of 512$$^3$$ individual spins. I produced the animation by recording my screen as the simulation is running, as it can be seen I can interact with the simulation by rotating the simulated cube with my mouse, also I can control the variables shown, first it shows both spin orientation, then each orientation is shown individually and then at the end I increase the temperature beyond the critical temperature for which the material losses it's net magnetism due to the random orientations of the atomic spins.   

