from django.conf.urls import patterns, url
from giganapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^papers/', views.papers, name='papers'),
    url(r'^figures/', views.figures, name='figures'),
    url(r'^tables/', views.tables, name='tables'),
    url(r'^paper/(?P<paper_short_name_url>\w+)/$', views.paper, name='paper'),
    url(r'^paper/(?P<paper_short_name_url>\w+)/workflow/(?P<workflow_name>\w+)/', views.workflow, name='paper'),
)