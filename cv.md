---
layout: page
title: CV
permalink: /cv/
---

## Bruno Villasenor

### Education

**University of California, Santa Cruz** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; ( August 2016 - Expected Jun 2022 ) \\
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
Received a "come back" offer to further develop of data analysis work done during the previous summer for the Higgs boson detection. Analyzed the Higgs Thrust from monte-carlo simulations and optimized the selection criteria for Higgs events from the Tevatron collider.\\
Advisor: Eric James & Sergo Jindariani

### Teaching Experience

**Teacher Assistant:** *Intro. to Scientific Computing*,  Astronomy Dept. UCSC. Winter 2016, Spring 2017 \\
**Teacher Assistant:** *Computational Physics, 7th semester*, UNAM. Semester: 2016-1.  \\
**Teacher Assistant:** *Electromagnetism I*, 4th semester, UNAM. Semester: 2012-2. \\
**Teacher Assistant:** *Scientific Computing Using GPU's*,  Advanced, UNAM. Semester: 2012-1. \\
**Teacher Assistant:** *Computation*,  1st semester, UNAM. Semesters: 2010-2, 2011-1, 2011-2, 2013-1.

### Mentoring Experience

**Graduate Student Instructor for Introduction to Research (ASTR 9)**,  UCSC, January 2019 - June 2019:\\
Mentored a team of four first year undergraduate students through an astronomy research project that I designed. We ran and analyzed a set of dark matter cosmological simulations, located the and studied the dark matter halos density profile.

### Honors and Awards


* **Excellence in Teaching**: UCSC Astronomy Department Award Recipient, 2017. 
* Second place at the III Mexican Olympiad of Astronomy, INAOE, Mexico, 2007. 
* Participant at the XXXVII International Physics Olympiad, Iran, 2007. 
* Participant at the XXXVI International Physics Olympiad, Singapore, 2006. 
* Silver medal at the X Ibero-American Physics Olympiad, Uruguay, 2005. 
* First place at the XVI Mexican Physics Olympiad, Merida, Mexico, 2005. 
* Second place at the XV Mexican Physics Olympiad, Zacatecas, Mexico, 2004. 
 
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

### Large Scale Cosmological Hydrodynamical Simulations on Multiple GPUs 

Originally Cholla was a hydrodynamics solver that runs in multiple GPUs. For my Ph.D. thesis I have extended Cholla to run cosmological simulations, I added several physics modules: \\
 - A distributed FFT based Poisson solver to  include the self-gravity of the fluid. \\
 - A Particle-Mesh scheme to solve the collisionless dynamics of the dark matter particles.\\
 - Integration with Grackle, an open source library to solve the chemical network and track the ionization states of Hydrogen and Helium on the simulation. Also include a uniform time-dependent UV background to account for the reionization of the universe.
 
 
 The animation bellow shows the evolution of the dark matter for a Cholla simulation, the initial conditions are mostly uniform except for tiny perturbations, as time progresses the regions where     

 <div style="text-align: center">
 <video src="{{ site.url }}assets/videos/dm_50Mpc_3D.mp4" width="100%"  height="auto" controls preload> </video>
 </div>
 
 The image below shows several components of a cosmological hydrodynamical simulation, the first column corresponds to the dark matter density, the second column shows the gas density, the third column correspond to the neutral hydrogen density and finally the last column show the temperature of the gas. The top row shows the results from a simulation evolved using a popular code called [Enzo](https://enzo-project.org/) and the bottom show shows the result from an analogous simulation that I ran using Cholla on 8 Nvidia P100 GPUs.
  
 <img src="{{ site.url }}assets/images/projection_deep_1.png">



Cholla uses MPI, CUDA and OpenMP to leverage the computing power of the largest computers in the world. I have used Cholla to run cosmological simulations in Summit (ORNL, number one in the top500) where I measured the performance of the code obtaining near perfect scaling when used in up to 16,000 GPUs.   


<img src="{{ site.url }}assets/images/weak_scaling.png">




### Quantum Turbulence

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/quantum_turbulence.mp4" width="100%"  height="auto" controls preload> </video>
</div>

### Volume Render 

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/ising_3D.mp4" width="100%"  height="auto" controls preload> </video>
</div>

