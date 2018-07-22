from django.urls import path, include
from . import views

urlpatterns = [
    path('api/candidate/', views.CandidateListCreate.as_view() ),
]