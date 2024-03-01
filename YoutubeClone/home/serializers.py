from rest_framework import serializers
from . models import Youtubecl
class youtubeclSerializer(serializers.ModelSerializer):
    class Meta:
        model=Youtubecl
        fields='__all__'