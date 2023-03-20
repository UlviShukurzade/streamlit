import streamlit as st
import plotly.express as px



gapminder_df = px.data.gapminder()

fig = px.scatter(data_frame=gapminder_df,
           x = 'gdpPercap', 
           y = 'lifeExp',
           size = 'pop', 
           color = 'country',
           title = 'Life Span and Wealth 1952 - 2007',
           labels = {'gdpPercap' : 'Wealth',
                   'lifeExp' : 'Life Span'},
           log_x = True,
           range_y = [25, 95],
           hover_name = 'country',
           animation_frame = 'year',
           height = 800,
           size_max=100,
          )

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

