import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv('india.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India Data visualization')

selected_state = st.sidebar.selectbox('Select a State',list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represents primary parameter')
    st.text('Color represents secondary parameter')
    if selected_state == 'Overall India':
        # plotting for India
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', size=primary, color=secondary,
                                color_continuous_scale='Plasma', zoom=3, mapbox_style="carto-positron", width=1200,
                                height=700, hover_name="District")
        st.plotly_chart(fig, use_container_width=True)
    else:
        # plot for the state
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary, color=secondary,
                                color_continuous_scale='Plasma', zoom=5, mapbox_style="carto-positron", width=1200,
                                height=700, hover_name="District")
        # Expand figure size
        # fig.update_layout(width=1000, height=600)
        st.plotly_chart(fig, use_container_width=True)
