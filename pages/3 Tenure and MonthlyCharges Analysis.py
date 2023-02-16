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

# add header
st.markdown('### 1. Impact of Tenure on customer churn:')
st.header(' ')
st.header(' ')

#function exploring numericalfeatures
def exploring_numerical_features(data, col):
    fig = px.histogram(data, x = col, width = 700, height = 450)
    return fig

fig1 = exploring_numerical_features(data[data['churn'] == 1], 'tenure')
fig1.update_layout(xaxis_title = 'Tenure', yaxis_title = 'Number of Customers', 
                      title = f'Customers who left the company')
fig1.update_traces(marker_color = '#CC0000')
st.plotly_chart(fig1) 

fig2 = exploring_numerical_features(data[data['churn'] == 0], 'tenure')
fig2.update_layout(xaxis_title = 'Tenure', yaxis_title = 'Number of Customers', 
                      title = f'Customers who remained with the company')
st.plotly_chart(fig2)

# add  note
st.markdown('##### Notes:')
if st.checkbox('Show Note.'):
    st.markdown(
                '''
                | Feature | Definition |
                |:---|:---|
                | Tenure | Indicates the period the customer spent in the company. (The period will be in a month) |
                '''
                )

# add space
st.header(' ')
st.header(' ')
st.header(' ')
st.header(' ')

# add header
st.markdown('### 2. Impact of MonthlyCharges on customer churn:')
st.header(' ')

fig3 = exploring_numerical_features(data[data['churn'] == 1], 'monthlycharges')
fig3.update_layout(xaxis_title = 'MonthlyCharges', yaxis_title = 'Number of Customers', 
                      title = f'Customers who left the company')
fig3.update_traces(marker_color = '#CC0000')
st.plotly_chart(fig3) 

fig4 = exploring_numerical_features(data[data['churn'] == 0], 'monthlycharges')
fig4.update_layout(xaxis_title = 'MonthlyCharges', yaxis_title = 'Number of Customers', 
                      title = f'Customers who remained with the company')
st.plotly_chart(fig4)

# add  note
st.markdown('##### Notes:')
if st.checkbox('Show Note..'):
    st.markdown(
                '''
                | Feature | Definition |
                |:---|:---|
                | MonthlyCharge | Indicates the customer’s current total monthly charge for all their services from the company. |
                '''
                )
