import streamlit as st
import requests
import pandas as pd

### Functions for loading data ###

# All functions load data from a url, perform some basic manipulations, and returns a dataset

@st.cache_data
def load_bike_points_data(url):
    r = requests.get(url)
    df = pd.DataFrame(r.json())
    df = df[['id', 'commonName', 'lat', 'lon']]
    return df

@st.cache_data
def load_cycle_lane_data(url):
    r = requests.get(url)
    json = r.json()
    return json

@st.cache_data
def load_london_borough_bondaries_data(url):
    r = requests.get(url)
    json = r.json()

    # Filters local authority districts for London boroughs only
    new_features = list()
    for i in range(len(json['features'])):
        temp = json['features'][i]
        if temp['properties']['LAD23CD'].startswith('E09'):
            new_features.append(temp)
    json['features'] = new_features
    return json


### Functions for processing data ###

# Filters cycle lane dataset for routes that are segregated from lanes used by other vehicles
def filter_cycle_lanes(data):
    new_features = list()
    for i in range(len(data['features'])):
        temp = data['features'][i]
        if temp['properties']['CLT_SEGREG'] == 'TRUE':
            new_features.append(temp)
        # elif temp['properties']['CLT_CARR'] == 'TRUE':
        #     new_features.append(temp)
    data['features'] = new_features
    return data