from django.urls import path
from .views.landing import LandingViewSet

urlpatterns = [
    path('', LandingViewSet.show ),
]