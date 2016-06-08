Title: My First Test Post
Date: 2016-06-02 17:34
Category: review
gallery: test

Following is the text of my first test post

<h2><a href="{{ SITEURL }}/pages/gallery.html#{{ article.album }}">{{ article.album }}</a></h2>
    <ul>
    {% for image in article.galleryimages %}
    <li><a class="{{ article.album }} cboxElement" href="{{ SITEURL }}/static/images/gallery/{{ article.album }}/{{ image }}"><img src="{{ SITEURL }}/static/images/gallery200x200/{{ article.album }}/{{ image }}"></a></li>
    {% endfor %}
    </ul>
