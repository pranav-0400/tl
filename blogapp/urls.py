from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('<str:slug>', views.blog_detailView, name = 'blog_detail')
]


