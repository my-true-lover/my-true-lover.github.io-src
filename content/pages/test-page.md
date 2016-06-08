Title: Gallery
Date: 2016-06-07 17:34
template: gallery

Following is the text of my first test page

{% for album, images in page.gallery.iteritems() %}
<h2><a name="{{ album }}">{{ album }}</a></h2>
<ul>
    {% for image in images %}
    <li><a class="{{ album }} cboxElement" href="{{ SITEURL }}/static/images/gallery/{{album}}/{{ image }}" title="{{ image }}"><img src="{{ SITEURL }}/static/images/gallery200x200/{{album}}/{{ image }}"></a></li>
    {% endfor %}
</ul>
{% endfor %}
