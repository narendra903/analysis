
import streamlit as st
import pandas as pd

st.title("My Data Analysis Project")

# Load your data
data = pd.read_csv('/workspaces/analysis/app_analyis/df.csv')

# Display the data
st.write("Here is the data:")
st.dataframe(data)

# Add more Streamlit code here to build your app
