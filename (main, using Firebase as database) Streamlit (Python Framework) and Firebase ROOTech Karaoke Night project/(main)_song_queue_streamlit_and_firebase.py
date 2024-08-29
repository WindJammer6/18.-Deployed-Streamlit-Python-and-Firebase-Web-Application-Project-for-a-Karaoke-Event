from firebase_admin import db
import firebase_admin
import streamlit as st
from queue_data_structure_class import Queue
from karaoke_singer_class import KaraokeSinger

#This is an imported function from some guy from Github who managed to create an 'autorefresh' functionality of 
#Streamlit (Python) web applications. 'st_autorefresh()' is the command from the self-made library 
#'streamlit_autorefresh' that allows us to do this.
#(Link: https://github.com/kmcgrady/streamlit-autorefresh#how-does-this-component-help (kmcgrady, Ken McGrady))
from streamlit_autorefresh import st_autorefresh


#//////////////////////////////////////////////////////////////////////////////


#BACKEND - With csv file and Pythonic commands side of things...

#Here is the link that goes directly to this ROOTech Karaoke Event project's Firebase Realtime database:
#https://console.firebase.google.com/u/0/project/karaokeeventproject/firestore 


#This if statement, accompanied by the condition with the function 'firebase_admin._apps', is used to prevent
#any error from creating multiple Firebase apps with the same name. 
 
#The 'firebase_app = firebase_admin.initialize_app' within this if statement will instantiate a Firebase app 
#if it is not already created, which is what the 'firebase_admin._apps' does, as an internal variable that 
#keeps track of the initialized Firebase apps. It is a dictionary-like object that holds information about 
#the Firebase apps that have been initialized in your Python application.
if not firebase_admin._apps:
    # Initialize Firebase
    credentials_object = firebase_admin.credentials.Certificate('karaokeeventproject-firebase-adminsdk-bto3h-502b60b589.json')
    firebase_admin.initialize_app(credentials_object, {
        'databaseURL': 'https://karaokeeventproject-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

# Get a reference to the database
reference_to_database = db.reference('/')

##########################
#THE AUTOREFRESH FUNCTION#
##########################
#Here is the 'st_autorefresh' function from the self-made library 'streamlit_autorefresh' created by Ken McGrady
#on Github that allows autorefresh functionality of the Streamlit (Python) web application

# 'st_autorefresh()' function's parameters:
# -> interval: int. 
#    - Amount of time in milliseconds to limit
# -> limit: int or None. 
#    - Amount of refreshes to allow. If none, it will refresh infinitely. While infinite refreshes sounds nice, 
#      it will continue to utilize computing resources.
# -> debounce: boolean.
#    - Whether to delay the autorefresh when user interaction occurs. Defaults to True in order to avoid 
#      refreshes interfering with interaction effects on scripts.
# -> key: str or None.
#    - An optional key that uniquely identifies this component. If this is None, and the component's arguments 
#      are changed, the component will be re-mounted in the Streamlit frontend and lose its current state. 
st_autorefresh(interval=10000, key="dataframerefresh")

# Read data from the Realtime Database from Firebase
database_data = reference_to_database.get()
print(database_data)

queue = Queue()

for i in database_data:
    print(database_data[i]['name'])
    print(database_data[i]['song_choice'])
    user = KaraokeSinger(database_data[i]['name'], database_data[i]['song_choice'], database_data[i]['song_artist'])
    queue.enqueue(user)
print(queue)


#/////////////////////////////////////////////////////////////////////////


#FRONTEND - Streamlit (Python) app side of things...

#In the database in Firebase I decided to maintain a 'placeholder' data storing the string 'placehold' as my 
#program will crash if there is no data in the database in Firebase. Hence 'queue' Queue Data Structure will
#always minimumly have at least the 1 default 'placeholder' data

#If there is more than 1 item in the Queue 
if len(queue.buffer) > 1:
    current_singer_and_song_choice = queue.buffer[-2]

    st.markdown("<h1 style='text-align: center; font-size: 60px;'> 🔥𝓢𝓸𝓷𝓰 𝓠𝓾𝓮𝓾𝓮🔥 </h1>", unsafe_allow_html=True)
    st.markdown("---")

    print(current_singer_and_song_choice.name)

    #Creating the 'Current Singer' and 'Current song being played' display widgets
    column1, column2 = st.columns(2)
    with column1:
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; font-size: 30px; font-style: italic;'> ✨In the Spotlight✨ </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; font-size: 65px;'> {current_singer_and_song_choice.name} </h1>", unsafe_allow_html=True)

    with column2:
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; font-size: 30px; font-style: italic;'> 🎧You're listening to🎧 </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; font-size: 65px;'> {current_singer_and_song_choice.song_choice} </h1>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: left; font-size: 30px; font-style: italic;'> By: {current_singer_and_song_choice.song_artist} </h3>", unsafe_allow_html=True)

    #Creating the 'Next Singers' and 'Next song choices and the respective song artists' song queue display widgets
    zcolumn1, zcolumn2 = st.columns(2)
    with zcolumn1:
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; font-style: italic; font-size: 30px;'> Next Singer🎤 </h3>", unsafe_allow_html=True)
        for i in reversed(queue.buffer):
            #To filter out the 'placehold' placeholder input to not it to be displayed in the song queue 
            #Streamlit (Python) web application
            if i.name != "placehold":
                st.markdown(f"<p style='text-align: left; font-size: 25px;'> {i.name} </p>", unsafe_allow_html=True)

    with zcolumn2:
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; font-style: italic; font-size: 30px;'> Song choice🎶 </h3>", unsafe_allow_html=True)
        for i in reversed(queue.buffer):
            if i.song_choice != "placehold":
                st.markdown(f"<p style='text-align: left; font-size: 25px;'> {i.song_choice} [{i.song_artist}] </p>", unsafe_allow_html=True)
    

#If length is 1 or less (the 1 being the 'placeholder' data, so we are not count that, then these code creates the 
#'if-there-is-currently-no-users-in-song-queue' page)
else:
    st.markdown("<h1 style='text-align: center; font-size: 60px;'> 🔥𝓢𝓸𝓷𝓰 𝓠𝓾𝓮𝓾𝓮🔥 </h1>", unsafe_allow_html=True)
    st.markdown("---")

    #Creating the 'Current Singer' and 'Current song being played' display widgets
    column1, column2 = st.columns(2)
    with column1:
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; font-size: 30px; font-style: italic;'> ✨In the Spotlight✨ </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; font-size: 65px;'> - </h1>", unsafe_allow_html=True)
        
    with column2:
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; font-size: 30px; font-style: italic;'> 🎧You're listening to🎧 </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; font-size: 65px;'> - </h1>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: left; font-size: 30px; font-style: italic;'> By: - </h3>", unsafe_allow_html=True)

    #Creating the 'Next Singers' and 'Next song choices and the respective song artists' song queue display widgets
    zcolumn1, zcolumn2 = st.columns(2)
    with zcolumn1:
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; font-style: italic; font-size: 30px;'> Next Singer🎤 </h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: left; font-size: 25px;'> - </p>", unsafe_allow_html=True)

    with zcolumn2:
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; font-size: 65px;'> \n </h1>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; font-style: italic; font-size: 30px;'> Song choice🎶 </h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: left; font-size: 25px;'> - </p>", unsafe_allow_html=True)
