import streamlit as st

from data_loaders import *
from chart_builders import *

BIKE_POINTS_URL = "https://api.tfl.gov.uk/BikePoint/"
LAD_BOUNDARY_URL = "https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Local_Authority_Districts_December_2023_Boundaries_UK_BGC/FeatureServer/0/query?where=1%3D1&outFields=LAD23CD,LAD23NM,LONG,LAT,Shape__Area&outSR=4326&f=geojson"
TFL_CYCLE_LANES_URL = "https://cycling.data.tfl.gov.uk/CyclingInfrastructure/data/lines/cycle_lane_track.json"

st.title('Bike Points in London')

data_load_state = st.info('Loading initial data into app...', icon="ℹ️")
bike_points = load_bike_points_data(BIKE_POINTS_URL)
london_boroughs = load_london_borough_bondaries_data(LAD_BOUNDARY_URL)
cycle_lanes = load_cycle_lane_data(TFL_CYCLE_LANES_URL)
data_load_state.info('Data loaded successfully! This has been cached and will not be loaded again.')

st.subheader('Map of all bike point locations')
map_fig = pydeck_map(bike_points, london_boroughs, cycle_lanes)
st.pydeck_chart(map_fig)

st.subheader('Bike Points Datatable')
st.write(bike_points)