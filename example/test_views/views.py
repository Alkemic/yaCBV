from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from yacbv.views import View, TemplateView
from yacbv.decorators import class_decorator


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self):
        return {'variable': 'I\' a variable'}


class TestView(View):
    def get(self):
        return HttpResponse('test', content_type='text/plain')


@class_decorator(login_required)
class LoginRequiredView(View):
    def get(self):
        return HttpResponse('logged in', content_type='text/plain')
