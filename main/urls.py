from django.urls import path
from main import views
urlpatterns=[
    path('/home',views.index, name='home'),
    path('/projects',views.projects,name='projects'),
    path('/languages',views.languages,name='languages'),
    path('',views.index,name='home')
]