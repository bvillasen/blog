---
layout: post
title:  "CHOLLA_PM: Dual energy Updated"
date:   2019-03-20 17:10:24 -0800
categories: cholla
---

First Column:  ENZO

Second Column: CHOLLA CHOLLA PREVIOUS DE METHOD: using  physical internal energy $$ ge_{tot} $$ when $$  ge_{tot}/E > 0.02  $$  and $$ E_{kin} > 0.4 \overline{E_{kin}} $$

Third Column: CHOLLA PREVIOUS DE METHOD:  using  physical internal energy $$ge_{tot}$$ when $$  ge_{tot}/E > 0.02  $$

Forth Column: CHOLLA  UPDATED DUAL ENERGY METHOD: pressure computed from physical internal energy ( $$ge_{tot}$$ ) when  $$  ge_{tot}/E > 0.02  $$ and pressure computed from advected internal_energy otherwise.

<div style="text-align: center">
<video src="{{ site.url }}assets/videos/phase_diagram_pressureDE.mp4" width="500" height="500" controls preload> </video>
</div>