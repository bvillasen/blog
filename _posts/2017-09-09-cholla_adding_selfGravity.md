---
layout: post
title:  "CHOLLA: self-gravity implementation"
date:   2017-09-09 17:10:24 -0800
categories: cholla
---

### Starting from the December-15 commit ( last commit from Evan )

* Created makefile for shamrock

* Added new initial conditions and test file for a 3D spherical overdensity

* Added SELF_GRAVITY switch to makefile

* Added self_gravity_functions.h and self_gravity_functions.cpp files

* Added a gravity class ( Grav3D ) for computing the gravitational potential from a general density field.
- The Grav3D class is initialized in the the Grid3D class, in this way grav3D will be an instance inside grid3D
- The Grav3D class has fields for general density, and potential
- The Grav3D class has functions for writing to the output HDF5 file


* Added makefile for titan and xstream

* Added files mpi_pfft.h and mpi_pfft.cpp for the data and partial functions related to the potential calculation

* Added function to grid3D to copy density from conservatives to density_h field in grav3d object

* **IMPORTANT:** Changed the way the 3D grid of mpi_processes is made:
- In line 401 of file **mpi_rutines.cpp**  transposed the nested loop, now the the x-axis is filed in the first index
- This was done to match the way PFFT assigns coordinates to processes.
- So far I haven't seen a change in the hydro calculations.   

* Potential boundaries:
- In line 887 of file mpi_rutines.cpp  (Allocate_MPI_Buffers_BLOCK ) I increazed the size of mpi_bufers
- Added functions to Grid3D in mpi_boundaries.cpp to load and read the potential to mpi_buffers
- Loaded buffers from for each side and each direction in Load_and_Send_MPI_Comm_Buffers_BLOCK, file: mpi_bounderies.cpp
- Read potential boundaries in Unload_MPI_Comm_Buffers_BLOCK, file: mpi_bounderies.cpp
