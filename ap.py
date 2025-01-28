import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv('vehicles_us.csv')
df['model_year'] = pd.to_datetime(df['model_year'], format='%Y')
# replacing missing values for cylinders with the mean
df['cylinders'].fillna(df['cylinders'].mean(), inplace=True) 
# replacing missing values for the odometer with the median
df['odometer'].fillna(df['odometer'].median(), inplace=True) 
# Missing values of colour to other colours
df['paint_color'].fillna('Other', inplace=True)
# the values here are either 1 or 0. so I replace missing values with 0
df['is_4wd'] = df['is_4wd'].fillna(0)
# I assume that missing values have values of the previous year 
df['model_year'] = df['model_year'].fillna(method='ffill')
st.header("Used Car Sales Analysis")
fig_hist = px.histogram(df, x='price', title='Distribution of Car Prices')
st.plotly_chart(fig_hist)
show_scatter = st.checkbox('Show Scatter Plot')

# fig_scatter = px.scatter(df, x='model_year', y='price', title='Car Price vs Model Year')
# fig_scatter.update_layout(
#     xaxis_title='Model Year',
#     yaxis_title='Price',
#     visible='hidden' if not show_scatter else 'visible'  # Change 'visibility' to 'visible'
# )

st.plotly_chart(fig_scatter)
