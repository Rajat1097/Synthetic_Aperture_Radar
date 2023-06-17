# import libraries
import asf_search as asf
import geopandas as gpd
from shapely.geometry import box
from datetime import date
import getpass
from os import listdir

# username and password for authentication
# username = input('Username : ')
# password = getpass.getpass('password : ')

# read shapefile of AOI
gdf = gpd.read_file(
    'E:/EOGM/Dissertation/Practice_data/51_compartment/fifty_one.shp')  # path of AOI

# save bounding box
bounds = gdf.total_bounds

# GeoDataFrame of the Bounding Box
gdf_bounds = gpd.GeoSeries([box(*bounds)])

# convert to WKT Coordinates
wkt_aoi = gdf_bounds.to_wkt().values.tolist()[0]

# search for results of images
results = asf.search(
    platform=asf.PLATFORM.SENTINEL1A,   # satellite name
    processingLevel=[asf.PRODUCT_TYPE.GRD_HD],  # product type
    start=date(2017, 1, 1),  # start date
    end=date(2017, 1, 31),   # end date
    intersectsWith=wkt_aoi   # AOI
)

# print total number of images
print(f'Total Images Found: {len(results)}')

# Save metadata to a dictionary
metadata = results.geojson()

# start the session with login credentials of earth data
session = asf.ASFSession().auth_with_creds(
    username='drajat1097', password='Drajat1097@')

# download the result to path
results.download(
    path='E:/EOGM/Dissertation/Practice_data/data/data_download/',  # path for data download
    session=session,
    processes=1  # images to download at one time
)

# list of downloaded images
# listdir('E:/EOGM/Dissertation/Practice_data/data_download/data/')
