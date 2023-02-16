# import libraries
import streamlit as st 
import pandas as pd

# load data
@st.cache_data
def load_data():
    data = pd.read_csv('customer_churn_modified_data.csv')
    return data

data = load_data()

# add title
st.markdown('<h1 style = "text-align:center; font-size:250%;">Telco Customare Churn Data Analysis</h1>', unsafe_allow_html = True)
st.title(' ')

# about data
st.header('About Project')
st.markdown('You can get data from Kaggle: [Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)', unsafe_allow_html = True)
st.markdown('You can see the notebook on Kaggle: [Kaggle Notebook](https://www.kaggle.com/ahmedmohammedhamada/customer-churn-analysis-eda)', unsafe_allow_html = True)
st.markdown('You can check the project repository on GitHub: [Project Repository](https://github.com/AhmedHamada101/Telco-Customer-Churn-Data-Analysis)', unsafe_allow_html = True)
st.markdown('You can view my LinkedIn Profile: [LinkedIn Profile](https://www.linkedin.com/in/ahmed-hamada-a38b9a219)', unsafe_allow_html = True)

st.header(' ')
st.header(' ')

# data content
st.header('Data Content')
st.markdown('Each row represents a customer, each column contains customer’s attributes described on the column Metadata.')

st.markdown('#### The dataset includes information about:')
st.markdown('''
            * Customers who left within the last month – the column is called Churn.
            * Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies.
            * Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges.
            * Demographic info about customers – gender, age range, and if they have partners and dependents.
            ''')

st.header(' ')
st.header(' ')

# display data
st.header('Display Data')
if st.checkbox('Show Data'):
    st.dataframe(data)
