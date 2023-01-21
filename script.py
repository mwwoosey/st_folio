import streamlit as st
import pandas as pd
import numpy as np


# https://docs.streamlit.io/library/get-started/create-an-app
st.write("""
# My first app
Hello *world!*
""")

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

d = {'Chocolate_Amount': choc_freq, 'Kellie_Happiness': kellie_happy}
df = pd.DataFrame(data=d)
st.line_chart(df)

st.write(df)

st.subheader('Number of kisses by hour')

