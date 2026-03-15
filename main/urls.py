from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path("novosti/", NovostiView.as_view()),
    path("natjecanja/", NatjecanjaView.as_view())
]