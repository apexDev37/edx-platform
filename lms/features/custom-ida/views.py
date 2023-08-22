from django.http import JsonResponse
from openedx.core.djangoapps.content.views.base import BaseView

class CustomIDAResponseView(BaseView):
  def greet(self, request, *args, **kwargs):
    payload = {'message': 'Welcome to Open edX!'}
    return JsonResponse(payload)
