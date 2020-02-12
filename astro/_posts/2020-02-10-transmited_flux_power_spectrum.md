---
layout: post
title:  "Transmitted Flux Power Spectrum"
date:   2020-02-10 17:10:24 -0800
categories: gas cholla
---

The input to the Flux Power Spectrum  is then flux as function of velocity, i.e. F (v), over some
velocity interval $$V$$ (in the data set this interval is chosen so that
one avoids the Lyman-$$\beta$$ forest, the quasar near zone, and potentially some strong absorbers; in the simulations it is set by the linear
extent of the simulated volume).


The FPS is written in terms of the dimensionless variance $$\Delta_F^2(k)$$ (strictly speaking a variance in $$\delta_F$$ per dex in $$k$$), defined by

$$\Delta_{F}^{2}(k)=\frac{1}{\pi} k P_{F}(k) $$

$$P_{F}(k)=V  \bigg \langle  \left|\tilde{\delta}_{F}(k)\right|^{2}  \bigg \rangle $$

$$\tilde{\delta}_{F}(k)=\frac{1}{V} \int_{0}^{V} d v e^{-i k v} \delta_{F}(v)$$