import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon="@:tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# load assets
data_img = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_yswivetl.json")
mountain_img = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_3uLMgcknAG.json")

# header section
with st.container():
    st.subheader("Hi, I'm Michael :wave:")
    st.title("A Business Analyst based in the UK")
    st.write("Using digital skills to better serve businesses, customers and society")
    st.write("[My LinkedIn >](http://www.linkedin.com/in/mwwoosey404)")

# what i do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("What I do")
        st.write("""
        I am passionate about producing data which is concise, meaningful and drives great decisions.
        - ETL (Extract, Transform, Load)
        - Data Manipulation & Visualation (Tableau)
        - Data Modelling (Python)
        - Statistics and Analysis
        """)

    with right_column:
        st_lottie(data_img, height=300, key="coding")

# my first, first project
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st_lottie(mountain_img, height=300, key="mountain")

    with text_column:
        st.subheader("British Mountains")
        st.write("""
        Here is some information about something I did
        """)
        st.markdown("[Watch Video...](http://google.com)")