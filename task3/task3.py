import geopandas as gpd
import matplotlib.pyplot as plt


def plot_shapefile(shapefile_path):
    gdf = gpd.read_file(shapefile_path)

    gdf['length'] = gdf['geometry'].length

    gdf.plot(column='length', cmap='OrRd', legend=True, figsize=(10, 6))
    plt.title('Choropleth Map of LineString Lengths')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()


plot_shapefile('gis_osm_waterways_free_1.shp')
