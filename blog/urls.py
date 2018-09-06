# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import path 
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
]