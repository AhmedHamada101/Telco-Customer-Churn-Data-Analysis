# import libraries
import streamlit as st 
import pandas as pd
import plotly.express as px

# load data
@st.cache_data
def load_data():
    data = pd.read_csv('customer_churn_modified_data.csv')
    data['seniorcitizen'].replace(to_replace = 1, value = 'Yes', inplace = True)
    data['seniorcitizen'].replace(to_replace = 0,  value = 'No', inplace = True)
    return data

data = load_data()

# function for exploring categorical feature
def exploring_categorical_features_by_churn(feature): 
    fig = px.bar(data.groupby(feature)['churn'].mean(), height = 500, width = 600, 
                 color = data.groupby(feature)['churn'].mean().index)
    fig.update_layout(xaxis_title = feature, yaxis_title = 'Percentage of Churn')
    return fig

# add header
st.markdown('### The effect of Gender, SeniorCitizen, Partner and Dependentson on customer churn:')
st.header(' ')
st.header(' ')

# select the feature
feature_options = st.selectbox('Select The Feature', ['gender', 'seniorcitizen', 'partner', 'dependents'])
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
                | Senior Citizen | Indicates if the customer is 65 or older: Yes, No. |
                | Partner | Indicates if the customer lives with any partner: Yes, No. |
                | Dependents | Indicates if the customer lives with any dependents: Yes, No. Dependents could be children, parents, grandparents, etc. |
                '''
                )


