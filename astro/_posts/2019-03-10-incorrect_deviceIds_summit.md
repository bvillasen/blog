---
layout: post
title:  "CHOLLA_PM: Incorrect device Ids on summit"
date:   2019-03-10 17:10:24 -0800
categories: cholla
---

When I run a small simulation on Summit, sometimes it will run the first timesteps correctly but some other times the data on the GPU arrays would be completely corrupted even before before cuda functions are called. This behavior seems unpredictable since it works sometimes and other times it doesn't without changing the code.

I found that the gpus are not been assigned correctly to the MPI processes.

<img src="{{ site.url }}assets/images/device_ids">




Here is an output file of a successful run:

https://www.dropbox.com/s/9111368dlx15xg1/run_output_good.log?dl=0

Here is an output file of a failed run:

https://www.dropbox.com/s/4br0dw5vuaie0qs/run_output_bad.log?dl=0


