from django.shortcuts import render

# Create your views here.
from app.models import Candidate
from app.serializers import CandidateSerializer
from rest_framework import generics
class CandidateListCreate(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer