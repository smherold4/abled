from rest_framework import serializers
from app.models import Candidate
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id', 'first_name', 'last_name', 'email', 'created_at')