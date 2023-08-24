from django.urls import path
from .views import CustomIDAResponseView

app_name = 'custom_ida'

urlpatterns = [
  path('api/v1/welcome/', CustomIDAResponseView.as_view(), name='custom_ida')
]
