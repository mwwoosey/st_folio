import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime

@st.experimental_memo
def get_data():
    df = pd.read_csv('data/strong.csv', parse_dates=['Date'])
    return df

df = get_data()  

# extra column with yyyy-mm
df['Month'] = df.apply(lambda x: x['Date'].strftime("%Y-%m"), axis=1)

st.title("My Strength Training :weight_lifter:")
st.write("""This application uses data recorded from my workouts using [Strong](https://www.strong.app/).
I have created a number of metrics to measure my training and progression.
""")

# container for one rep max
with st.container():
    st.subheader('My progression using 1RM metric')
    st.write("""
    The Epley (1985) equation is largely the most popular method used to create a one-rep max. This metric
    gives an estimation of the highest weight the lifter could complete one time only, and is used in raw 
    strength training, where endurance is not a consideration.
    """)
    
    # data manipulation
    df['1RM'] = df.apply(lambda x: (0.033 * x['Reps'] * x['Weight']) + x['Weight'], axis=1)
    rm_set = df[(df['Reps'] <= 10)]
    rm_set = df.groupby(['Month','Exercise Name'], as_index=False)['1RM'].max()

    selected_1rm_exercise = st.radio(
        "Select an exercise to visualise...",
        ('Squat (Barbell)', 'Deadlift (Barbell)', 'Bench Press (Barbell)'), key='repmax')

    st.line_chart(rm_set.loc[rm_set['Exercise Name'] == selected_1rm_exercise]
                  , x="Month", y="1RM")

# container for training volume
with st.container():
    st.subheader('Progression through Training Volume')
    st.write("""
    This visualisation plots the maximum training volume lifted for each exercise per month. This is the 
    number of reps multiplied by the weight used in the set.
    """)
    
    # data manipulation
    df['Volume'] = df.apply(lambda x: x['Weight'] * x['Reps'], axis=1)
    volume_set = df.groupby(['Month','Exercise Name'], as_index=False)['Volume'].max()

    selected_volume_exercise = st.radio(
        "Select an exercise to visualise...",
        ('Squat (Barbell)', 'Deadlift (Barbell)', 'Bench Press (Barbell)'), key='volmax')

    st.line_chart(volume_set.loc[volume_set['Exercise Name'] == selected_volume_exercise]
                  , x="Month", y="Volume")