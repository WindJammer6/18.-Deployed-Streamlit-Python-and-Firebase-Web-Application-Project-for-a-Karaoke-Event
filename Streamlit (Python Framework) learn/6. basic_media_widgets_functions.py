#Here are the basic media widget functions in Streamlit (Python)
# 1. st.image()
# 2. st.video()
# 3. st.audio()

import streamlit as st

#1. 'st.image()' function places an image into your web application
st.image("6.1. streamlit_image.jpg", caption="This is my image", width=680)

#2. 'st.video()' function places an video into your web application
st.video("6.2. streamlit_video.mp4", start_time=10)

#3. 'st.audio()' function places an audio into your web application
st.audio("6.3. streamlit_audio.mp3")