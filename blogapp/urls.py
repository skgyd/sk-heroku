from django.contrib import admin
from django.urls import path, include
from . import views
import blogapp.views

urlpatterns = [
    path('<int:blog_id>/',views.detail,name='detail'),
    #path('new/',views.new, name='new'),
    path('create/',views.create, name='create'),
    path('<int:blog_id>/delete/',views.delete,name='delete'),
    path('<int:blog_id>/edit/',views.edit,name='edit'),
    path('<int:blog_id>/update/',views.update,name='update'),
    path('<int:blog_id>/comments/',views.add_comment,name='add_comment'),
    path('newblog/',views.blogpost,name='newblog'),
    path('delete_comment/<int:comment_id>/' , views.delete_comment, name = 'delete_comment'),
    path('edit_comment/<int:comment_id>/' , views.edit_comment, name = 'edit_comment'),
]

