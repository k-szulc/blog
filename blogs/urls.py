"""URLs for blogs"""

from django.conf.urls import url

from . import views

app_name = "blogs"

urlpatterns = [

    #Home
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post'),
    url(r'^new_post/$', views.new_post, name='new_post'),
    url(r'^edit_post/(?P<post_id>\d+)/$', views.edit_post, name='edit_post'),

]
