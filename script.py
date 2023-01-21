import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")

choc_freq = range(1,25)
kellie_happy = [x**2 for x in choc_freq]

d = {'Chocolate_Amount': choc_freq, 'Kellie_Happiness': kellie_happy}
df = pd.DataFrame(data=d)
st.line_chart(df)