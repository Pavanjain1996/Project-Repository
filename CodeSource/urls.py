from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from CodeSource.models import Console, Desktop, Web, Python

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^Home/$',views.home,name='home'),
    url(r'^About/$',views.about,name='about'),
    url(r'^Projects/$',views.projects,name='projects'),
    url(r'^Videos/$',views.videos,name='videos'),
    url(r'^Console/$',ListView.as_view(queryset = Console.objects.all().order_by("name"),template_name='CodeSource/List.html')),
    url(r'^Console/(?P<pk>\d+)$',DetailView.as_view(model=Console,template_name='CodeSource/Play.html')),
    url(r'^Desktop/$',ListView.as_view(queryset = Desktop.objects.all().order_by("name"),template_name='CodeSource/List.html')),
    url(r'^Desktop/(?P<pk>\d+)$',DetailView.as_view(model=Desktop,template_name='CodeSource/Play.html')),
    url(r'^Web/$',ListView.as_view(queryset = Web.objects.all().order_by("name"),template_name='CodeSource/List.html')),
    url(r'^Web/(?P<pk>\d+)$',DetailView.as_view(model=Web,template_name='CodeSource/Play.html')),
    url(r'^Python/$',ListView.as_view(queryset = Python.objects.all().order_by("name"),template_name='CodeSource/List.html')),
    url(r'^Python/(?P<pk>\d+)$',DetailView.as_view(model=Python,template_name='CodeSource/Play.html')),
]
