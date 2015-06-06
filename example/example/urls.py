from django.conf.urls import url

from test_views.views import IndexView, TestView, LoginRequiredView

urlpatterns = [
    url(r'^$', IndexView()),
    url(r'^test$', TestView()),
    url(r'^login_required$', LoginRequiredView()),
]
