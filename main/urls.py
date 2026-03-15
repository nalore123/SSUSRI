from django.urls import path, include
from main.views import *
from rest_framework import routers
from . import views
app_name = 'main'

router = routers.DefaultRouter()
router.register(r'novosti', views.NovostiView)
router.register(r'natjecanja', views.NatjecanjaView)
router.register(r'galerija', views.GalerijaView)


urlpatterns = [
    path('', include(router.urls)),

]