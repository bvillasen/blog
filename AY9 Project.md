---
layout: page
title: AY9 Project
permalink: /ay9project/
---


<div class="home">

  <h1 class="page-heading"></h1>

  <font size="6.5" color="#4286f4">
  Analysis of Dark Matter Simulations
  </font>

  <a href="https://github.com/bvillasen/AY9_dark_matter_analysis" > Project GitHub Repository </a>

  <ul class="post-list">
    {% for post in site.categories.ay9 %}
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
