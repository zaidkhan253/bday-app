
import streamlit as st
import base64

st.set_page_config(layout="wide")

# Page background and audio player (shared function)
def set_background_and_audio(bg_path, audio_path):
    st.markdown(f'''
        <style>
            .stApp {{
                background-image: url("https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
        </style>
    ''', unsafe_allow_html=True)

    audio_file = open(audio_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3', autoplay=True)

# Define pages
def page1():
    set_background_and_audio("assets/music1.mp3", "assets/music1.mp3")
    st.markdown("<h1 style='text-align: center; color: white;'>Happieee birthdayyy Samiya, 🌹🎀💗<br>my best friend🙃😉 and my fav person!!😊😏</h1>", unsafe_allow_html=True)
    st.markdown("### ", unsafe_allow_html=True)
    if st.button("Press Here 🎉"):
        st.session_state.page = 2

def page2():
    set_background_and_audio("assets/music2.mp3", "assets/music2.mp3")
    st.markdown("<h3 style='color: pink;'>Thanku for being my bestfriend for so long and staying with me always* ;)...</h3>", unsafe_allow_html=True)
    if st.button("🐱 Click the Cat!"):
        st.session_state.page = 3

def page3():
    set_background_and_audio("assets/music3.mp3", "assets/music3.mp3")
    st.markdown("<h3 style='color: pink;'>donno until when we r together...<br>but i would love to be here always...<br>Hope everything will be fine and we never break our friendship samiya :)</h3>", unsafe_allow_html=True)
    if st.button("🐱 Cute Cat with Frog!"):
        st.session_state.page = 4

def page4():
    set_background_and_audio("assets/music4.mp3", "assets/music4.mp3")
    st.image("assets/image1.jpg", caption="🥰😉")
    if st.button("💐 Bouquet of White Roses"):
        st.session_state.page = 5

def page5():
    set_background_and_audio("assets/music5.mp3", "assets/music5.mp3")
    st.markdown("<h2 style='color: pink;'>once again wish you a very happy 20th birthdayy pgllll!!🎊🌹🎀💗🎉🥂🎆🎉🎂😽</h2>", unsafe_allow_html=True)
    if st.button("⭐ Star Button"):
        st.session_state.page = 6

def page6():
    set_background_and_audio("assets/music6.mp3", "assets/music6.mp3")
    st.image("assets/image2.jpg")
    st.markdown("<h3 style='color: pink;'>🎉🎀 End of the Surprise 🎀🎉</h3>", unsafe_allow_html=True)

# App logic
if 'page' not in st.session_state:
    st.session_state.page = 1

if st.session_state.page == 1:
    page1()
elif st.session_state.page == 2:
    page2()
elif st.session_state.page == 3:
    page3()
elif st.session_state.page == 4:
    page4()
elif st.session_state.page == 5:
    page5()
elif st.session_state.page == 6:
    page6()
