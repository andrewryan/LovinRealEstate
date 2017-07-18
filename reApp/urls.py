from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^email/$', views.email, name='email'),
    # url(r'^home/$', views.home, name='home'),
    url(r'^success/$', views.success, name='success'),
]
