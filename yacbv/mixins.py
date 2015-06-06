from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http.response import HttpResponseNotAllowed


class HttpMethodRestrictMixin(object):
    allowed_methods = [
        'options', 'get', 'head', 'post',
        'put', 'delete', 'trace', 'connect',
    ]

    def dispatch(self, request, *args, **kwargs):
        if self.method_name not in self.allowed_methods:
            return HttpResponseNotAllowed()

        super(HttpMethodRestrictMixin, self).dispatch(request, *args, **kwargs)


class TemplateMixin(object):
    """In this case, method must return dict, that is used to populate data
    in template"""
    template_name = None

    def dispatch(self, request, *args, **kwargs):
        context = super(TemplateMixin, self).dispatch(request, *args, **kwargs)

        return render_to_response(
            self.template_name,
            context,
            context_instance=RequestContext(self.request),
        )
