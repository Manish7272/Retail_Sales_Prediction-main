# import streamlit as st
# import pandas as pd
# import numpy as np
# from sklearn.preprocessing import LabelEncoder
# import joblib

# # Load your trained model
# model = joblib.load('models\model1.pkl')



# # Function to predict sales
# def predict_sales(input_data):
#     sales_prediction = model.predict(input_data)
#     return sales_prediction



# # Streamlit app
# def main():
#     st.title('Sales Prediction App')

#     # Input widgets
#     PromoInterval = st.selectbox("Promo Interval", ['No Promotion', 'Jan,Apr,Jul,Oct', 'Feb,May,Aug,Nov', 'Mar,Jun,Sept,Dec'])
#     StoreType = st.radio("StoreType", ["a", "b", "c", "d"])
#     Assortment = st.radio("Assortment", ["a", "b", "c"])
#     StateHoliday = st.radio("State Holiday", ["1", "0"])
#     SchoolHoliday = st.radio("School Holiday", ["1", "0"])
#     Promo = st.radio("Promo", ["1", "0"])
#     Store = st.slider("Store", 1, 1115)
#     Customers = st.slider("Customers", 0, 7388)
#     CompetitionDistance = st.slider("Competition Distance", 20, 75860)
#     CompetitionOpenSinceMonth = st.slider("Competition Open Since Month", 1, 12)
#     CompetitionOpenSinceYear = st.slider("Competition Open Since Year", 1998, 2015)

#    	# PromoInterval	StoreType	Assortment	StateHoliday	Store	Customers	Promo	SchoolHoliday	CompetitionDistance	CompetitionOpenSinceMonth	CompetitionOpenSinceYear
#     # Store user inputs
#     input_data = pd.DataFrame({
#         'PromoInterval': [PromoInterval],
#         'StoreType': [StoreType],
#         'Assortment': [Assortment],
#         'StateHoliday': [StateHoliday],
#         'Store': [Store],

#         'Customers': [Customers],
#         'Promo': [Promo],

#         'SchoolHoliday': [SchoolHoliday],
#         'CompetitionDistance': [CompetitionDistance],
#         'CompetitionOpenSinceMonth': [CompetitionOpenSinceMonth],
#         'CompetitionOpenSinceYear': [CompetitionOpenSinceYear]
#     })

#     # Display input data
#     st.subheader('Input Data:')
#     st.write(input_data)
    
#     # Predict sales
#     if st.button('Predict Sales'):
#         prediction = predict_sales(input_data)
#         st.write('Predicted Sales:', prediction)

# if __name__ == '__main__':
#     main()

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import joblib

# Load your trained model
model = joblib.load('models\model1.pkl')

# Function to predict sales
def predict_sales(input_data):
    sales_prediction = model.predict(input_data)
    return sales_prediction

# Function for data analysis
def perform_analysis(data):
    # Add your analysis code here
    st.subheader("Analysis")
    st.write("Performing analysis...")

# Function for data overview
def show_data_overview():
    # Load data from CSV file
    data = pd.read_csv('Dataset/rossmann.csv')
    
    # Display data overview
    st.subheader("Data Overview")
    st.write(data)

# Streamlit app
def main():
    st.title('Sales Prediction App')

    # Sidebar options
    sidebar_option = st.sidebar.radio("Navigation", ["Main", "Analysis", "Data Overview"])

    if sidebar_option == "Main":
        # Input widgets
        PromoInterval = st.selectbox("Promo Interval", ['No Promotion', 'Jan,Apr,Jul,Oct', 'Feb,May,Aug,Nov', 'Mar,Jun,Sept,Dec'])
        StoreType = st.radio("StoreType", ["a", "b", "c", "d"])
        Assortment = st.radio("Assortment", ["a", "b", "c"])
        StateHoliday = st.radio("State Holiday", ["1", "0"])
        SchoolHoliday = st.radio("School Holiday", ["1", "0"])
        Promo = st.radio("Promo", ["1", "0"])
        Store = st.slider("Store", 1, 1115)
        Customers = st.slider("Customers", 0, 7388)
        CompetitionDistance = st.slider("Competition Distance", 20, 75860)
        CompetitionOpenSinceMonth = st.slider("Competition Open Since Month", 1, 12)
        CompetitionOpenSinceYear = st.slider("Competition Open Since Year", 1998, 2015)

        # Store user inputs
        input_data = pd.DataFrame({
            'PromoInterval': [PromoInterval],
            'StoreType': [StoreType],
            'Assortment': [Assortment],
            'StateHoliday': [StateHoliday],
            'Store': [Store],

            'Customers': [Customers],
            'Promo': [Promo],

            'SchoolHoliday': [SchoolHoliday],
            'CompetitionDistance': [CompetitionDistance],
            'CompetitionOpenSinceMonth': [CompetitionOpenSinceMonth],
            'CompetitionOpenSinceYear': [CompetitionOpenSinceYear]
        })

        # Display input data
        st.subheader('Input Data:')
        st.write(input_data)
        
        # Predict sales
        if st.button('Predict Sales'):
            prediction = predict_sales(input_data)
            st.write('Predicted Sales:', prediction)

    elif sidebar_option == "Analysis":
        perform_analysis(None)  # Pass data for analysis if needed

    elif sidebar_option == "Data Overview":
        show_data_overview()  # Pass data for overview if needed

if __name__ == '__main__':
    main()

