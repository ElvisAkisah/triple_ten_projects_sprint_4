import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv('vehicles_us.csv')
df['model_year'] = pd.to_datetime(df['model_year'], format='%Y')
st.header("Used Car Sales Analysis")
# Impute missing values in 'cylinders'
df['cylinders'] = df.groupby('model')['cylinders'].transform(lambda x: x.fillna(x.median())) 
# Impute missing values in 'odometer'
df['odometer'] = df.groupby('model_year')['odometer'].transform(lambda x: x.fillna(x.median())) 
# Missing values of colour to other colours
df['paint_color'].fillna('Other', inplace=True)
# the values here are either 1 or 0. so I replace missing values with 0
df['is_4wd'] = df['is_4wd'].fillna(0)
# Impute missing values in 'model_year'
df['model_year'] = df.groupby('model')['model_year'].transform(lambda x: x.fillna(x.median()))
# Handle outliers in 'model_year' (adjust quantiles as needed)
Q1_model_year = df['model_year'].quantile(0.25)
Q3_model_year = df['model_year'].quantile(0.75)
IQR_model_year = Q3_model_year - Q1_model_year
lower_bound_model_year = Q1_model_year - 1.5 * IQR_model_year
upper_bound_model_year = Q3_model_year + 1.5 * IQR_model_year
df = df[(df['model_year'] >= lower_bound_model_year) & (df['model_year'] <= upper_bound_model_year)]

# Handle outliers in 'price' (replace 'price' with your actual price column name and adjust quantiles as needed)
Q1_price = df['price'].quantile(0.25)
Q3_price = df['price'].quantile(0.75)
IQR_price = Q3_price - Q1_price
lower_bound_price = Q1_price - 1.5 * IQR_price
upper_bound_price = Q3_price + 1.5 * IQR_price
df = df[(df['price'] >= lower_bound_price) & (df['price'] <= upper_bound_price)]
fig1 = px.histogram(df, x="price", title='Distribution of price')
fig1.show()
fig2 = px.box(df, y="price", color="model", title='Price by car model')
fig2.show()
fig3 = px.line(df, x="date_posted", y="price", title='Price over time')
fig3.show()
fig4 = px.scatter(df, x="odometer", y="price", 
                 title='Price vs. Odometer', 
                 labels={'odometer': 'Odometer (miles)', 'price': 'Price'})
fig4.show()
fig5 = px.histogram(df, x="odometer", title='Distribution of Odometer Readings')
fig5.show()
fig6 = px.scatter(df, x="model_year", y="price", 
                 title='Price vs. Model Year', 
                 labels={'model_year': 'Model Year'})
fig6.show()
