
from django.urls import path
from . import views

app_name = 'text_editor'
urlpatterns = [
  path('editor/', views.editor, name='editor'),
]
