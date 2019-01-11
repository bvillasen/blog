---
layout: page
permalink: /ay9project/posts/
---


<div class="home">

  <h1 class="page-heading"></h1>

  <font size="6" color="#147BA8">
  Analysis of Dark Matter Simulations
  </font>

  <br>
  <br>

  <font size="6" color="#147BA8">
  Posts for the Project:
  </font>

  <br>
  <br>
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
