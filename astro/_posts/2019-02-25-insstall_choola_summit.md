---
layout: post
title:  "CHOLLA_PM: Install Cholla on Summit"
date:   2019-02-35 17:10:24 -0800
categories: cholla
---


## Install FFTW ( Not Necessary Already installed on Summit )

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
./configure --disable-fortran --disable-shared --enable-openmp --with-fftw3=/autofs/nccs-svm1_sw/summit/.swci/1-compute/opt/spack/20180914/linux-rhel7-ppc64le/xl-16.1.1-1/fftw-3.3.8-vuwn274gfobnmpcr6d3bbualaqbj6nnc/ --prefix=/ccs/home/bvilasen/code/pfft
make -j 10
make install
```

## Insall HDF5

```
wget https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8/hdf5-1.8.21/src/hdf5-1.8.21.tar.gz
tar -xzvf hdf5-1.8.21.tar.gz
cd hdf5-1.8.21
CC=/usr/mpi/gcc/openmpi-3.1.3a1/bin/mpiCC ./configure --enable-parallel --prefix=/ccs/home/bvilasen/code/hdf5
