from urllib.parse import urljoin

from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from djproxy.views import HttpProxy


class ProxyView(HttpProxy):
    base_url = settings.PROXY_URL

    @property
    def proxy_url(self):
        return urljoin(self.base_url, self.request.path)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
