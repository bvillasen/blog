---
layout: post
title: "Flux Power Spectrum Comparison to Data Quantified "
date:   2020-09-01 10:10:24 -0800
categorines: dm cholla
---

Figures below show the differences in the Flux Power Spectrum measured in our simulations compared to the observational data. The differences are quantified by $$\chi^2$$ defined as:

$$  \chi^{2} = \sum_{i}^N \left[ \frac{ P(k_i)^{\mathrm{observ}} - P(k_i)^{\mathrm{model}} } { \sigma_i^{\mathrm{observ}} }  \right]^{2}  $$




The errors $$\Delta_{\mathrm{P19}}$$ and $$\Delta_{\mathrm{HM12}}$$ shown in the figures for each snapshot are computed as:


$$\Delta =  \frac{ \sqrt{ \chi^2 } }{ N }  $$ 

<img src="{{ site.url }}assets/images/fps_comparison_boss.png">


For the small scale  comparison the scales selected are $$ 0.01 \leq k \leq 0.1 \, \mathrm{s} \, \mathrm{km}^1 $$ and the measurements of $$\chi^2$$ is computed separately for each of the observational data sets. 

<img src="{{ site.url }}assets/images/fps_comparison.png">
