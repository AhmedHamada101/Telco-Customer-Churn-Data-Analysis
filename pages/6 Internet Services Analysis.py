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

# function for exploring categorical feature
def exploring_categorical_features_by_churn(feature): 
    fig = px.bar(data.groupby(feature)['churn'].mean(), height = 500, width = 600, 
                 color = data.groupby(feature)['churn'].mean().index)
    fig.update_layout(xaxis_title = feature, yaxis_title = 'Percentage of Churn')
    return fig

# add header
st.markdown('### The effect of Internet Services on customer churn:')
st.header(' ')
st.header(' ')

# select the feature
feature_options = st.selectbox('Select The Feature', ['internetservice', 'onlinesecurity', 'techsupport', 'onlinebackup', 
                                                      'deviceprotection', 'streamingtv', 'streamingmovies',])
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
                | Internet Service | Indicates if the customer subscribes to Internet service with the company: No, DSL, Fiber Optic, Cable. |
                | Online Security | Indicates if the customer subscribes to an additional online security service provided by the company: Yes, No. |
                | Online Backup | Indicates if the customer subscribes to an additional online backup service provided by the company: Yes, No. |
                | Device Protection | Indicates if the customer subscribes to an additional device protection plan for their Internet equipment provided by the company: Yes, No. |
                | Tech Support | Indicates if the customer subscribes to an additional technical support plan from the company with reduced wait times: Yes, No. |
                | Streaming TV | Indicates if the customer uses their Internet service to stream television programing from a third party provider: Yes, No. The company does not charge an additional fee for this service. |
                | Streaming Movies | Indicates if the customer uses their Internet service to stream movies from a third party provider: Yes, No. The company does not charge an additional fee for this service. |
                '''
                )