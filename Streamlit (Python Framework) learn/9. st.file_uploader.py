import streamlit as st

st.title("Uploading Files")
st.markdown("---")


#'st.file_uploader()' allows a user to upload files in your web application. It can take many arguments, the most 
#important 3 are the 'label', 'type' and 'accept_multiple_files' arguments.
#   -> the 'label' argument is used to label the name of the checkbox
#   -> the 'type' argument accepts a string or a List of strings. It is used to specify the accepted file types (you can
#      google for the documentation for the names of the strings of the various file types accepted by this 'type' 
#      argument)
#   -> the 'accept_multiple_files' argument allows the file uploader to accept multiple files to be uploaded 
#      simultaneously
uploaded_image = st.file_uploader(label="This is the file uploader. Upload your file here. (Images only)", type=["jpg", "png"])
if uploaded_image is not None:
    st.image(uploaded_image)            #Displaying the uploaded image onto your web application

uploaded_audio = st.file_uploader(label="This is the file uploader. Upload your file here. (Audio only)", type="mp3")
if uploaded_audio is not None:
    st.audio(uploaded_audio)            #Displaying the uploaded audio onto your web application

uploaded_video = st.file_uploader(label="This is the file uploader. Upload your file here. (Videos only)", type="mp4")
if uploaded_video is not None:
    st.video(uploaded_video)            #Displaying the uploaded video onto your web application


#Demonstrating how the 'accept_multiple_files' argument is used in the 'st.file_uploader()' function widget
uploaded_image_list = st.file_uploader(label="This is the file uploader. Upload your files here. (Images only)", type=["jpg", "png"], accept_multiple_files=True)
if uploaded_image_list is not None:
    for image in uploaded_image_list:
        st.image(image)                 #Displaying the uploaded images onto your web application