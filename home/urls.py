from django.contrib import admin
from django.urls import path,include
from home import views


admin.site.site_header = "Login"
admin.site.site_title = "Welcome to Sakshi's Dashboard"
admin.site.index_title = "Welcome"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('projects', views.projects, name='projects')
]
