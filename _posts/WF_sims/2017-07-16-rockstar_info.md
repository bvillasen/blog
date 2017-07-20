---
layout: post
title:  "ROCKSTAR summary"
date:   2017-07-19 17:10:24 -0800
categories: cosmology wfirst
---

```c++
double vir_density(double a) {
  double x = (Om/pow(a,3))/pow(hubble_scaling(1.0/a-1.0),2.0) - 1.0;
  return ((18*M_PI*M_PI + 82.0*x - 39*x*x)/(1.0+x));
}
```


```c++
float _calc_mass_definition(char **md) {
  int64_t length = strlen(*md);
  char last_char = (length) ? md[0][length-1] : 0;
  float matter_fraction = (Om/pow(SCALE_NOW,3))/pow(hubble_scaling(1.0/SCALE_NOW-1.0),2.0);
  float cons = Om * CRITICAL_DENSITY / PARTICLE_MASS; // background density
  char *mass = *md;
  float thresh_dens;
  if (mass[0] == 'm' || mass[0] == 'M') mass++;

  if (last_char == 'b' || last_char == 'B')
    thresh_dens = atof(mass) * cons;
  else if (last_char == 'c' || last_char == 'C')
    thresh_dens = atof(mass) * cons / matter_fraction;
  else {
    if (strcasecmp(*md, "vir")) *md = "vir";
    thresh_dens = vir_density(SCALE_NOW) * cons;
  }
  particle_rvir_dens_z0 = vir_density(1.0) * cons;
  return thresh_dens;
}
```
