import streamlit as st
# from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Michael Woosey - Business Analyst", page_icon="@:bar_chart:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# load assets
data_img = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_yswivetl.json")

# sidebar
# with st.sidebar:
#     st.write("My Socials:")
#     st.write("[LinkedIn >](http://www.linkedin.com/in/mwwoosey404)")

# header section
with st.container():
    st.subheader("Hi, I'm Michael :wave:")
    st.title("A Business Analyst based in the UK")
    # st.markdown
    st.write("""I build and use data to drive real-life decision making. My ambition is to produce 
    information which is meaningful to society. My profile is both within operations and technology. 
    This includes examples of using big data to identify & present opportunity, control waste-streams 
    & workflow optimisation. [>> My LinkedIn <<](http://www.linkedin.com/in/mwwoosey404)""")
    # st.write("[My LinkedIn >](http://www.linkedin.com/in/mwwoosey404)")

# what i do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("My Skillset")
        st.write("""
        I am passionate about delivering a great user experience. I am
        skilled in the below areas:
        - Programming in SQL, Python, VBA
        - Data Management with experience in PostgreSQL
        - Data Visualisation with Quicksight, Tableau, Seaborn
        - Data Arcitecture & Cloud Technologies (AWS)
        """)

    with right_column:
        st_lottie(data_img, height=300, key="coding")