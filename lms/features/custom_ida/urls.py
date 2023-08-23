from django.urls import path
from .views import CustomIDAResponseView

app_name = 'custom_ida'

urlpatterns = [
  path('customida/', CustomIDAResponseView.as_view(), name='custom_ida')
]
