from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from main.models import *
from main.serializers import *
# Create your views here.

class NovostiView(CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = NovostiSerializer

class NatjecanjaView(CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = NatjecanjaSerializer

class GalerijaView(CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = GalerijaSerializer