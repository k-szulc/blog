"""URLs for blogs"""

from django.conf.urls import url

from . import views

app_name = "blogs"

urlpatterns = [

    #Home
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post')

]
