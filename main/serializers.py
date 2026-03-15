from rest_framework import serializers

from main.models import *

class NovostiSlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NovostiSlike
        fields = "__all__"
    
class NovostiSerializer(serializers.ModelSerializer):
    images =  NovostiSlikeSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )
    class Meta:
        model = Novosti
        fields = "__all__"
    
    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        novost = Novosti.objects.create(**validated_data)

        for image in uploaded_images:
            NovostiSlike.objects.create(novost=novost, image=image)

        return novost 

class NatjecanjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Natjecanja
        fields = "__all__"

class GalerijaSlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalerijaSlike
        fields = "__all__"

class GalerijaSerializer(serializers.ModelSerializer):
    images =  GalerijaSlikeSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )
    class Meta:
        model = Galerija
        fields = "__all__"
    
    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        galerija = Galerija.objects.create(**validated_data)

        for image in uploaded_images:
            GalerijaSlike.objects.create(galerija=galerija, slika=image)

        return galerija 

