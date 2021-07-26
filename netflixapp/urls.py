from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<str:article_id>', detail, name ="detail"),
    path('new/', new, name = "new"),
    path('edit/<str:article_id>', edit, name = "edit"),
    path('delete/<str:article_id>', delete, name = "delete"),
    path('search', search, name='search'),
]