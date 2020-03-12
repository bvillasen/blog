---
layout: post
title: "Summit Simulations Summary"
date:   2020-03-11 17:10:24 -0800
categories: dm cholla
---

This is the usage of Summit for project AST149


### Scaling Tests

For the Incite 2019 application we did several weak scaling tests:

All all full hydro + dm + chemistry simulations, we timed 3 versions for each n_GPUs: 128$$^3$$, 256$$^3$$ and 384$$^3$$ cells/particles per GPU  


* 3 x ( 2 nodes,  8 GPUs,  20 min each )
* 3 x ( 11 nodes,  64 GPUs,  20 min each )
* 3 x ( 86 nodes,  512 GPUs,  20 min each )  
* 3 x ( 342 nodes,  2048 GPUs,  20 min each )
* 3 x ( 683 nodes,  4096 GPUs,  20 min each )  
* 3 x ( 1366 nodes,  8192 GPUs,  20 min each ) 
* 3 x ( 2731 nodes,  16384 GPUs,  20 min each )  


### Cosmological Simulations

All Simulations: box=50 Mpc/h

Simulations that ran to z=0: 

* 1 x ( 86 nodes, 512 GPUs, 2.5 hrs ) 1024$$^3$$ hydro simulation, UVB=HM12
* 1 x ( 86 nodes, 512 GPUs, 2.5 hrs ) 1024$$^3$$ hydro simulation, UVB=PCHW19  


Simulations that ran to z=2: 

* 1 x ( 86 nodes, 512 GPUs, 4 hrs ) 2048$$^3$$ DM-Only simulation
* 1 x ( 86 nodes, 512 GPUs, 12 hrs ) 2048$$^3$$ hydro simulation, UVB=HM12
* 1 x ( 86 nodes, 512 GPUs, 12 hrs ) 2048$$^3$$ hydro simulation, UVB=PCHW19    
* 4 x ( 86 nodes, 512 GPUs, 12 hrs ) 2048$$^3$$ hydro simulation, UVB=PCHW19, Alternative Cosmologies


### Data Analysis

Analysis of simulation outputs performed in Large-Memory Nodes on Rhea ( I don't remember what was the usage here but my guess is that around 100-120 node hours, I left my token in the office, but if you need the exact usage I can go to my office later  ).


### Extra Stuff

Evan also used some time ( Don't remember how much exactly but I think around 2000 node-hours )
