---
layout: post
title:  "Gadget Errors"
date:   2017-07-29 17:10:24 -0800
categories: cosmology wfirst
---

Gadget parameters file [Here](https://github.com/bvillasen/blog/blob/master/assets/files/test_1024.param)

Gadget output failed run [Here](https://github.com/bvillasen/blog/blob/master/assets/files/output_1024_fft512_has)

For succesful run the next output from gadget is:

----------------------------------------------------------------------------------------------------------------

domain decomposition...
NTopleaves= 32768
work-load balance=1.01394   memory-balance=1.01394
exchange of 0133952850 particles
exchange of 0002343460 particles
domain decomposition done.
begin Peano-Hilbert order...
Peano-Hilbert done.
Begin Ngb-tree construction.
Ngb-Tree contruction finished

Setting next time for snapshot file to Time_next= 0.01

----------------------------------------------------------------------------------------------------------------




Error File [Here](https://github.com/bvillasen/blog/blob/master/assets/files/cosmo_1024_fft512_has.e2244885)

Output File [Here](https://github.com/bvillasen/blog/blob/master/assets/files/cosmo_1024_fft512_has.o2244885)








**Update**

Got same error when running on 64 nodes * 16 cores

Now running in 32 nodes * 16 cores: max_wall_time 120hrs,   

The $512^3$ simulation took 10hrs to run in 32 nodes*16cores
