---
layout: post
title: "Effects of Rescaling on the P(k) "
date:   2021-04-10 08:00:24 -0800
categorines: cholla
---

The power spectrum is computed on the transmited flux fluctuations $$\delta_{F}$$, defines as: 

$$\delta_{F} \,=\, \frac{F- \overline{F} }{ \overline{F}} \,=\, \frac{F}{ \overline{F} } - 1  $$ 


### Rescaling The Transmitted Flux

If we rescale the Transmitted flux along the line of sight by a factor $$\alpha$$, then:


$$ F^\prime = \alpha F $$  
$$\overline{F^\prime} = \alpha  \overline{F} $$ 
$$\delta_{F}^\prime = \delta_{F} $$

Then, rescaling the Transmitted Flux has no effect on the Flux Power Spectrum  


### Rescaling The Optical Depth

Now, if instead we rescale the Optical Depth along the line of sight, such that:

$$\tau^\prime = \alpha \tau $$


$$ F^\prime = \mathrm{exp}( - \tau^\prime ) = \mathrm{exp}( - \alpha \tau  ) $$



#### Effects rescaling $$\tau$$ as a function of redshift

The effects for $$k > 0.1$$ are mostly scale independent 

<img src="{{ site.url }}assets/images/fig_rescaled_power_spectrum_25.png">
<img src="{{ site.url }}assets/images/fig_rescaled_power_spectrum_30.png">
<img src="{{ site.url }}assets/images/fig_rescaled_power_spectrum_35.png">
<img src="{{ site.url }}assets/images/fig_rescaled_power_spectrum_40.png">
<img src="{{ site.url }}assets/images/fig_rescaled_power_spectrum_45.png">
<img src="{{ site.url }}assets/images/fig_rescaled_power_spectrum_48.png">
<img src="{{ site.url }}assets/images/fig_rescaled_power_spectrum_50.png">
<img src="{{ site.url }}assets/images/fig_rescaled_power_spectrum_53.png">
<img src="{{ site.url }}assets/images/fig_rescaled_power_spectrum_55.png">
 
