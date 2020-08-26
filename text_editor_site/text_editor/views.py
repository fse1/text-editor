
from django.http import HttpResponse
from django.shortcuts import render
from django.templatetags.static import static

def editor(request):
  basic_page = {'header_links': {'css': [], 'js': []}, 'title': 'Text Editor'}
  react_page = {'id': 'editor-app', 'bottom_js_links': []}
  template_context = {'basic_page': basic_page, 'react_page': react_page}
  
  return render(request, 'text_editor/react_app_injection.html', template_context)
