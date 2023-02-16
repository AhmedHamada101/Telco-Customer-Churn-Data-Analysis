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

# data content
st.info('### The dataset includes information about: ')
st.markdown('''
            * **Customers who left within the last month** – Churn column (Target).\n
            * **Services that each customer has signed up for** – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies.\n  
            * **Customer account information** – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges.\n
            * **Demographic info about customers** – gender, age range, and if they have partners and dependents.
            ''')

# add space
st.title(' ')
st.title(' ')

# add header
st.info('### Churn Distribution')

# Display the churn details
feature = data['churn'].value_counts(normalize = True)
fig1 = px.pie(values = feature.values, names = feature.index, hole = 0.5, title = 'churn', 
             height = 400, width = 800, color = [0, 1], color_discrete_map = {0: '#4183D7', 1: '#CC0000'})
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
st.title(' ')
st.title(' ')

# some insights
st.info('### Some insights from the dataset: ')

st.markdown('##### 1. **In terms of Tenure and Monthly Charges:**')
st.markdown('''
            * Customers who come for 1 to 5 months are more probable to churn.
            * customers who do not churn, tend to stay for a longer tenure with the company.
            * Customers who pay higher monthly charges (around 70 to 105) are also more probable to be affected.
            ''')

st.markdown('##### 2. **In terms of Senior Citizens, Partners, and Dependents:**')
st.markdown('''
            * Senior citizens are only 16% of customers, but they have a much higher churn rate of 42% and 23% for non-seniors.
            * About 52% of customers don't have a partner, but they have a much higher churn rate of 33% and 20% for customers who have a partner.
            * About 70% of customers don't have dependents, but they have a much higher churn rate of 31% and 16% for customers who have dependents.
            ''')

st.markdown('##### 3. **In terms of Phone Services, Multiple Lines:**')
st.markdown('''
            * About 90% of customers have phone services, but customers with multiple lines have a slightly higher churn rate of about 28%, and 25% for customers who don't have multiple lines.
            * Customers who use multiple lines pay more monthly charges than the rest.
            ''')

st.markdown('##### 4. **In terms of Internet Service:**')
st.markdown('''
            * About 44% of customers use fiber optic and 34.4% use DSL, but customers who use fiber optic have a higher churn rate of about 42%, and 19% for customers who use DSL. 
            * Customers who use fiber optic pay more monthly charges than they use DSL connections.
            ''')

st.markdown('##### 5. **In terms of Internet Services:**')
st.markdown('''
            * About 49% of customers don't subscribe to the online security service and 29% subscribe, but customers who don't subscribe have a higher churn rate of about 42%, and 15% for customers who subscribe.
            * About 50% of customers don't subscribe to the tech support service and 29% subscribe, but customers who don't subscribe have a higher churn rate of about 42%, and 15% for customers who subscribe.
            * About 44% of customers don't subscribe to the online backup service and 35.5% subscribe, but customers who don't subscribe have a higher churn rate of about 40%, and 22% for customers who subscribe.
            * About 44% of customers don't subscribe to the device protection service and 34% subscribe, but customers who don't subscribe have a higher churn rate of about 39%, and 23% for customers who subscribe.
            ''')

st.markdown('##### 6. **In terms of Contact and Payment Methods:**')
st.markdown('''
            * About 55% of customers contract month to month and 24% contract for two years, but customers who contract month to month have a higher churn rate of about 43%, and 3% for customers who contract for two years.
            * About 41% of customers chose paper billing, but customers who have chosen paperless billing have a higher churn rate of about 34%, and 16% for customers who chose paper billing.
            * About 35% of customers prefer to pay by the Electronic check method, but this method has a very higher churn rate of about 45% compared to other methods.
            *  Mailed checks have lower monthly charges.
            ''')

st.markdown('##### 7. **In terms of insignificant features:**')
st.markdown('''
            * Customer Churn is not affected by gender.
            * Customer Churn is not affected by streaming tv services.
            * Customer Churn is not affected by streaming movie services.
            ''')