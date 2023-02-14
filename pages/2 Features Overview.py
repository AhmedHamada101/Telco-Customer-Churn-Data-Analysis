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


# add header
st.header('The Churn Details')

# Display the churn details
feature = data['churn'].value_counts(normalize = True)
fig1 = px.pie(values = feature.values, names = feature.index, hole = 0.5, title = 'churn', 
             height = 450, width = 800, color = [0, 1], color_discrete_map = {0: '#4183D7', 1: '#CC0000'})
st.plotly_chart(fig1) 

# add  note
st.markdown('##### Notes:')
if st.checkbox('Show Note'):
    st.markdown(
                '''
                *  1 = The percentage of customers who left the company. 
                *  0 = The percentage of customers who remained with the company. 
                '''
                )

# add space
st.header(' ')
st.header(' ')

# function to exploring categorical features
def about_features(col):
    feature = data[col].value_counts(normalize = True)
    fig = px.pie(values = feature.values, names = feature.index, 
                 title = col, height = 450, width = 800, hole = 0.5)
    return fig

# add header
st.header('The Feature Details')

# select all columns having object datatype
categorical_features = list(data.select_dtypes(include ='object'))
feature_options = st.selectbox('Select The Feature', categorical_features)

# Display features details
fig2 = about_features(feature_options)
st.plotly_chart(fig2)


# add dictionary
st.header(' ')
st.markdown('### Here is the data dictionary to understand the **features**')

if st.checkbox('Show The Data Dictionary'):
    st.markdown(
                '''

| Feature | Definition |
|:---|:---|
| Gender | The customer’s gender: Male, Female. |
| Senior Citizen | Indicates if the customer is 65 or older: Yes, No. |
| Partner | Indicates if the customer lives with any partner: Yes, No. |
| Dependents | Indicates if the customer lives with any dependents: Yes, No. Dependents could be children, parents, grandparents, etc. |
| Phone Service | Indicates if the customer subscribes to home phone service with the company: Yes, No. |
| Multiple Lines | Indicates if the customer subscribes to multiple telephone lines with the company: Yes, No. |
| Internet Service | Indicates if the customer subscribes to Internet service with the company: No, DSL, Fiber Optic, Cable. |
| Online Security | Indicates if the customer subscribes to an additional online security service provided by the company: Yes, No. |
| Online Backup | Indicates if the customer subscribes to an additional online backup service provided by the company: Yes, No. |
| Device Protection | Indicates if the customer subscribes to an additional device protection plan for their Internet equipment provided by the company: Yes, No. |
| Tech Support | Indicates if the customer subscribes to an additional technical support plan from the company with reduced wait times: Yes, No. |
| Streaming TV | Indicates if the customer uses their Internet service to stream television programing from a third party provider: Yes, No. The company does not charge an additional fee for this service. |
| Streaming Movies | Indicates if the customer uses their Internet service to stream movies from a third party provider: Yes, No. The company does not charge an additional fee for this service. |
| Contract | Indicates the customer’s current contract type: Month-to-Month, One Year, Two Year. |
| Paperless Billing | Indicates if the customer has chosen paperless billing: Yes, No. |
| Payment Method | Indicates how the customer pays their bill: Bank Withdrawal, Credit Card, Mailed Check. |
                
                '''
                )
    


