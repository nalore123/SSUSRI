from django.contrib import admin
from .models import *

# Register your models here.

model_list = [Novosti, NovostiSlike, Natjecanja]

admin.site.register(model_list)