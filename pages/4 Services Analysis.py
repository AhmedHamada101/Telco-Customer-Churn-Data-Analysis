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
st.markdown('<h1 style = "text-align:center; font-size:250%;">Customer Services Analysis</h1>', unsafe_allow_html = True)

# add space
st.title('')
st.title('')

# add header
st.markdown('### Impact of Servies on customer churn:')

# add space
st.header(' ')

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

# select the feature
feature_options = st.selectbox('Select The Feature', ['phoneservice', 'multiplelines', 'internetservice', 'onlinesecurity', 'techsupport', 
                                                      'onlinebackup', 'deviceprotection', 'streamingtv', 'streamingmovies',])

# Display features details
st.markdown('#### Feature Details')
fig1 = about_features(feature_options)
st.plotly_chart(fig1)

# add space
st.header(' ')

st.markdown(f'#### Percentage of Churn by {feature_options}')
fig2 = exploring_categorical_features_by_churn(feature_options)
st.plotly_chart(fig2)
                
                # add  note
st.markdown('##### Notes:')
if st.checkbox('Show Note'):
    st.markdown('''
                | Feature | Definition |
                |:---|:---|
                | Phone Service	| Indicates if the customer subscribes to home phone service with the company: Yes, No.|
                | Multiple Lines | Indicates if the customer subscribes to multiple telephone lines with the company: Yes, No. |
                | Internet Service | Indicates if the customer subscribes to Internet service with the company: No, DSL, Fiber Optic, Cable. |
                | Online Security | Indicates if the customer subscribes to an additional online security service provided by the company: Yes, No. |
                | Online Backup | Indicates if the customer subscribes to an additional online backup service provided by the company: Yes, No. |
                | Device Protection | Indicates if the customer subscribes to an additional device protection plan for their Internet equipment provided by the company: Yes, No. |
                | Tech Support | Indicates if the customer subscribes to an additional technical support plan from the company with reduced wait times: Yes, No. |
                | Streaming TV | Indicates if the customer uses their Internet service to stream television programing from a third party provider: Yes, No. The company does not charge an additional fee for this service. |
                | Streaming Movies | Indicates if the customer uses their Internet service to stream movies from a third party provider: Yes, No. The company does not charge an additional fee for this service. |
                ''')
