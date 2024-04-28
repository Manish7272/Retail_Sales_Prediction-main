import streamlit as st
import pandas as pd

# st.title("hi")

# Function for data overview
def show_data_overview():
    # Load data from CSV file
    data = pd.read_csv("Dataset\Rossmann_Cleaned_data.csv")
    
    # Display data overview
    st.subheader("Data Overview")
    st.write(data)


show_data_overview()  # Call the function to show data overview
