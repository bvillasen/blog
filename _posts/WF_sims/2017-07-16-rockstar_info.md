---
layout: post
title:  "ROCKSTAR summary"
date:   2017-07-25 17:10:24 -0800
categories: cosmology wfirst
---

### From ROCKSTAR paper:

>As a first step, our algorithm performs a rapid variant of the 3D friends-of-friends (FOF) method to find overdense regions which are then distributed among processors for analysis. Then, it builds a hierarchy of FOF subgroups in phase space by progressively and adaptively reducing the 6D linking length, so that a tunable fraction of particles are captured at each subgroup as compared to the immediate parent group. Next, it converts this hierarchy of FOF
groups into a list of particle memberships for halos.It then computes the host halo/subhalo relationships among halos, using information from the previous timestep if available. Finally, it removes unbound particles from halos
and calculates halo properties, before automatically generating particle-based merger trees (§3.5). A visual summary of
these steps is shown in Fig. 1.

<img src="{{ site.url }}assets/images/rks_1.png">

1. Performs a rapid variant of the 3D friends-of-friends (FOF) method to find overdense regions which are then distributed among processors for analysis.

2. For each 3D FOF group which is created in the previous step, the algorithm proceeds by building a hierarchy of FOF subgroups in phase space. Deeper levels of subgroups have a tighter linking-length criterion in phase space, which means
that deeper levels correspond to increasingly tighter isodensity contours around peaks in the phase-space density distribution. This enables an easy way to distinguish separate substructures — above some threshold phase-space density, their particle distributions must be distinct in phase space; otherwise, it would be difficult to justify the separation into different structures.
Beginning with a base FOF group, ROCKSTAR adaptively chooses a phase-space linking length based on the standard deviations of the particle distribution in position and velocity space. That is, for two particles p 1 and p 2 in the base group, the phase-space distance metric is defined as:

$$ d( p_{1}, p_{2} ) = \bigg( \frac{ |\vec{x_{1}} - \vec{x_{2}}|^{2} }{\sigma_{x}^2} + \frac{ |v_{1} - v_{2}|^{2} }{\sigma_{v}^2} \bigg)^{1/2} $$

where $$\sigma_x$$ and $$\sigma_y$$ are the particle position and velocity dispersions for the given FOF group; this is identical to the metric of
Gottlöber (1998). For each particle, the distance to the nearest neighbor is computed; the phase-space linking length is then chosen such that a constant fraction f (f=0.7) of the particles are linked together with at least one other particle. In large groups (>10,000 particles), where computing the nearest neighbor for all particles can be very costly, the nearest neighbors are only
calculated for a random 10,000-particle subset of the group, as this is sufficient to determine the linking length to reasonable precision.
Once subgroups have been found in the base FOF group, this process is repeated. For each subgroup, the phase-space metric is recalculated, and a new linking-length is selected such that a fraction f of the subgroup’s particles are linked together into sub-subgroups. Group finding proceeds hierarchically in phase space until a predetermined minimum number of particles remain at the deepest level of the hierarchy. Here we set this minimum number to 10 particles, although halo properties are not robust approaching this minimum.



$$ d( h, p ) = \bigg( \frac{ |\vec{x_{h}} - \vec{x_{p}}|^{2} }{r_{dyn}^2 }+ \frac{ |\vec{v_{h}} - \vec{v_{p}}|^{2} }{\sigma_{v}^2} \bigg)^{1/2} $$

$$ r_{dyn} = \frac{v_{max}}{\sqrt{ \frac{4}{3} \pi G \rho_{vir}}} $$


* Halo masses at several radii: Mvir, M200b, M200c, M500c, M2500c. These masses always include any contributions from substructure. Also, masses with higher density thresholds (e.g., 2500c) can sometimes be zero if the density of the halo never rises above the threshold. [Footnote: Particles are assumed to have an effective radius of FORCE_RES for the purposes of density calculations near the halo center.} By default, only bound particles are included; see Section \ref{s:common_options] if this is not what you want.
* Halo maximum circular velocity and velocity dispersion.
* Halo radii: Rvir and the scale radius r_s, calculated both using profile fitting and using the Klypin v_max method.
* Halo center positions and velocities.
* Halo spin (both Bullock and Peebles) and angular momentum.
* Halo shapes and principal axes, using the Allgood method (iterative, weighted by 1/r^2), at both Rvir and R500c. See Section 2.11.1 for how to change the shape calculation method.
* The ratio of halo kinetic to potential energy, and the center position and velocity offsets from the halo's bulk average position and velocity.

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
