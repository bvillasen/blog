---
layout: post
title:  "CHOLLA: Domain decomposition"
date:   2017-09-13 17:10:24 -0800
categories: cholla
---

### 256 x 256 x 256 in 16 gpus:

** Before MPI_routines modification: **



Parameter values:  nx = 256, ny = 256, nz = 256, tout = 0.010000, init = Sphere_3D, boundaries = 1 1 1 1 1 1
Output directory:  /lustre/atlas/scratch/bvilasen/ast125/data/cholla_output/
nproc_x 4 nproc_y 2 nproc_z 2
 procID 0: dst[ 12 4 2 2 1 1 ] src[ 12 4 2 2 1 1 ]
 procID 1: dst[ 13 5 3 3 0 0 ] src[ 13 5 3 3 0 0 ]
 procID 2: dst[ 14 6 0 0 3 3 ] src[ 14 6 0 0 3 3 ]
 procID 3: dst[ 15 7 1 1 2 2 ] src[ 15 7 1 1 2 2 ]
 procID 4: dst[ 0 8 6 6 5 5 ] src[ 0 8 6 6 5 5 ]
 procID 5: dst[ 1 9 7 7 4 4 ] src[ 1 9 7 7 4 4 ]
 procID 6: dst[ 2 10 4 4 7 7 ] src[ 2 10 4 4 7 7 ]
 procID 7: dst[ 3 11 5 5 6 6 ] src[ 3 11 5 5 6 6 ]
 procID 8: dst[ 4 12 10 10 9 9 ] src[ 4 12 10 10 9 9 ]
 procID 9: dst[ 5 13 11 11 8 8 ] src[ 5 13 11 11 8 8 ]
 procID 10: dst[ 6 14 8 8 11 11 ] src[ 6 14 8 8 11 11 ]
 procID 11: dst[ 7 15 9 9 10 10 ] src[ 7 15 9 9 10 10 ]
 procID 12: dst[ 8 0 14 14 13 13 ] src[ 8 0 14 14 13 13 ]
 procID 13: dst[ 9 1 15 15 12 12 ] src[ 9 1 15 15 12 12 ]
 procID 14: dst[ 10 2 12 12 15 15 ] src[ 10 2 12 12 15 15 ]
 procID 15: dst[ 11 3 13 13 14 14 ] src[ 11 3 13 13 14 14 ]
Gravity Initialized:
 Local: 64 128 128
 Global: 256 256 256
Local number of grid cells: 64 128 128 1331712
Setting initial conditions...
Dimensions of each cell: dx = 0.003906 dy = 0.003906 dz = 0.003906
Ratio of specific heats gamma = 1.666667
Nstep = 0  Timestep = 0.000000  Simulation time = 0.000000
Using PFFT for self-gravity calculations
Initializing PFFT
PFFT process: nz:2 ny:2 nx:4
PFFT cells:   nz:256 ny:256 nx:256
PFFT local:   nz:128 ny:128 nx:64
procID 0: [ 0 0 0 ], [ 8 8 ] [ 4 4 ] [ 1 3 ]  
procID 1: [ 0 0 1 ], [ 9 9 ] [ 5 5 ] [ 2 0 ]  
procID 2: [ 0 0 2 ], [ 10 10 ] [ 6 6 ] [ 3 1 ]  
procID 3: [ 0 0 3 ], [ 11 11 ] [ 7 7 ] [ 0 2 ]  
procID 4: [ 0 1 0 ], [ 12 12 ] [ 0 0 ] [ 5 7 ]  
procID 5: [ 0 1 1 ], [ 13 13 ] [ 1 1 ] [ 6 4 ]  
procID 6: [ 0 1 2 ], [ 14 14 ] [ 2 2 ] [ 7 5 ]  
procID 7: [ 0 1 3 ], [ 15 15 ] [ 3 3 ] [ 4 6 ]  
procID 8: [ 1 0 0 ], [ 0 0 ] [ 12 12 ] [ 9 11 ]  
procID 9: [ 1 0 1 ], [ 1 1 ] [ 13 13 ] [ 10 8 ]  
procID 10: [ 1 0 2 ], [ 2 2 ] [ 14 14 ] [ 11 9 ]  
procID 11: [ 1 0 3 ], [ 3 3 ] [ 15 15 ] [ 8 10 ]  
procID 12: [ 1 1 0 ], [ 4 4 ] [ 8 8 ] [ 13 15 ]  
procID 13: [ 1 1 1 ], [ 5 5 ] [ 9 9 ] [ 14 12 ]  
procID 14: [ 1 1 2 ], [ 6 6 ] [ 10 10 ] [ 15 13 ]  
procID 15: [ 1 1 3 ], [ 7 7 ] [ 11 11 ] [ 12 14 ]  
*********
procID 0 nxl 64 nxls 0
Local domain: x[ 0.000 0.250 ] y[ 0.000 0.500 ] z[ 0.000 0.500 ]
*********
procID 1 nxl 64 nxls 0
Local domain: x[ 0.000 0.250 ] y[ 0.000 0.500 ] z[ 0.500 1.000 ]
*********
procID 2 nxl 64 nxls 0
Local domain: x[ 0.000 0.250 ] y[ 0.500 1.000 ] z[ 0.000 0.500 ]
*********
procID 3 nxl 64 nxls 0
Local domain: x[ 0.000 0.250 ] y[ 0.500 1.000 ] z[ 0.500 1.000 ]
*********
procID 4 nxl 64 nxls 64
Local domain: x[ 0.250 0.500 ] y[ 0.000 0.500 ] z[ 0.000 0.500 ]
*********
procID 5 nxl 64 nxls 64
Local domain: x[ 0.250 0.500 ] y[ 0.000 0.500 ] z[ 0.500 1.000 ]
*********
procID 6 nxl 64 nxls 64
Local domain: x[ 0.250 0.500 ] y[ 0.500 1.000 ] z[ 0.000 0.500 ]
*********
procID 7 nxl 64 nxls 64
Local domain: x[ 0.250 0.500 ] y[ 0.500 1.000 ] z[ 0.500 1.000 ]
*********
procID 8 nxl 64 nxls 128
Local domain: x[ 0.500 0.750 ] y[ 0.000 0.500 ] z[ 0.000 0.500 ]
*********
procID 9 nxl 64 nxls 128
Local domain: x[ 0.500 0.750 ] y[ 0.000 0.500 ] z[ 0.500 1.000 ]
*********
procID 10 nxl 64 nxls 128
Local domain: x[ 0.500 0.750 ] y[ 0.500 1.000 ] z[ 0.000 0.500 ]
*********
procID 11 nxl 64 nxls 128
Local domain: x[ 0.500 0.750 ] y[ 0.500 1.000 ] z[ 0.500 1.000 ]
*********
procID 12 nxl 64 nxls 192
Local domain: x[ 0.750 1.000 ] y[ 0.000 0.500 ] z[ 0.000 0.500 ]
*********
procID 13 nxl 64 nxls 192
Local domain: x[ 0.750 1.000 ] y[ 0.000 0.500 ] z[ 0.500 1.000 ]
*********
procID 14 nxl 64 nxls 192
Local domain: x[ 0.750 1.000 ] y[ 0.500 1.000 ] z[ 0.000 0.500 ]
*********
procID 15 nxl 64 nxls 192
Local domain: x[ 0.750 1.000 ] y[ 0.500 1.000 ] z[ 0.500 1.000 ]
*********





** After MPI_routines modification: **

Parameter values:  nx = 256, ny = 256, nz = 256, tout = 0.010000, init = Sphere_3D, boundaries = 1 1 1 1 1 1
Output directory:  /lustre/atlas/scratch/bvilasen/ast125/data/cholla_output/
nproc_x 4 nproc_y 2 nproc_z 2
procID 0: dst[ 3 1 4 4 8 8 ] src[ 3 1 4 4 8 8 ]
procID 1: dst[ 0 2 5 5 9 9 ] src[ 0 2 5 5 9 9 ]
procID 2: dst[ 1 3 6 6 10 10 ] src[ 1 3 6 6 10 10 ]
procID 3: dst[ 2 0 7 7 11 11 ] src[ 2 0 7 7 11 11 ]
procID 4: dst[ 7 5 0 0 12 12 ] src[ 7 5 0 0 12 12 ]
procID 5: dst[ 4 6 1 1 13 13 ] src[ 4 6 1 1 13 13 ]
procID 6: dst[ 5 7 2 2 14 14 ] src[ 5 7 2 2 14 14 ]
procID 7: dst[ 6 4 3 3 15 15 ] src[ 6 4 3 3 15 15 ]
procID 8: dst[ 11 9 12 12 0 0 ] src[ 11 9 12 12 0 0 ]
procID 9: dst[ 8 10 13 13 1 1 ] src[ 8 10 13 13 1 1 ]
procID 10: dst[ 9 11 14 14 2 2 ] src[ 9 11 14 14 2 2 ]
procID 11: dst[ 10 8 15 15 3 3 ] src[ 10 8 15 15 3 3 ]
procID 12: dst[ 15 13 8 8 4 4 ] src[ 15 13 8 8 4 4 ]
procID 13: dst[ 12 14 9 9 5 5 ] src[ 12 14 9 9 5 5 ]
procID 14: dst[ 13 15 10 10 6 6 ] src[ 13 15 10 10 6 6 ]
procID 15: dst[ 14 12 11 11 7 7 ] src[ 14 12 11 11 7 7 ]
Gravity Initialized:
Local: 64 128 128
Global: 256 256 256
Local number of grid cells: 64 128 128 1331712
Setting initial conditions...
Dimensions of each cell: dx = 0.003906 dy = 0.003906 dz = 0.003906
Ratio of specific heats gamma = 1.666667
Nstep = 0  Timestep = 0.000000  Simulation time = 0.000000
Using PFFT for self-gravity calculations
Initializing PFFT
PFFT process: nz:2 ny:2 nx:4
PFFT cells:   nz:256 ny:256 nx:256
PFFT local:   nz:128 ny:128 nx:64
procID 0: [ 0 0 0 ], [ 8 8 ] [ 4 4 ] [ 1 3 ]  
procID 1: [ 0 0 1 ], [ 9 9 ] [ 5 5 ] [ 2 0 ]  
procID 2: [ 0 0 2 ], [ 10 10 ] [ 6 6 ] [ 3 1 ]  
procID 3: [ 0 0 3 ], [ 11 11 ] [ 7 7 ] [ 0 2 ]  
procID 4: [ 0 1 0 ], [ 12 12 ] [ 0 0 ] [ 5 7 ]  
procID 5: [ 0 1 1 ], [ 13 13 ] [ 1 1 ] [ 6 4 ]  
procID 6: [ 0 1 2 ], [ 14 14 ] [ 2 2 ] [ 7 5 ]  
procID 7: [ 0 1 3 ], [ 15 15 ] [ 3 3 ] [ 4 6 ]  
procID 8: [ 1 0 0 ], [ 0 0 ] [ 12 12 ] [ 9 11 ]  
procID 9: [ 1 0 1 ], [ 1 1 ] [ 13 13 ] [ 10 8 ]  
procID 10: [ 1 0 2 ], [ 2 2 ] [ 14 14 ] [ 11 9 ]  
procID 11: [ 1 0 3 ], [ 3 3 ] [ 15 15 ] [ 8 10 ]  
procID 12: [ 1 1 0 ], [ 4 4 ] [ 8 8 ] [ 13 15 ]  
procID 13: [ 1 1 1 ], [ 5 5 ] [ 9 9 ] [ 14 12 ]  
procID 14: [ 1 1 2 ], [ 6 6 ] [ 10 10 ] [ 15 13 ]  
procID 15: [ 1 1 3 ], [ 7 7 ] [ 11 11 ] [ 12 14 ]  
*********
procID 0 nxl 64 nxls 0
Local domain: x[ 0.000 0.250 ] y[ 0.000 0.500 ] z[ 0.000 0.500 ]
*********
procID 1 nxl 64 nxls 64
Local domain: x[ 0.250 0.500 ] y[ 0.000 0.500 ] z[ 0.000 0.500 ]
*********
procID 2 nxl 64 nxls 128
Local domain: x[ 0.500 0.750 ] y[ 0.000 0.500 ] z[ 0.000 0.500 ]
*********
procID 3 nxl 64 nxls 192
Local domain: x[ 0.750 1.000 ] y[ 0.000 0.500 ] z[ 0.000 0.500 ]
*********
procID 4 nxl 64 nxls 0
Local domain: x[ 0.000 0.250 ] y[ 0.500 1.000 ] z[ 0.000 0.500 ]
*********
procID 5 nxl 64 nxls 64
Local domain: x[ 0.250 0.500 ] y[ 0.500 1.000 ] z[ 0.000 0.500 ]
*********
procID 6 nxl 64 nxls 128
Local domain: x[ 0.500 0.750 ] y[ 0.500 1.000 ] z[ 0.000 0.500 ]
*********
procID 7 nxl 64 nxls 192
Local domain: x[ 0.750 1.000 ] y[ 0.500 1.000 ] z[ 0.000 0.500 ]
*********
procID 8 nxl 64 nxls 0
Local domain: x[ 0.000 0.250 ] y[ 0.000 0.500 ] z[ 0.500 1.000 ]
*********
procID 9 nxl 64 nxls 64
Local domain: x[ 0.250 0.500 ] y[ 0.000 0.500 ] z[ 0.500 1.000 ]
*********
procID 10 nxl 64 nxls 128
Local domain: x[ 0.500 0.750 ] y[ 0.000 0.500 ] z[ 0.500 1.000 ]
*********
procID 11 nxl 64 nxls 192
Local domain: x[ 0.750 1.000 ] y[ 0.000 0.500 ] z[ 0.500 1.000 ]
*********
procID 12 nxl 64 nxls 0
Local domain: x[ 0.000 0.250 ] y[ 0.500 1.000 ] z[ 0.500 1.000 ]
*********
procID 13 nxl 64 nxls 64
Local domain: x[ 0.250 0.500 ] y[ 0.500 1.000 ] z[ 0.500 1.000 ]
*********
procID 14 nxl 64 nxls 128
Local domain: x[ 0.500 0.750 ] y[ 0.500 1.000 ] z[ 0.500 1.000 ]
*********
procID 15 nxl 64 nxls 192
Local domain: x[ 0.750 1.000 ] y[ 0.500 1.000 ] z[ 0.500 1.000 ]
*********



### 512 x 256 x 256 in 16 gpus:


** Before MPI_routines modification: **


Parameter values:  nx = 512, ny = 256, nz = 256, tout = 0.010000, init = Sphere_3D, boundaries = 1 1 1 1 1 1
nproc_x 4 nproc_y 2 nproc_z 2
 procID 0: dst[ 12 4 2 2 1 1 ] src[ 12 4 2 2 1 1 ]
 procID 1: dst[ 13 5 3 3 0 0 ] src[ 13 5 3 3 0 0 ]
 procID 2: dst[ 14 6 0 0 3 3 ] src[ 14 6 0 0 3 3 ]
 procID 3: dst[ 15 7 1 1 2 2 ] src[ 15 7 1 1 2 2 ]
 procID 4: dst[ 0 8 6 6 5 5 ] src[ 0 8 6 6 5 5 ]
 procID 5: dst[ 1 9 7 7 4 4 ] src[ 1 9 7 7 4 4 ]
 procID 6: dst[ 2 10 4 4 7 7 ] src[ 2 10 4 4 7 7 ]
 procID 7: dst[ 3 11 5 5 6 6 ] src[ 3 11 5 5 6 6 ]
 procID 8: dst[ 4 12 10 10 9 9 ] src[ 4 12 10 10 9 9 ]
 procID 9: dst[ 5 13 11 11 8 8 ] src[ 5 13 11 11 8 8 ]
 procID 10: dst[ 6 14 8 8 11 11 ] src[ 6 14 8 8 11 11 ]
 procID 11: dst[ 7 15 9 9 10 10 ] src[ 7 15 9 9 10 10 ]
 procID 12: dst[ 8 0 14 14 13 13 ] src[ 8 0 14 14 13 13 ]
 procID 13: dst[ 9 1 15 15 12 12 ] src[ 9 1 15 15 12 12 ]
 procID 14: dst[ 10 2 12 12 15 15 ] src[ 10 2 12 12 15 15 ]
 procID 15: dst[ 11 3 13 13 14 14 ] src[ 11 3 13 13 14 14 ]
Gravity Initialized:
 Local: 128 128 128
 Global: 512 256 256
Local number of grid cells: 128 128 128 2515456
Setting initial conditions...
Dimensions of each cell: dx = 0.001953 dy = 0.003906 dz = 0.003906
Ratio of specific heats gamma = 1.666667
Nstep = 0  Timestep = 0.000000  Simulation time = 0.000000
Using PFFT for self-gravity calculations
Initializing PFFT
PFFT process: nz:2 ny:2 nx:4
PFFT cells:   nz:256 ny:256 nx:512
PFFT local:   nz:128 ny:128 nx:128
procID 0: [ 0 0 0 ], [ 8 8 ] [ 4 4 ] [ 1 3 ]  
procID 1: [ 0 0 1 ], [ 9 9 ] [ 5 5 ] [ 2 0 ]  
procID 2: [ 0 0 2 ], [ 10 10 ] [ 6 6 ] [ 3 1 ]  
procID 3: [ 0 0 3 ], [ 11 11 ] [ 7 7 ] [ 0 2 ]  
procID 4: [ 0 1 0 ], [ 12 12 ] [ 0 0 ] [ 5 7 ]  
procID 5: [ 0 1 1 ], [ 13 13 ] [ 1 1 ] [ 6 4 ]  
procID 6: [ 0 1 2 ], [ 14 14 ] [ 2 2 ] [ 7 5 ]  
procID 7: [ 0 1 3 ], [ 15 15 ] [ 3 3 ] [ 4 6 ]  
procID 8: [ 1 0 0 ], [ 0 0 ] [ 12 12 ] [ 9 11 ]  
procID 9: [ 1 0 1 ], [ 1 1 ] [ 13 13 ] [ 10 8 ]  
procID 10: [ 1 0 2 ], [ 2 2 ] [ 14 14 ] [ 11 9 ]  
procID 11: [ 1 0 3 ], [ 3 3 ] [ 15 15 ] [ 8 10 ]  
procID 12: [ 1 1 0 ], [ 4 4 ] [ 8 8 ] [ 13 15 ]  
procID 13: [ 1 1 1 ], [ 5 5 ] [ 9 9 ] [ 14 12 ]  
procID 14: [ 1 1 2 ], [ 6 6 ] [ 10 10 ] [ 15 13 ]  
procID 15: [ 1 1 3 ], [ 7 7 ] [ 11 11 ] [ 12 14 ]  
*********
procID 0 nxl 128 nxls 0
Local domain: x[ 0.000 0.250 ] y[ 0.000 0.500 ] z[ 0.000 0.500 ]
*********
procID 1 nxl 128 nxls 0
Local domain: x[ 0.000 0.250 ] y[ 0.000 0.500 ] z[ 0.500 1.000 ]
*********
procID 2 nxl 128 nxls 0
Local domain: x[ 0.000 0.250 ] y[ 0.500 1.000 ] z[ 0.000 0.500 ]
*********
procID 3 nxl 128 nxls 0
Local domain: x[ 0.000 0.250 ] y[ 0.500 1.000 ] z[ 0.500 1.000 ]
*********
procID 4 nxl 128 nxls 128
Local domain: x[ 0.250 0.500 ] y[ 0.000 0.500 ] z[ 0.000 0.500 ]
*********
procID 5 nxl 128 nxls 128
Local domain: x[ 0.250 0.500 ] y[ 0.000 0.500 ] z[ 0.500 1.000 ]
*********
procID 6 nxl 128 nxls 128
Local domain: x[ 0.250 0.500 ] y[ 0.500 1.000 ] z[ 0.000 0.500 ]
*********
procID 7 nxl 128 nxls 128
Local domain: x[ 0.250 0.500 ] y[ 0.500 1.000 ] z[ 0.500 1.000 ]
*********
procID 8 nxl 128 nxls 256
Local domain: x[ 0.500 0.750 ] y[ 0.000 0.500 ] z[ 0.000 0.500 ]
*********
procID 9 nxl 128 nxls 256
Local domain: x[ 0.500 0.750 ] y[ 0.000 0.500 ] z[ 0.500 1.000 ]
*********
procID 10 nxl 128 nxls 256
Local domain: x[ 0.500 0.750 ] y[ 0.500 1.000 ] z[ 0.000 0.500 ]
*********
procID 11 nxl 128 nxls 256
Local domain: x[ 0.500 0.750 ] y[ 0.500 1.000 ] z[ 0.500 1.000 ]
*********
procID 12 nxl 128 nxls 384
Local domain: x[ 0.750 1.000 ] y[ 0.000 0.500 ] z[ 0.000 0.500 ]
*********
procID 13 nxl 128 nxls 384
Local domain: x[ 0.750 1.000 ] y[ 0.000 0.500 ] z[ 0.500 1.000 ]
*********
procID 14 nxl 128 nxls 384
Local domain: x[ 0.750 1.000 ] y[ 0.500 1.000 ] z[ 0.000 0.500 ]
*********
procID 15 nxl 128 nxls 384
Local domain: x[ 0.750 1.000 ] y[ 0.500 1.000 ] z[ 0.500 1.000 ]
*********



** After MPI_routines modification: **

 Parameter values:  nx = 512, ny = 256, nz = 256, tout = 0.010000, init = Sphere_3D, boundaries = 1 1 1 1 1 1
nproc_x 4 nproc_y 2 nproc_z 2
 procID 0: dst[ 3 1 4 4 8 8 ] src[ 3 1 4 4 8 8 ]
 procID 1: dst[ 0 2 5 5 9 9 ] src[ 0 2 5 5 9 9 ]
 procID 2: dst[ 1 3 6 6 10 10 ] src[ 1 3 6 6 10 10 ]
 procID 3: dst[ 2 0 7 7 11 11 ] src[ 2 0 7 7 11 11 ]
 procID 4: dst[ 7 5 0 0 12 12 ] src[ 7 5 0 0 12 12 ]
 procID 5: dst[ 4 6 1 1 13 13 ] src[ 4 6 1 1 13 13 ]
 procID 6: dst[ 5 7 2 2 14 14 ] src[ 5 7 2 2 14 14 ]
 procID 7: dst[ 6 4 3 3 15 15 ] src[ 6 4 3 3 15 15 ]
 procID 8: dst[ 11 9 12 12 0 0 ] src[ 11 9 12 12 0 0 ]
 procID 9: dst[ 8 10 13 13 1 1 ] src[ 8 10 13 13 1 1 ]
 procID 10: dst[ 9 11 14 14 2 2 ] src[ 9 11 14 14 2 2 ]
 procID 11: dst[ 10 8 15 15 3 3 ] src[ 10 8 15 15 3 3 ]
 procID 12: dst[ 15 13 8 8 4 4 ] src[ 15 13 8 8 4 4 ]
 procID 13: dst[ 12 14 9 9 5 5 ] src[ 12 14 9 9 5 5 ]
 procID 14: dst[ 13 15 10 10 6 6 ] src[ 13 15 10 10 6 6 ]
 procID 15: dst[ 14 12 11 11 7 7 ] src[ 14 12 11 11 7 7 ]
Gravity Initialized:
 Local: 128 128 128
 Global: 512 256 256
Local number of grid cells: 128 128 128 2515456
Setting initial conditions...
Dimensions of each cell: dx = 0.001953 dy = 0.003906 dz = 0.003906
Ratio of specific heats gamma = 1.666667
Nstep = 0  Timestep = 0.000000  Simulation time = 0.000000
Using PFFT for self-gravity calculations
Initializing PFFT
 PFFT process: nz:2 ny:2 nx:4
 PFFT cells:   nz:256 ny:256 nx:512
 PFFT local:   nz:128 ny:128 nx:128
 procID 0: [ 0 0 0 ], [ 8 8 ] [ 4 4 ] [ 1 3 ]  
 procID 1: [ 0 0 1 ], [ 9 9 ] [ 5 5 ] [ 2 0 ]  
 procID 2: [ 0 0 2 ], [ 10 10 ] [ 6 6 ] [ 3 1 ]  
 procID 3: [ 0 0 3 ], [ 11 11 ] [ 7 7 ] [ 0 2 ]  
 procID 4: [ 0 1 0 ], [ 12 12 ] [ 0 0 ] [ 5 7 ]  
 procID 5: [ 0 1 1 ], [ 13 13 ] [ 1 1 ] [ 6 4 ]  
 procID 6: [ 0 1 2 ], [ 14 14 ] [ 2 2 ] [ 7 5 ]  
 procID 7: [ 0 1 3 ], [ 15 15 ] [ 3 3 ] [ 4 6 ]  
 procID 8: [ 1 0 0 ], [ 0 0 ] [ 12 12 ] [ 9 11 ]  
 procID 9: [ 1 0 1 ], [ 1 1 ] [ 13 13 ] [ 10 8 ]  
 procID 10: [ 1 0 2 ], [ 2 2 ] [ 14 14 ] [ 11 9 ]  
 procID 11: [ 1 0 3 ], [ 3 3 ] [ 15 15 ] [ 8 10 ]  
 procID 12: [ 1 1 0 ], [ 4 4 ] [ 8 8 ] [ 13 15 ]  
 procID 13: [ 1 1 1 ], [ 5 5 ] [ 9 9 ] [ 14 12 ]  
 procID 14: [ 1 1 2 ], [ 6 6 ] [ 10 10 ] [ 15 13 ]  
 procID 15: [ 1 1 3 ], [ 7 7 ] [ 11 11 ] [ 12 14 ]
*********
procID 0 nxl 128 nxls 0
Local domain: x[ 0.000 0.250 ] y[ 0.000 0.500 ] z[ 0.000 0.500 ]
*********
procID 1 nxl 128 nxls 128
Local domain: x[ 0.250 0.500 ] y[ 0.000 0.500 ] z[ 0.000 0.500 ]
*********
procID 2 nxl 128 nxls 256
Local domain: x[ 0.500 0.750 ] y[ 0.000 0.500 ] z[ 0.000 0.500 ]
*********
procID 3 nxl 128 nxls 384
Local domain: x[ 0.750 1.000 ] y[ 0.000 0.500 ] z[ 0.000 0.500 ]
*********
procID 4 nxl 128 nxls 0
Local domain: x[ 0.000 0.250 ] y[ 0.500 1.000 ] z[ 0.000 0.500 ]
*********
procID 5 nxl 128 nxls 128
Local domain: x[ 0.250 0.500 ] y[ 0.500 1.000 ] z[ 0.000 0.500 ]
*********
procID 6 nxl 128 nxls 256
Local domain: x[ 0.500 0.750 ] y[ 0.500 1.000 ] z[ 0.000 0.500 ]
*********
procID 7 nxl 128 nxls 384
Local domain: x[ 0.750 1.000 ] y[ 0.500 1.000 ] z[ 0.000 0.500 ]
*********
procID 8 nxl 128 nxls 0
Local domain: x[ 0.000 0.250 ] y[ 0.000 0.500 ] z[ 0.500 1.000 ]
*********
procID 9 nxl 128 nxls 128
Local domain: x[ 0.250 0.500 ] y[ 0.000 0.500 ] z[ 0.500 1.000 ]
*********
procID 10 nxl 128 nxls 256
Local domain: x[ 0.500 0.750 ] y[ 0.000 0.500 ] z[ 0.500 1.000 ]
*********
procID 11 nxl 128 nxls 384
Local domain: x[ 0.750 1.000 ] y[ 0.000 0.500 ] z[ 0.500 1.000 ]
*********
procID 12 nxl 128 nxls 0
Local domain: x[ 0.000 0.250 ] y[ 0.500 1.000 ] z[ 0.500 1.000 ]
*********
procID 13 nxl 128 nxls 128
Local domain: x[ 0.250 0.500 ] y[ 0.500 1.000 ] z[ 0.500 1.000 ]
*********
procID 14 nxl 128 nxls 256
Local domain: x[ 0.500 0.750 ] y[ 0.500 1.000 ] z[ 0.500 1.000 ]
*********
procID 15 nxl 128 nxls 384
Local domain: x[ 0.750 1.000 ] y[ 0.500 1.000 ] z[ 0.500 1.000 ]
*********

```c

 // update the conserved variable array
  dev_conserved[            id] += dtodx * (dev_F[            id-1] - dev_F[            id]);
  dev_conserved[  n_cells + id] += dtodx * (dev_F[  n_cells + id-1] - dev_F[  n_cells + id]);
  dev_conserved[2*n_cells + id] += dtodx * (dev_F[2*n_cells + id-1] - dev_F[2*n_cells + id]);
  dev_conserved[3*n_cells + id] += dtodx * (dev_F[3*n_cells + id-1] - dev_F[3*n_cells + id]);
  dev_conserved[4*n_cells + id] += dtodx * (dev_F[4*n_cells + id-1] - dev_F[4*n_cells + id]);
  #ifdef DE
  dev_conserved[5*n_cells + id] += dtodx * (dev_F[5*n_cells + id-1] - dev_F[5*n_cells + id])
                                +  dtodx * P * 0.5 * (vx_imo - vx_ipo);
  #endif
  d  =  dev_conserved[            id];
  d_inv = 1.0 / d;
  vx =  dev_conserved[1*n_cells + id] * d_inv;
  vy =  dev_conserved[2*n_cells + id] * d_inv;
  vz =  dev_conserved[3*n_cells + id] * d_inv;
  P  = (dev_conserved[4*n_cells + id] - 0.5*d*(vx*vx + vy*vy + vz*vz)) * (gamma - 1.0);
  //if (P < 0.0) printf("%3d %3d %3d Negative pressure after final update. %f %f %f %f %f\n", xid, yid, zid, dev_conserved[4*n_cells + id], 0.5*d*vx*vx, 0.5*d*vy*vy, 0.5*d*vz*vz, P);
  #ifdef STATIC_GRAV
  calc_g_3D_CUDA(xid, yid, zid, x_off, y_off, z_off, n_ghost, dx, dy, dz, xbound, ybound, zbound, &gx, &gy, &gz);
  d_n  =  dev_conserved[            id];
  d_inv_n = 1.0 / d_n;
  vx_n =  dev_conserved[1*n_cells + id] * d_inv_n;
  vy_n =  dev_conserved[2*n_cells + id] * d_inv_n;
  vz_n =  dev_conserved[3*n_cells + id] * d_inv_n;
  dev_conserved[  n_cells + id] += 0.5*dt*gx*(d + d_n);
  dev_conserved[2*n_cells + id] += 0.5*dt*gy*(d + d_n);
  dev_conserved[3*n_cells + id] += 0.5*dt*gz*(d + d_n);
  //gcorr =  0.5*dt*gz*(d + d_n);
  dev_conserved[4*n_cells + id] += 0.25*dt*gx*(d + d_n)*(vx + vx_n)
                                +  0.25*dt*gy*(d + d_n)*(vy + vy_n)
                                +  0.25*dt*gz*(d + d_n)*(vz + vz_n);
  #endif  
```
