from rest_framework.views import APIView
from rest_framework.response import Response

class CustomIDAResponseView(APIView):
  def get(self, request, *args, **kwargs):
    payload = {'message': 'Welcome to Open edX!'}
    return Response(payload)
