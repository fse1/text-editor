
from django.urls import path
from django.contrib.auth import views as auth_views
from django.templatetags.static import static
from . import views

app_name = 'text_editor'
urlpatterns = [
  path('', views.index, name='index'),
  path('editor/', views.editor, name='editor'),
  path('editor/get-posts/', views.posts, name='get-posts'),
  path('editor/add-post/', views.add_post, name='add_post'),
  path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='text_editor/login.html', extra_context={'basic_page': {'header_links': {'css': [static('text_editor/styles.css')], 'js': []}, 'title': 'Text Editor'}}), name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
