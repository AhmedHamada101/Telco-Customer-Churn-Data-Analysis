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
st.markdown('<h1 style = "text-align:center; font-size:250%;">Customer Account Info Analysis</h1>', unsafe_allow_html = True)

# add space
st.title('')
st.title('')

# add header
st.markdown('##### 1. Impact of Tenure, MonthlyCharges and TotalCharges on customer churn:')

# add space
st.header(' ')

#function exploring numericalfeatures
def exploring_numerical_features(data, col):
    fig = px.histogram(data, x = col, width = 355, height = 450)
    return fig

# select the feature
feature_options1 = st.selectbox('Select The Feature', ['tenure', 'monthlycharges', 'totalcharges'])

# add space
st.header(" ")

with st.container():
    col1, col2 = st.columns(2)
    
    fig1 = exploring_numerical_features(data[data['churn'] == 1], feature_options1)
    fig1.update_layout(xaxis_title = 'Tenure', yaxis_title = 'Number of Customers')
    fig1.update_traces(marker_color = '#CC0000')
    
    fig2 = exploring_numerical_features(data[data['churn'] == 0], feature_options1)
    fig2.update_layout(xaxis_title = 'Tenure', yaxis_title = 'Number of Customers')

    with col1:
        st.markdown('##### Customers who left the company:')
        st.plotly_chart(fig1) 

    with col2:
        st.markdown('##### Customers who remainedthe company:')
        st.plotly_chart(fig2)

# add  note
st.markdown('##### Notes:')
if st.checkbox('Show Note.'):
    st.markdown('''
                | Feature | Definition |
                |:---|:---|
                | Tenure | Indicates the period the customer spent in the company. (The period will be in a month) |
                | MonthlyCharge | Indicates the customer’s current total monthly charge for all their services from the company. |
                | TotalCharges | Indicates the customer’s total charges, calculated to the end of the quarter specified above. |
                ''')
    
 # add space
st.header(' ')
st.header(' ')
st.header(' ')

# add header
st.markdown('##### 2. Impact of PaymentMethod, PaperlessBilling and Contract on customer churn:')

# add space
st.header(' ')

# function to exploring categorical features
def about_features(col):
    feature = data[col].value_counts(normalize = True)
    fig = px.pie(values = feature.values, names = feature.index, 
                 title = col, height = 450, width = 800, hole = 0.5)
    return fig


# function for exploring categorical feature
def exploring_categorical_features_by_churn(feature): 
    fig = px.bar(data.groupby(feature)['churn'].mean(), height = 500, width = 800, 
                 color = data.groupby(feature)['churn'].mean().index)
    fig.update_layout(xaxis_title = feature, yaxis_title = 'Percentage of Churn')
    return fig

# select the feature
feature_options2 = st.selectbox('Select The Feature', ['paymentmethod', 'paperlessbilling', 'contract'])

# Display features details
st.markdown('#### Feature Details')
fig3 = about_features(feature_options2)
st.plotly_chart(fig3)

# add space
st.header(' ')

st.markdown(f'#### Percentage of Churn by {feature_options2}')
fig4 = exploring_categorical_features_by_churn(feature_options2)
st.plotly_chart(fig4) 

# add  note
st.markdown('##### Notes:')
if st.checkbox('Show Note'):
    st.markdown('''
                | Feature | Definition |
                |:---|:---|
                | Contract | Indicates the customer’s current contract type: Month-to-Month, One Year, Two Year. |
                | Paperless Billing | Indicates if the customer has chosen paperless billing: Yes, No. |
                | Payment Method | Indicates how the customer pays their bill: Bank Withdrawal, Credit Card, Mailed Check. |
                ''')   

