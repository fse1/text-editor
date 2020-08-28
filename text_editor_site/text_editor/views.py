
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from text_editor.models import Post


def index(request):
  return redirect('text_editor:editor')

@require_http_methods(["GET", "HEAD"])
def editor(request):
  if not request.user.is_authenticated:
    return redirect('text_editor:login')
    
  basic_page = {'header_links': {'css': [static('text_editor/styles.css')], 'js': []}, 'title': 'Text Editor'}
  react_page = {'id': 'editor-app', 'bottom_js_links': [static('text_editor/editor-bundle.js')]}
  template_context = {'basic_page': basic_page, 'react_page': react_page}
  
  return render(request, 'text_editor/react_app_injection.html', template_context)

@require_http_methods(["GET", "HEAD"])
def posts(request):
  if not request.user.is_authenticated:
    return HttpResponse('Forbidden', status=403)
  
  posts = Post.objects.filter(user_id=request.user.id).order_by('-creation_time')
  post_list = []
  for post in posts:
    post_dict = {'id': post.pk, 'creation_time': post.creation_time, 'content': post.content}
    post_list.append(post_dict)
  
  template_context = {'user': {'name': request.user.get_username()}, 'links': {'create_post': reverse('text_editor:add_post'), 'logout': reverse('text_editor:logout')}, 'posts': post_list}
  
  return render(request, 'text_editor/get_posts.json', template_context)

@require_http_methods(["POST"])
@csrf_exempt
def add_post(request):
  if not request.user.is_authenticated:
    return HttpResponse('Forbidden', status=403)
  
  new_post = Post(content=request.POST['post-content'], user=request.user)
  new_post.save()
  
  template_context = {'id': new_post.pk, 'creation_date': new_post.creation_time, 'content': new_post.content}
  
  return render(request, 'text_editor/add_post.json', template_context)
