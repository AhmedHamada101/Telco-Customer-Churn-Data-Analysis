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
st.markdown('### Impact of Phone Services on customer churn:')
st.header(' ')
st.header(' ')

# select the feature
feature_options = st.selectbox('Select The Feature', ['phoneservice', 'multiplelines'])
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
                | Partner | Indicates if the customer lives with any partner: Yes, No. |
                '''
                )
