from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<str:article_id>', detail, name ="detail"),
    path('new/', new, name = "new"),
    path('edit/<str:article_id>', edit, name = "edit"),
    path('delete/<str:article_id>', delete, name = "delete"),
    path('search', search, name='search'),
    path('create_comment/<str:article_id>', create_comment, name="create_comment"),
    path('create_re_comment/<int:article_id>/<str:comment_id>', create_re_comment, name="create_re_comment"),
    path('delete_comment/<int:article_id>/<int:comment_id>', delete_comment, name="delete_comment")
]