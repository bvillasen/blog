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
