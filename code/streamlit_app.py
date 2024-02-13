import streamlit as st

from data_loaders import *
from chart_builders import *

BIKE_POINTS_URL = "https://api.tfl.gov.uk/BikePoint/"
LAD_BOUNDARY_URL = "https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Local_Authority_Districts_December_2023_Boundaries_UK_BGC/FeatureServer/0/query?where=1%3D1&outFields=LAD23CD,LAD23NM,LONG,LAT,Shape__Area&outSR=4326&f=geojson"
TFL_CYCLE_LANES_URL = "https://cycling.data.tfl.gov.uk/CyclingInfrastructure/data/lines/cycle_lane_track.json"

st.set_page_config(layout='wide')

st.title('Bike Points in London')

data_load_state = st.info('Loading initial data into app...', icon="ℹ️")
bike_points = load_bike_points_data(BIKE_POINTS_URL)
london_boroughs = load_london_borough_bondaries_data(LAD_BOUNDARY_URL)
cycle_lanes = load_cycle_lane_data(TFL_CYCLE_LANES_URL)
data_load_state.info('Data loaded successfully! This has been cached and will not be loaded again.')

left_col, right_col = st.columns([3,2])

right_col.subheader('Context')
segregation = right_col.checkbox(label="Segregated cycle lanes only", value=0)
if segregation:
    cycle_lanes = filter_cycle_lanes(cycle_lanes)
right_col.text("White Lines = London borough boundaries.\n"
               "Purple Points = TFL Bike Points.\n"
               "Orange Lines = Cycling network.")
right_col.divider()
right_col.text(
    "The Santander public bike hire scheme is predominantly located in Zones 1 & 2\n"
    "of London's transport network. The cycling network is spreads over all of London,\n"
    "however, the quality of those cycle routes is varied. \n\n"
    "According to a recent survey on perceptions of cycling, non-cyclists said high\n"
    "quality and safe cycling infrastructure would be their greatest barrier to not\n"
    "partipating in cycling.\n\n"
    "To increase uptake in cycling, improving the cycling network may be a more\n"
    "effective solution than inreasing the number of rental bikes."
)

left_col.subheader('Map of all bike point locations')
map_fig = pydeck_map(bike_points, london_boroughs, cycle_lanes)
left_col.pydeck_chart(map_fig)