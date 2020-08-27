
from django.urls import path
from . import views

app_name = 'text_editor'
urlpatterns = [
  path('editor/', views.editor, name='editor'),
  path('editor/get-posts/', views.posts, name='get-posts'),
  path('editor/add-post/', views.add_post, name='add_post'),
]
