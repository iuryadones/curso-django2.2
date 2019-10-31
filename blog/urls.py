from django.urls import path
from . import views


blog_urls = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/data/', views.current_datetime, name='datetime'),
    path('blog/contato/', views.contact, name='contact'),
]
