---
layout: post
title:  "Dark Matter Simulations Tutorial"
date:   2019-11-17 17:10:24 -0800
categories: dm 
---

# DM Simulations

## Prerequisites 

### FFTW
We will need to install FFTW.  To use Gadget2 we need FFTW2, you can download it from here: [FFTW](http://www.fftw.org/download.html) be sure to download FFTW-2.1.5 and install it by: 


```
tar -xzvf fftw-2.1.5.tar.gz
cd fftw-2.1.5
./configure --prefix=/home/bruno/code/fftw_2 --enable-type-prefix --enable-threads
make
make install
```

### GSL

Download from [Here](ftp://ftp.gnu.org/gnu/gsl/) and istall it by:

```
tar -xzvf gsl-2.6.tar.gz 
cd gsl-2.6/
./configure --prefix=/home/bruno/code/gsl
make 
make install

```


## Initial Conditions

To generate initial conditions for our simulations we will use [MUSIC] (https://www-n.oca.eu/ohahn/MUSIC/). Download and extract the .zip file. Then change the **Makefile** to add the FFTW and GSL directories:

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

To run MUSIC you need to pass a parameter file with the configuration for your initial conditions, here is an example for a $$128^3$$ simulation:

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




export LD_LIBRARY_PATH=/home/bruno/code/gsl/lib:$LD_LIBRARY_PATH

