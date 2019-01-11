---
layout: page
title: AY9-Project
permalink: /ay9project/
---


<div class="home">

  <h1 class="page-heading">AY9 Project: Analysis of Dark Matter Simulations A</h1>

  <ul class="post-list">
    {% for post in site.ay9posts %}
      <li>
        <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>

        <h2>
          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        </h2>
      </li>
    {% endfor %}
  </ul>

  <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>

</div>
