from django.shortcuts import render
from main.models import *
from main.serializers import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class NovostiView(ModelViewSet):
    queryset = Novosti.objects.all()
    serializer_class = NovostiSerializer

class NatjecanjaView(ModelViewSet):
    queryset = Natjecanja.objects.all()
    serializer_class = NatjecanjaSerializer

class GalerijaView(ModelViewSet):
    queryset = Galerija.objects.all()
    serializer_class = GalerijaSerializer