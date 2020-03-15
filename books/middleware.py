from django.http import HttpResponse
from django.shortcuts import render

class BookMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        return HttpResponse('<h1>Response from Process View<h1>')

    def process_exception(self, request, exception):
        return HttpResponse('<h1>Response from Process Exception<h1>')

    def process_template_response(self, request, response):
        if hasattr(response, 'home.html'):
            return render(request, 'response.html')
