
from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.index, name="BlogHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogPost"),
]

