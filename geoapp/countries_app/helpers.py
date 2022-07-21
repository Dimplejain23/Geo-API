import geopandas as gpd
import os
from sqlalchemy import create_engine

def ProcessData():
    """
    Download countries data from datahub.io. 
    Then load data in PostGIS Database on the -
    fly in memory without saving geojson as a physical file
    """
    try:
        gdf = gpd.read_file("https://datahub.io/core/geo-countries/r/countries.geojson")
        engine = create_engine(os.environ.get("DB_URL"), echo=False)
        gdf.columns= gdf.columns.str.lower()
        gdf.index += 1 
        gdf.to_postgis('countries_app_countries',engine,if_exists='replace',index=True,index_label='id')
        print("upload done successfully")
        return "upload done successfully"
    except Exception as e:
        print("upload to db failed " + str(e))
        return "upload to db failed " + str(e)