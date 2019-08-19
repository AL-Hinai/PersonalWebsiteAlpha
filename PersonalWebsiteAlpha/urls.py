from django.conf.urls import url 
from PersonalWebsiteAlpha import views

urlpatterns = [ 
    url(r'^$', views.index, name='index'), 
]