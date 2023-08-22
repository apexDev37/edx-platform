from django.urls import path
from .views import CustomIDAResponseView

app_name = 'custom-ida'

urlpatterns = [
  path('customida/', CustomIDAResponseView.as_view(), name='custom-ida')
]
