from django.contrib.gis.db import models

# Schema for countries table
class Countries(models.Model):
    id = models.BigAutoField(primary_key=True)
    admin = models.TextField( blank=True, null=True)  
    iso_a3 = models.TextField( blank=True, null=True)  
    geometry = models.GeometryField(blank=True, null=True)
