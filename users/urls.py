"""URLs for users"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views


app_name = "users"

urlpatterns = [

    #Login page
    url(r'^login/$', login, {'template_name' :'users/login.html'},
        name='login'),
    #Logout
    url(r'^logout/$', views.logout_view, name='logout'),
    #Register
    url(r'^register/$', views.register, name='register'),
    #Activate
    #url(r'^activate/(?P<uid64>[0-9A-Za-z_\-]+/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z{1,20})/$',views.activate, name='activate'),
    url(r'^activate/(?P<pk>[0-9]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate')
]
