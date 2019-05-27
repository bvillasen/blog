---
layout: post
title:  "CHOLLA_PM: Install Cholla on Summit"
date:   2019-02-35 17:10:24 -0800
categories: cholla
---


## Install FFTW
```
wget http://www.fftw.org/fftw-3.3.8.tar.gz
tar -xzvf fftw-3.3.8.tar.gz
cd fftw-3.3.8
./bootstrap.sh
./configure --enable-mpi --enable-openmp --enable-threads --disable-shared --prefix=/ccs/home/bvilasen/code/fftw
make -j 10
make install
```

## Install PFFT

```
git clone https://github.com/mpip/pfft.git
cd pfft
./bootstrap.sh
./configure --disable-fortran --disable-shared --with-fftw3=/ccs/home/bvilasen/code/fftw --prefix=/ccs/home/bvilasen/code/pfft
make -j 10
make install
```

## Install Grackle
Get the repository from [HERE]( https://github.com/grackle-project/grackle ).


Change paths on the Makefile (src/clib/Make.mach.summit) to match your local directories.
```
cd grackle/src/clib
make machine-summit
make opt-high
make omp-on
make
make install
```

## Download and Compile Cholla
Change paths on the Makefile to match your local directories.
```
git clone https://github.com/bvillasen/cholla.git
cd cholla
cp extras/makefile_summit.sh Makefile
module load hdf5
module load cuda
make
```

## Submit an Interactive Job
```
bsub -W 10 -nnodes 2 -P AST149 -Is /bin/bash
```

## Add Grackle library to PATH
```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/ccs/home/bvilasen/code/grackle/lib
```

## Run Cholla
```
jsrun -n 8 -a 1 -c 7 -g 1 -r 4 -l CPU-CPU -d packed -b packed:7 ./cholla tests/3D/Cosmological_hydro_256_summit.txt > results.log
```

## Submit job to the queue
This example runs 8 MPI taks on 2 nodes
```
#!/bin/bash
# Begin LSF Directives
#BSUB -P AST149
#BSUB -W 0:03
#BSUB -nnodes 2
#BSUB -alloc_flags gpumps
#BSUB -J cosmo_256
#BSUB -o cosmo_256.o%J
#BSUB -e cosmo_256.e%J
#BSUB -alloc_flags "smt4"

module load hdf5
module load cuda

export WORK_DIR=$MEMBERWORK/ast149/cosmo_256
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/ccs/home/bvilasen/code/grackle/lib

cd $MEMBERWORK/ast149/cholla
date
export OMP_NUM_THREADS=12
jsrun -n 8 -a 1 -c 7 -g 1 -l CPU-CPU -d packed -b packed:7 ./cholla tests/3D/Cosmological_hydro_256_summit.txt > $WORK_DIR/run_output.log |sort
```
