---
layout: page_main
title: Projects
permalink: /projects/
---


<div class="home">

  <h3 class="page-heading">Projects</h3>

  <ul class="post-list">
    {% for post in site.categories.projects %}
      <li>
        <!-- <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span> -->

        <h2>
          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        </h2>
      </li>
    {% endfor %}
  </ul>

</div>

<!-- ### Main projects that I had worked on:
  
* <a href="{{ site.url }}projects/cholla/"  > CHOLLA: Large Scale Cosmological Hydrodynamical Simulations on Multiple GPUs  </a>

* <a href="{{ site.url }}projects/quantum_turbulence/"  > Quantum Turbulence 2 </a>

* <a href="{{ site.url }}projects/volume_render/"  > Volume Render  </a> -->
