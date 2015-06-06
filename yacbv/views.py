from .mixins import TemplateMixin


class View(object):
    def __call__(self, request, *args, **kwargs):
        return self.dispatch(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.method_name = self.request.method.lower()
        method = getattr(self, self.method_name, self._not_implemented)

        return method(*args, **kwargs)

    def _not_implemented(self):
        raise NotImplementedError(
            '\'%s.%s\' method is not implemented.' % (
                self.__class__.__name__,
                self.method_name,
            ),
        )


class TemplateView(TemplateMixin, View):
    """In this case, method must return dict, that is used to populate data
    in template"""
    pass
