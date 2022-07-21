from rest_framework import serializers
from .models import Countries

# Country data serializer
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ('id','admin','iso_a3','geometry')