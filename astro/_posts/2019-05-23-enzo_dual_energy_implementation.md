---
layout: post
title:  "Enzo: Dual Energy Implementation"
date:   2019-05-23 17:10:24 -0800
categories: cholla
---

This are the files I have found in Enzo that are relevant for the Dual Energy Implementation:

**src/enzo/hydro_rk/Grid_UpdatePrim.C**   lines 288 - 320 

```
if (DualEnergyFormalism) {
  v2 = vx*vx + vy*vy + vz*vz;
  eint = Eint_new/D_new;
  float eint_du = eint;
  float eint1 = etot - 0.5*v2;
        float emin = SmallT/(Mu*(Gamma-1.0));
  //float emin = 4.0*0.48999*D_new*pow(CellWidth[0][0],2)/(Gamma*(Gamma-1.0));

  if (eint1 > 0) {
    EOS(p, D_new, eint1, h, cs, dpdrho, dpde, EOSType, 2);
  }
  else {
    cs = 0.0;
  }
  if (cs*cs > DualEnergyFormalismEta1*v2 && eint1 > 0.5*eint) {
    eint = eint1;
  }
  eint = max(eint, emin);
  BaryonField[GENum][igrid] = eint;
  BaryonField[TENum][igrid] = eint + 0.5*v2;
}  
```