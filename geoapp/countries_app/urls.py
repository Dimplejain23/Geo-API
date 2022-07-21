from django.urls import path,re_path
from . import views
urlpatterns = [
      path('create/', views.create_country, name='create-country'),
      path('fetchall/', views.get_all_countries, name='get-all-countries'),
      path('getcountry/<name>/', views.get_country, name='get-country'),
      path('update/<name>/', views.update_country, name='update-country'),
      path('delete/<name>/', views.delete_country, name='delete-country'),
      path('search/<name>/', views.search_country, name='search-country'),
      path('sgeomquery/<geom>/', views.squery_by_geom, name='squery-by-geom'),
      path('squerybycountry/<name>/', views.spatial_query_country, name='spatial-query-country'),
]