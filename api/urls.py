from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.ping, name='test'),
    url(r'^jokes/$', views.JokeListView.as_view(), name='joke_list'),
    url(r'^jokes/(?P<pk>[0-9]+)/$', views.JokeDetailView.as_view(), name='joke_detail'),
]
