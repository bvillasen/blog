---
layout: post
title:  "Cholla_PM: Summit Scaling Tests (Instructions)"
date:   2019-05-27 17:10:24 -0800
categories: cholla
---

### Cholla Location:

I installed all the necessary software ( FFTW, PFFT, GRACKLE ) under the **PROJHOME** directory:

```
/ccs/proj/ast149
``` 

I installed Cholla on the  **PROJWORK** directory:


```
/gpfs/alpine/proj-shared/ast149/cosmo_tests/cholla
```

To recompile Cholla these are the modules you need:

```
module load hdf5
module load cuda
```

### Running Scaling Tests:

I added initial conditions for running scaling test on the **PROJWORK** directory:

```
/gpfs/alpine/proj-shared/ast149/cosmo_tests
```

The scaling test consist on duplicating a box of 25Mpc per each GPU, this is turned on using the compiler parameter **TILED_INITIAL_CONDITIONS**, the number of timesteps can be set using the compiling parameter **N_STEPS_LIMIT**, currently N_STEPS_LIMIT=26 this means the code will run the first 26 timesteps and exit, ignoring the first timestep the average time for the different sections of the timestep will be recorded on the **run_timing.log** file ( same directory as the Cholla executable ).


There are two possibilities for the scaling tests: $$128^3$$ cells/particles per GPU or $$256^3$$ cells/particles per GPU  

To run tests using $$128^3$$ per GPU:

```
cd scale_128
bsub submit_jobs.lsf
```

The main command  on the **submit_jobs.lsf** file is:

```
#BSUB -nnodes 1

jsrun -n 4 -a 1 -c 7 -g 1 -r 4 -l CPU-CPU -d packed -b packed:7 ./cholla tests/3D/Cosmological_Scaling_128.txt > $WORK_DIR/run_output.log |sort
```

This will run 4 MPI processes on 1 node.

**-n:** Number of resources \\
**-a:** Number of MPI tasks per resource \\
**-c:** Number of physical cores per resource \\
**-g:** Number of GPUs per resource \\
**-r:** Number of resources per node \\

For a visual distribution of the resources check: [jsrun Visualizer](https://jsrunvisualizer.olcf.ornl.gov/?s4f0o128n6c7g1r11d1b27l0=)

To change the size of the problem you need to increase the number of Resources and the number of nodes accordingly ( also change the number of resources per node, 6 GPUs per node ), for example to run using 64 GPUs:

```
#BSUB -nnodes 11

jsrun -n 64 -a 1 -c 7 -g 1 -r 6 -l CPU-CPU -d packed -b packed:7 ./cholla tests/3D/Cosmological_Scaling_128.txt > $WORK_DIR/run_output.log |sort
```

For the scaling tests it's also necessary to change the simulation parameter file. You will need to change the box size ( numerical and physical ) to match the number of GPUs.

The parameter files are in the Cholla directory: **tests/3D/Cosmological_Scaling_128.txt** or **tests/3D/Cosmological_Scaling_256.txt** 

The initial configuration is set to run using 4 GPUs, this corresponds to the next parameters for a $$128^3$$ per GPU simulation:

```
nx=256
ny=256
nz=128
xlen=50000.0
ylen=50000.0
zlen=25000.0
```

Length units are **kpc**. Note that the physical length must match the number of cells for each direction so that $$dx = dy = dz$$

At the end of the each simulation the average timing values for each section of the timestep will be appended to the **run_timing.log**  file ( same location as Cholla excecutable ), the columns correspond to:

**0:** nx ( cells ) \\
**1:** ny ( cells ) \\
**2:** nz ( cells ) \\
**3:** Number of GPUs \\
**4:** Number of OpenMP threads \\
**5:** Number of timesteps for the timing average \\
**6:** Average Time on Computing dt \\
**7:** Average Time on Hydro \\
**8:** Average Time on Boundary transfers \\
**9:** Average Time on Gravitational Potential \\
**10:** Average Time on Potential Boundary transfers \\
**11:** Average Time on Compute Particles Density \\
**12:** Average Time on Particles Boundary transfers \\
**13:** Average Time on Particles Density boundary transfers \\
**14:** Average Time on Update Particles Step 1 \\
**15:** Average Time on Update Particles Step 2 ( also compute gravitational acceleration ) \\
**16:** Average Time on Grackle Cooling \\
**17:** Average Timestep time 


### Cosmological Simulations:

I ran two complete cosmological simulations, the outputs are in the **PROJWORK** directory:


```
/gpfs/alpine/proj-shared/ast149/cosmo_tests
```

**1: cosmo_512:**  A 50 Mpc$$^3$$ box using 512$$^3$$ cells/particles. **It took about 55 min on 64 GPUs, 128$$^3$$ cells per GPU**.

**2: cosmo_1024:**  A 100 Mpc$$^3$$ box using 1024$$^3$$ cells/particles. **It took 8.1 hours on 64 GPUs, 256$$^3$$ cells per GPU**. This had to be ran in 4 separate submissions since the max run time is 2 hours for jobs using less than  46 nodes.

### Compress Snapshot Data:

I added scripts to combine the several output files into a single snapshot file. You can find these scripts under the directory **python_scripts** in the Cholla folder :

To run the python script you probably will want to use an interactive job, you can request one by:

```
bsub -W 10 -nnodes 1 -P AST149 -Is /bin/bash
```

the command above will request 1 node for 10 minutes. Once the interactive job was initialized you need to add the needed modules and run the python script. 


```
module load hdf5
module load python/2.7.15-anaconda2-5.3.0
python python_scripts/compress_snapshots.py
```

In the **compress_snapshots.py** you can change the input_directory and output_directory accordingly to match the location of the raw Cholla output files (inDir) and the location where the compressed files will be written (outDir), currently this are set to compress the $$1024^3$$ simulation:

```
dataDir = '/gpfs/alpine/proj-shared/ast149/cosmo_tests/'
inDir = dataDir + 'cosmo_1024/output_snapshots/'
outDir = dataDir + 'cosmo_1024/snapshots/'
```

Additionally you can choose which snapshots to compress, you can set **snapshots_all** and it will compress all the snapshots available on the input directory or you can use a list with the number of the snapshots to compress, the example below will compress snapshot 99 and snapshot 199

```
# snapshots_to_compress = snapshots_all
snapshots_to_compress = [ 99, 199 ]
``` 
 
 Finally you can choose which fields you want to save and the floating point precision:
 
 ```
 hydro_fields = ['density', 'GasEnergy']
 particles_fields = ['density']
 
 precision = np.float32
 ```
 
 The example above will only compress the selected fields for hydro and particles, to compress all the available fields use:
  
 ```
 hydro_fields = 'all'
 particles_fields = 'all'
 ```
    

 