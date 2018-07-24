from django.urls import path, include
from .views.api.candidates import CandidateListCreate

urlpatterns = [
    path('api/candidates/', CandidateListCreate.as_view() ),
]