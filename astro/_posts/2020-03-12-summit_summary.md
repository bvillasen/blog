---
layout: post
title: "Summit Simulations Summary"
date:   2020-03-11 17:10:24 -0800
categories: dm cholla
---

This is the usage of Summit for project AST169


### Scaling Tests

For the Incite 2019 application we did several weak scaling tests:

All all full hydro + dm + chemistry simulations, we timed 3 versions for each n_GPUs 128$$^3$$, 256$$^3$$ and 384$$^3$$ cells/particles per GPU  


* 3 x ( 2 nodes,  8 GPUs,  20 min each )
* 3 x ( 11 nodes,  64 GPUs,  20 min each )
* 3 x ( 86 nodes,  512 GPUs,  20 min each )  
* 3 x ( 342 nodes,  2048 GPUs,  20 min each )
* 3 x ( 683 nodes,  4096 GPUs,  20 min each )  
* 3 x ( 1366 nodes,  8192 GPUs,  20 min each ) 
* 3 x ( 2731 nodes,  16384 GPUs,  20 min each )  


### Cosmological Simulations

