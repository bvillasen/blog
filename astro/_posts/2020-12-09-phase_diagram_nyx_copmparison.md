---
layout: post
title: "Nyx Density Temperature Comparison"
date:   2020-12-08 10:10:24 -0800
categorines: dm cholla
---

Here I compare the density-temperature distribution from analogous **adiabatic** simulations  that I ran with **Nyx** and **Cholla**.

- Box: 50 Mpc/h, 256$$^3$$ cells ( uniform resolution )


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_nyx_cholla.mp4" width="100%"  height="auto" controls preload> </video>
</div>

As shown, the evolution of the gas temperature is very different, the temperatures for the IGM from the Nyx simulation are ~10$$^4$$ K at $$z>2$$ for a simulation in which no heating is present. For the Cholla simulation the IGM cools adiabatically during the entire simulation and only the gas that collapsed into halos is heated to high temperatures.

The contents of the Makefile for compiling Nyx:


```
# AMREX_HOME defines the directory in which we will find all the BoxLib code
AMREX_HOME ?= ../../../amrex

# TOP defines the directory in which we will find Source, Exec, etc
TOP = ../..

# compilation options
COMP    =  gnu
USE_OMP = TRUE
USE_MPI = TRUE

PRECISION = DOUBLE
USE_SINGLE_PRECISION_PARTICLES = FALSE
DEBUG     = FALSE

# physics
DIM      = 3
USE_GRAV = TRUE
USE_HEATCOOL = FALSE
USE_AGN = FALSE
USE_CVODE = FALSE
USE_SUNDIALS3 = FALSE

Bpack := ./Make.package
Blocs := .

include $(TOP)/Exec/Make.Nyx
```



The contents of the parameter file I used for the Nyx simulation:

```
# ------------------  INPUTS TO MAIN PROGRAM  -------------------
max_step = 10000000

nyx.ppm_type = 1
nyx.use_colglaz = 0
nyx.add_ext_src = 0

nyx.do_santa_barbara = 1
nyx.init_sb_vels     = 1
#nyx.init with sph particles = 1
#nyx.sph particle file = ic_sb_sph.ascii

#This is 1e-8 times the lowest density in plt00000
nyx.small_dens = 1.e-2

#This is 1e-5 times the constant temparature in plt00000
nyx.small_temp = 1.e-2

gravity.sl_tol = 1.e-12

nyx.initial_z = 100
nyx.final_a = 1.0

#File written during the run: nstep | time | dt | redshift | a
amr.data_log = runlog
amr.grid_log = grdlog


gravity.gravity_type = PoissonGrav
gravity.no_sync      = 1
gravity.no_composite = 1
gravity.solve_with_hpgmg = 0

mg.bottom_solver = 4

# PROBLEM SIZE & GEOMETRY
geometry.is_periodic =  1     1     1
geometry.coord_sys   =  0

geometry.prob_lo     =  0     0     0

#Domain size in Mpc
geometry.prob_hi     =  73.898906 73.898906 73.898906

amr.n_cell           = 256 256 256
amr.max_grid_size    = 256


# >>>>>>>>>>>>>  BC FLAGS <<<<<<<<<<<<<<<<
# 0 = Interior           3 = Symmetry
# 1 = Inflow             4 = SlipWall
# 2 = Outflow
# >>>>>>>>>>>>>  BC FLAGS <<<<<<<<<<<<<<<<
nyx.lo_bc       =  0   0   0
nyx.hi_bc       =  0   0   0

# WHICH PHYSICS
nyx.do_hydro = 1
nyx.do_grav  = 1

# COMOVING
#nyx.comoving_OmM = 0.2614
nyx.comoving_OmM = 0.3111
nyx.comoving_OmB = 0.0497
nyx.comoving_h   = 0.6766

# PARTICLES
nyx.do_dm_particles = 1

# >>>>>>>>>>>>>  PARTICLE INIT OPTIONS <<<<<<<<<<<<<<<<
#  "AsciiFile"        "Random"	    "Cosmological"
# >>>>>>>>>>>>>  PARTICLE INIT OPTIONS <<<<<<<<<<<<<<<<
nyx.particle_init_type = AsciiFile
nyx.ascii_particle_file = /home/bruno/Desktop/ssd_0/data/cosmo_sims/nyx/256_hydro_50Mpc/ic_256_dm_50Mpc.ascii

# >>>>>>>>>>>>>  PARTICLE MOVE OPTIONS <<<<<<<<<<<<<<<<
#  "Gravitational"    "Random"
# >>>>>>>>>>>>>  PARTICLE MOVE OPTIONS <<<<<<<<<<<<<<<<
nyx.particle_move_type = Gravitational


# TIME STEP CONTROL
particles.cfl      = 0.3     # 'cfl' for particles
nyx.cfl            = 0.3     # cfl number for hyperbolic system
nyx.init_shrink    = 1.0     # scale back initial timestep
nyx.change_max     = 1.1     # factor by which timestep can change
nyx.dt_cutoff      = 5.e-20  # level 0 timestep below which we halt

# DIAGNOSTICS & VERBOSITY
nyx.sum_interval      = -1      # timesteps between computing mass
nyx.v                 = 0       # verbosity in Castro.cpp
gravity.v             = 1       # verbosity in Gravity.cpp
amr.v                 = 0       # verbosity in Amr.cpp
mg.v                  = 0       # verbosity in Amr.cpp
particles.v           = 1       # verbosity in Particle class
#amr.grid_log         = grdlog  # name of grid logging file

# REFINEMENT / REGRIDDING
amr.max_level          = 0        # maximum level number allowed
amr.ref_ratio          = 2 2 2 2
amr.regrid_int         = 4 4 4 4
amr.n_error_buf        = 0 0 0 8
amr.refine_grid_layout = 1
amr.regrid_on_restart  = 1
amr.blocking_factor    = 32
amr.subcycling_mode    = None

# CHECKPOINT FILES
amr.check_file      = /home/bruno/Desktop/ssd_0/data/cosmo_sims/nyx/256_hydro_50Mpc/chk
amr.check_int       = 1000

# PLOTFILES
amr.plot_file       = /home/bruno/Desktop/ssd_0/data/cosmo_sims/nyx/256_hydro_50Mpc/plt
amr.plot_int        = 10

amr.plot_vars        = density xmom ymom zmom Temp
amr.derive_plot_vars = NONE

particles.write in plotfile

#PROBIN FILENAME
amr.probin_file = probin
```
