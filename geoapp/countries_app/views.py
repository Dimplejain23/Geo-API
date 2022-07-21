from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Countries
from .serializers import CountrySerializer
from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers import serialize


@api_view(['GET'])
def get_all_countries(request):
    """
    Return all countries in table
    """
    countries = Countries.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_country(request,name):
    """
    Return country queried
    """
    try:
        country = Countries.objects.get(admin=name)
        serializer = CountrySerializer(country)
        return Response(serializer.data)
    except Countries.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_country(request):
    """
    Create a new country in table
    """
    data = request.POST.dict()
    serializer = CountrySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','POST'])
def update_country(request,name):
    """
    Update country in table
    """
    try:
        country = Countries.objects.get(admin=name)
    except Countries.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CountrySerializer(country, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_country(request,name):
    """
    Delete a country row in table
    """
    try:
        country = Countries.objects.get(admin=name)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Countries.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def search_country(request,name):
    """
    Return call countries which has query string matching with its name
    """
    try:
        country = Countries.objects.filter(admin__icontains=name)
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)
    except Countries.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def squery_by_geom(request,geom):
    """
    Perform spatial intersects by geometry
    """
    try:
        geom = GEOSGeometry(geom)
        country = Countries.objects.filter(geometry__intersects=geom)
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)
    except Countries.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def spatial_query_country(request,name):
    """
    Perform spatial intersects by geometry of the queried country
    """
    try:
        country = Countries.objects.get(admin=name)
        data = Countries.objects.filter(geometry__intersects=country.geometry)
        serializer = CountrySerializer(data, many=True)
        return Response(serializer.data)
    except Countries.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)