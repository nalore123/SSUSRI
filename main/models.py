from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

# Create your models here.

class Novosti(models.Model):
    naslov = models.TextField()
    kratki_opis = models.TextField()
    glavna_slika = models.ImageField(upload_to ='novostislike/glavna')
    dugi_opis = models.TextField()
    datum_objave = models.DateTimeField(default=timezone.now)
    #ne znam ako mi ovo treba, to sam vidjela na ovoj str: https://philipodulaja.hashnode.dev/how-to-upload-multiple-images-with-django-rest-framework
    #ako sam dobro skuzila, naziv koji stavim, sprema se u url: https://www.w3schools.com/django/django_slug_field.php
    slug = models.CharField(max_length=80, blank=False, null=False, default="1")
    def save(self, *args, **kwargs):
        self.slug = slugify(self.naslov)
        super().save(*args, **kwargs)
    def __str__(self):
        return "%s" % (self.naslov)
    

class NovostiSlike(models.Model):
    novost  = models.ForeignKey(Novosti, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="novostislike/ostale")
    def __str__(self):
        return "%s" % (self.novost.naslov)
    
class Natjecanja(models.Model):
    datum_natjecanja=models.DateField()
    vrsta_natjecanja=models.CharField(max_length=120)
    def __str__(self):
        return self.vrsta_natjecanja

class Galerija(models.Model):
    naziv = models.CharField(max_length=200)
    def __str__(self):
        return self.naziv

class GalerijaSlike(models.Model):
    galerija = models.ForeignKey(Galerija, on_delete=models.CASCADE, related_name="images")
    slika = models.ImageField(upload_to="galerija/")
    def __str__(self):
        return self.galerija.naziv