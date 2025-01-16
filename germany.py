import streamlit as st
import plotly.express as px
import pandas as pd

# Load the Germany dataset from Plotly Express
df = px.data.germany()

# Display the first few rows of the dataset to understand its structure
st.write("Germany Population & Migration Data:", df.head())

# Create an interactive line plot showing migration, population, births, and deaths over the years
fig = px.line(df,
              x="year", 
              y=["pop", "migration", "births", "deaths"], 
              labels={
                  "year": "Year", 
                  "pop": "Population", 
                  "migration": "Migration", 
                  "births": "Births", 
                  "deaths": "Deaths"
              },
              title="Germany Population, Migration, Births & Deaths (Yearly)")

# Display the Plotly figure in Streamlit
st.plotly_chart(fig)

# Optional: Show the raw dataset (if needed for analysis)
st.write("Raw Data", df)
