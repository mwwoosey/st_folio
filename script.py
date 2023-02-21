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
lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_Jj1h5xMtEv.json")
img_mountain = Image.open("images/IMG_0306.jpg")

# header section
with st.container():
    st.subheader("Hi, I'm Michael :wave:")
    st.title("A Data Analyst based in the UK")
    st.write("I am passionate about finding ways to use Python and VBA to be more effective in business")
    st.write("[Learn More >](https://google.com)")

# what i do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("What I do")
        st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent varius, odio a lacinia auctor, massa massa pellentesque diam, a aliquet neque urna vitae magna. In feugiat, enim efficitur consequat blandit, risus nisi suscipit turpis, sit amet pharetra nisl tellus eget nunc. Quisque auctor erat dictum dolor efficitur varius. Praesent lacinia felis sit amet dolor ultrices suscipit scelerisque quis justo. Etiam vitae nulla malesuada, tristique neque ut, dictum lorem. Curabitur justo magna, aliquam sit amet tincidunt pulvinar, blandit ac dui. Nulla sed mauris sed felis convallis rutrum vitae nec elit.
        Praesent pharetra sapien sit amet malesuada tempus. Proin dapibus est lorem, id vestibulum lorem elementum at. Suspendisse id interdum leo, feugiat vehicula turpis. Morbi ac erat aliquam, fermentum lectus eu, posuere mauris. Fusce ac turpis quis arcu sagittis ullamcorper. Vivamus molestie vestibulum est sit amet semper. Sed sed ligula non eros ultrices accumsan. Maecenas condimentum volutpat erat quis mollis. Morbi cursus, dui sed dapibus vulputate, risus nisl laoreet lacus, rhoncus fermentum eros lorem ac nulla. Praesent congue enim id faucibus auctor.
        """)
        st.write("[LinkedIn >](http://linkedin.com)")

    with right_column:
        st_lottie(lottie, height=300, key="coding")

# my first, first project
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.write("yes")

    with text_column:
        st.subheader("Something blah")
        st.write("""
        Here is some information about something I did
        """)
        st.markdown("[Watch Video...](http://google.com)")