---
layout: page_main
title: Results
permalink: /results/
---


<div class="home">

  <h1 class="page-heading"></h1>

  <h1 class="main-title">  Main Research Results </h1>


  <br>
  <br>
  
  <ul class="post-list">
    {% for post in site.categories.results %}
      <li>
        <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>

        <h2>
          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        </h2>
      </li>
    {% endfor %}
  </ul>
  
  
</div>