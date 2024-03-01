

from rest_framework.generics import ListAPIView,ListCreateAPIView
from . serializers import youtubeclSerializer
from .models import Youtubecl

# Create your views here.

class Youtubecvlview(ListCreateAPIView):
    queryset=Youtubecl.objects.all()
    serializer_class=youtubeclSerializer


