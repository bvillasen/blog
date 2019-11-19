---
layout: post
title:  "Dark Matter Simulations Tutorial"
date:   2019-11-17 17:10:24 -0800
categories: dm 
---

# DM Simulations

## Prerequisites 

### MPI

If you don't have MPI on your system you can get it from [Here](https://www.open-mpi.org/software/ompi/v3.0/).



### FFTW
We will need to install FFTW.  To use Gadget2 we need FFTW2, you can download it from here: [FFTW](http://www.fftw.org/download.html) be sure to download FFTW-2.1.5 and install it by: 


```
tar -xzvf fftw-2.1.5.tar.gz
cd fftw-2.1.5
./configure --prefix=/home/bruno/code/fftw_2 --enable-type-prefix --enable-threads --enable-mpi
make
make install
```

### GSL

Download from [Here](ftp://ftp.gnu.org/gnu/gsl/) and install it by:

```
tar -xzvf gsl-2.6.tar.gz 
cd gsl-2.6/
./configure --prefix=/home/bruno/code/gsl
make 
make install

```


## Initial Conditions

To generate initial conditions for our simulations we will use [MUSIC](https://www-n.oca.eu/ohahn/MUSIC/). Download and extract the .zip file. Then change the **Makefile** to add the FFTW and GSL directories:

```
### compile time configuration options
FFTW3		= no
MULTITHREADFFTW	= yes
SINGLEPRECISION	= no
HAVEHDF5        = no
HAVEBOXLIB	= no
BOXLIB_HOME     = ${HOME}/nyx_tot_sterben/BoxLib
FFTW_HOME = /home/bruno/code/fftw_2
GSL_HOME = /home/bruno/code/gsl

##############################################################################
### compiler and path settings
CC      = g++
OPT     = -Wall -Wno-unknown-pragmas -O3 -g -mtune=native
CFLAGS  =  
LFLAGS  = -lgsl -lgslcblas 
CPATHS  = -I. -I$(HOME)/local/include -I/opt/local/include -I/usr/local/include -I$(FFTW_HOME)/include -I$(GSL_HOME)/include
LPATHS  = -L$(HOME)/local/lib -L/opt/local/lib -L/usr/local/lib -L$(FFTW_HOME)/lib -L$(GSL_HOME)/lib 
```

Then just *make* and if everything works correctly you should see the MUSIC executable.

To run MUSIC you need to pass a parameter file (ics_parameters.conf) with the configuration for your initial conditions, here is an example for a $$128^3$$ simulation:

```
[setup]
boxlength		= 50
zstart			= 100
levelmin		= 7
levelmin_TF		= 7
levelmax		= 7
align_top		= no
baryons			= no
use_2LPT		= yes
use_LLA			= yes
periodic_TF		= yes


[cosmology]
Omega_m			= 0.3111
Omega_L			= 0.6889
w0			= -1.0
wa			= 0.0
Omega_b			= 0.0486
H0			= 67.66
sigma_8			= 0.8102
nspec			= 0.9665
transfer		= eisenstein
YHe = 0

[random]
seed[7]			= 12345
seed[8]			= 23456
seed[9]			= 34567
seed[10]		= 45678
seed[11]		= 56789
seed[12]		= 67890

[output]
##Gadget-2 (type=1: high-res particles, type=5: rest)
format			= gadget2
filename		= /home/bruno/Desktop/Dropbox/Developer/dm_simulations/ics_dm/ics_128_gadget
gadget_num_files = 1
gadget_lunit = kpc
UnitLength_in_cm = 3.08568025e21
UnitMass_in_g = 1.989e43
UnitVelocity_in_cm_per_s = 1e5
#gadget_usekpc = yes

[poisson]
fft_fine		= yes
accuracy		= 1e-5
pre_smooth		= 3
post_smooth		= 3
smoother		= gs
laplace_order		= 6
grad_order		= 6
```

To run music just pass the parameter file

```
export LD_LIBRARY_PATH=/home/bruno/code/gsl/lib:$LD_LIBRARY_PATH
./MUSIC ics_parameters.conf
```

## Gadget2

To run the simulation we will use Gadget2, download it from [Here](https://wwwmpa.mpa-garching.mpg.de/gadget/) and extract it by:

```
gunzip gadget-2.0.7.tar.gz
tar -xvf gadget-2.0.7.tar

```

You will have to edit the Makefile, this are the changes I made:

```
#--------------------------------------- Single/Double Precision
OPT   +=  -DDOUBLEPRECISION      
OPT   +=  -DDOUBLEPRECISION_FFTW      


SYSTYPE="falcon"

#--------------------------------------- Adjust settings for target computer

ifeq ($(SYSTYPE),"falcon")
CC       =  mpicc   
OPTIMIZE =  -O3 -Wall
GSL_INCL =  -I/home/bruno/code/gsl/include
GSL_LIBS =  -L/home/bruno/code/gsl/lib 
FFTW_INCL=  -I/home/bruno/code/fftw_2/include
FFTW_LIBS=  -L/home/bruno/code/fftw_2/lib
MPICHLIB =
HDF5INCL =  
HDF5LIB  =  -lhdf5 -lz 
endif
```

Then just *make* and if it works you should have a *Gadget2* executable.

To run a simulation you will have to pass a parameter file, this is an example:

```
%  Relevant files

InitCondFile  	   /home/bruno/Desktop/Dropbox/Developer/dm_simulations/ics_dm/ics_128_gadget
OutputDir          /home/bruno/Desktop/Dropbox/Developer/dm_simulations/output_files

EnergyFile         energy.txt
InfoFile           info.txt
TimingsFile        timings.txt
CpuFile            cpu.txt

RestartFile        restart
SnapshotFileBase   snapshot

OutputListFilename /home/bruno/Desktop/Dropbox/Developer/dm_simulations/outputs_100.txt

% CPU time -limit

TimeLimitCPU      10000000  % = 30 hours
ResubmitOn        0
ResubmitCommand   my-scriptfile


% Code options

ICFormat                 1
SnapFormat               1
ComovingIntegrationOn    1

TypeOfTimestepCriterion  0
OutputListOn             1
PeriodicBoundariesOn     1

%  Caracteristics of run

TimeBegin           0.00990099  % z=100, Begin of the simulation
TimeMax	            1.0

Omega0	              0.3111
OmegaLambda           0.6889
OmegaBaryon           0.0486
HubbleParam           0.6766
BoxSize               50000.0

% Output frequency

TimeBetSnapshot        0.5
TimeOfFirstSnapshot    0

CpuTimeBetRestartFile     36000.0    ; here in seconds
TimeBetStatistics         0.05

NumFilesPerSnapshot       1
NumFilesWrittenInParallel 1



% Accuracy of time integration

ErrTolIntAccuracy      0.025

MaxRMSDisplacementFac  0.2



MaxSizeTimestep       0.01
MinSizeTimestep       0.0




% Tree algorithm, force accuracy, domain update frequency

ErrTolTheta            0.5
TypeOfOpeningCriterion 0
ErrTolForceAcc         0.005


TreeDomainUpdateFrequency    0.005


%  Further parameters of SPH

CourantFac             0.15
DesNumNgb              33
MaxNumNgbDeviation     2
ArtBulkViscConst       0.8
InitGasTemp            1000.0        % always ignored if set to 0
MinGasTemp             50.0


% Memory allocation

PartAllocFactor       1.6
TreeAllocFactor       0.8
BufferSize            30          % in MByte


% System of units

UnitLength_in_cm         3.085678e21       % ;  1.0 kpc
UnitMass_in_g            1.989e43          % ;  1.0e10 solar masses
UnitVelocity_in_cm_per_s 1e5               % ;  1 km/sec
GravityConstantInternal  0


% Softening lengths

MinGasHsmlFractional 0.25

SofteningGas       0
SofteningHalo      80
SofteningDisk      0
SofteningBulge     0
SofteningStars     0
SofteningBndry     0

SofteningGasMaxPhys       0
SofteningHaloMaxPhys      80
SofteningDiskMaxPhys      0
SofteningBulgeMaxPhys     0
SofteningStarsMaxPhys     0
SofteningBndryMaxPhys     0

```

where outputs_100.txt is where you pass the values of **a** when you want to save snapshots.

Finally just run the code by 

```
export LD_LIBRARY_PATH=/home/bruno/code/gsl/lib:$LD_LIBRARY_PATH
mpirun -n 2 ./Gadget2 128_dm.param 
```

