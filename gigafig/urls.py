from django.conf.urls import patterns, url
from gigafig import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^papers/', views.papers, name='papers'),
    url(r'^figures/', views.figures, name='figures'),
    url(r'^tables/', views.tables, name='tables'),
    url(r'^paper/(?P<paper_short_name_url>\w+)/$', views.paper, name='paper'),
    url(r'^paper/(?P<paper_short_name_url>\w+)/workflow/(?P<workflow_name>\w+)/', views.workflow, name='paper'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^files/', views.files, name='files'),
    url(r'^galaxy2cytoscape/$', views.galaxy2cytoscape, name='galaxy2cytoscape'),

)