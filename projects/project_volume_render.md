---
layout: page
permalink: /projects/volume_render/
---

<h2> Volume Render </h2>

<h1>A GPU accelerated pyCUDA/pyOpenGL ray-tracing based 3D visualization tool.</h1> 


[GitHub Repositoty: https://github.com/bvillasen/volumeRender](https://github.com/bvillasen/volumeRender)

[GitHub Repository: https://github.com/bvillasen/isingModel](https://github.com/bvillasen/isingModel)

I believe that visualization plays a very important role in understanding the physical phenomena that we study by using computers to numerically solve the equations that govern their evolution, this motivated me to apply my knowledge of GPU computing and visualization to develop a 3D volume render that I could use to visualize the physics that I was solving.

For this project I used **pyCUDA** to call CUDA kernels from python and run a ray-tracing algorithm over some volumetric data, then I used **pyOpenGL** to display the generated image and to record mouse or keyboard events, this allowed the user to interact with the simulation in real time. As a simple example, the animation bellow shows a 3D simulation of the "Ising Model" which is used to represent the orientations of the magnetic dipoles of atoms in  ferromagnetic materials, in this representation, the atomic "spins" can be in one of two states: pointing up or pointing down, the two states are represented as different colors in the visualization. Because of the thermal excitation of the material, each spin can change orientation whit a probability that increases with temperature, this means that when the temperature is low then the spins will tend to orient themselves and this will create a net magnetic field. In contrast, when the temperature increases the spins will start changing orientation randomly so that there is no net magnetic field.


<div style="text-align: center">
<video src="{{ site.url }}assets/videos/ising_3D.mp4" width="100%"  height="auto" controls preload> </video>
</div>

The animation above shows the Ising model for a 3D volume of 512$$^3$$ individual spins. I produced the animation by recording my screen as the simulation is running, as it can be seen I can interact with the simulation by rotating the simulated cube with my mouse, also I can control the variables shown, first it shows both spin orientation, then each orientation is shown individually and then at the end I increase the temperature beyond the critical temperature for which the material losses it's net magnetism due to the random orientations of the atomic spins.   

