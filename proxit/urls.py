from django.urls import re_path

from .views import ProxyView

urlpatterns = [
    re_path(r'^.*$', ProxyView.as_view(), name='proxy'),
]
