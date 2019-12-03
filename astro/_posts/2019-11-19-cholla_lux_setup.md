---
layout: post
title:  "Cholla: Lux Setup"
date:   2019-11-19 17:10:24 -0800
categories: dm 
---

## Install FFTW

Download FFTW from [HERE](http://www.fftw.org/download.html)

```
./configure --prefix=/data/groups/comp-astro/bruno/code/fftw --enable-mpi --enable-openmp --enable-threads --disable-shared 
make 
make install
```

## Install PFFT