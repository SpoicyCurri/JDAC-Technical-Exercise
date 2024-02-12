import pydeck as pdk

def pydeck_map(bike_points, london_boroughs, cycle_lanes):
    fig = pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=51.5072, longitude=-0.1276, 
            zoom=10.5, bearing=0, pitch=0),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                bike_points,
                get_position=['lon', 'lat'],
                get_radius=90,
                get_fill_color=[180, 0, 200, 140],
                pickable=True
                ),
            pdk.Layer(
                'GeoJsonLayer',
                london_boroughs,
                filled=False,
                get_line_color=[255,255,255],
                getLineWidth=10,
                lineWidthMinPixels=1,
                pickable=False
                ),
            pdk.Layer(
                'GeoJsonLayer',
                cycle_lanes,
                filled=False,
                get_line_color=[255,153,51],
                getLineWidth=5,
                lineWidthMinPixels=1,
                pickable=False
                )
            ],
        tooltip={"html": "<b>Location:</b> {commonName}"}
    )

    return fig