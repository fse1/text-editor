
from django.http import HttpResponse
from django.shortcuts import render
from django.templatetags.static import static
from django.views.decorators.csrf import csrf_exempt

def editor(request):
  basic_page = {'header_links': {'css': [static('text_editor/styles.css')], 'js': []}, 'title': 'Text Editor'}
  react_page = {'id': 'editor-app', 'bottom_js_links': [static('text_editor/editor-bundle.js')]}
  template_context = {'basic_page': basic_page, 'react_page': react_page}
  
  return render(request, 'text_editor/react_app_injection.html', template_context)

def posts(request):
  template_context = {}
  
  return render(request, 'text_editor/get_posts.json', template_context)

@csrf_exempt
def add_post(request):
  template_context = {}
  
  return render(request, 'text_editor/add_post.json', template_context)