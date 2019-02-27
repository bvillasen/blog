---
layout: post
title:  "CHOLLA_PM: Install Colla on Summit"
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
```
