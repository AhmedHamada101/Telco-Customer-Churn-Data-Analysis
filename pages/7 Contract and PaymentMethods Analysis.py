# import libraries
import streamlit as st 
import pandas as pd
import plotly.express as px

# load data
@st.cache_data
def load_data():
    data = pd.read_csv('customer_churn_modified_data.csv')
    return data

data = load_data()

# add title
st.markdown('<h1 style = "text-align:center; font-size:250%;">Telco Customare Churn Data Analysis</h1>', unsafe_allow_html = True)
st.title(' ')
st.title(' ')

# function for exploring categorical feature
def exploring_categorical_features_by_churn(feature): 
    fig = px.bar(data.groupby(feature)['churn'].mean(), height = 500, width = 600, 
                 color = data.groupby(feature)['churn'].mean().index)
    fig.update_layout(xaxis_title = feature, yaxis_title = 'Percentage of Churn')
    return fig

# add header
st.markdown('### Impact of Contract and PaymentMethods on customer churn:')
st.header(' ')
st.header(' ')

# select the feature
feature_options = st.selectbox('Select The Feature', ['paymentmethod', 'paperlessbilling', 'contract'])

st.header(' ')

fig = exploring_categorical_features_by_churn(feature_options)
st.plotly_chart(fig) 

# add  note
st.markdown('##### Notes:')
if st.checkbox('Show Note'):
    st.markdown(
                '''
                | Feature | Definition |
                |:---|:---|
                | Contract | Indicates the customer’s current contract type: Month-to-Month, One Year, Two Year. |
                | Paperless Billing | Indicates if the customer has chosen paperless billing: Yes, No. |
                | Payment Method | Indicates how the customer pays their bill: Bank Withdrawal, Credit Card, Mailed Check. |
                '''
                )   
