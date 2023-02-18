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

# add title
st.markdown('<h1 style = "text-align:center; font-size:250%;">Customer Demographic Info Analysis</h1>', unsafe_allow_html = True)

# add space
st.title('')
st.title('')

# function to exploring categorical features
def about_features(col):
    feature = data[col].value_counts(normalize = True)
    fig = px.pie(values = feature.values, names = feature.index, 
                 title = col, height = 400, width = 700, hole = 0.5)
    return fig


# function for exploring categorical feature
def exploring_categorical_features_by_churn(feature): 
    fig = px.bar(data.groupby(feature)['churn'].mean(), height = 500, width = 700, 
                 color = data.groupby(feature)['churn'].mean().index)
    fig.update_layout(xaxis_title = feature, yaxis_title = 'Percentage of Churn')
    return fig

# add header
st.markdown('##### Impact of Gender, SeniorCitizen, Partner and Dependentson on customer churn:')

# add space
st.header(' ')

# select the feature
feature_options = st.selectbox('Select The Feature', ['gender', 'seniorcitizen', 'partner', 'dependents'])
st.header(' ')

# Display features details
st.markdown('#### Feature Details')
fig1 = about_features(feature_options)
st.plotly_chart(fig1)

st.markdown(f'#### Percentage of Churn by {feature_options}')
fig2 = exploring_categorical_features_by_churn(feature_options)
st.plotly_chart(fig2)

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


