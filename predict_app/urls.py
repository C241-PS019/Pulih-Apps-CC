from django.urls import path
from .views import StressPredictionView

urlpatterns = [
    path('predict/', StressPredictionView.as_view(), name='predict'),
]