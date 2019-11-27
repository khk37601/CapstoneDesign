from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #path('', views.post_list, name='post_list'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('', views.index),
    path('crawling', views.crawling),
    path('index1', views.index1),
    path('index2', views.index2),
    path('index3', views.index3),
    #path('post/new/', views.post_new, name='post_new'),
    #path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #path('', views.create, name='create'),
    #path('post/<int:pk>/', views._post, name='_post'),

]

