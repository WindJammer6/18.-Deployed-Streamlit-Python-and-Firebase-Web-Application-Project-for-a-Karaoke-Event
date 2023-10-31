from firebase_admin import db
import firebase_admin
import streamlit as st


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
    credentials_object = firebase_admin.credentials.Certificate("firebase_key.json")
    firebase_admin.initialize_app(credentials_object, {
        'databaseURL': 'https://karaokeeventproject-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

# Get a reference to the database
reference_to_database = db.reference('/')
 
# Read data from the Realtime Database from Firebase
print(reference_to_database.get())


#/////////////////////////////////////////////////////////////////////////


#FRONTEND - Streamlit (Python) app side of things...

st.image(image="karaoke_poster.svg", width=680)
st.header("🎶 Add Your Name and Your Song Choice! 🎶")
st.markdown("If you accidentally added yourself into the song queue and wish to remove yourself from the queue, please message Jet Wei (@Jetwei) or Siddharth (@musicbysid) on telegram!")


########################################################
#ABOUT STREAMLIT (PYTHON)'S 'ST.SESSION_STATE' FUNCTION#
########################################################
#The 'st.session_state' function in Streamlit (Python) allows you to store and access session-specific data in your 
#Streamlit (Python) web applications. It provides a way to maintain state across widget interactions, making it 
#easier to build dynamic and interactive applications.

#Functionality of the 'st.session_state' function in Streamlit (Python):
#-> Store Data: You can use 'st.session_state' function to store data as key-value pairs during the lifetime of a 
#   session. For example, you might store user input, flags, or other session-specific information.
#-> Access Data: You can access the stored data throughout your Streamlit app. This allows you to access and modify 
#   session-specific variables as needed.
#-> Preserve State: Data stored in st.session_state is preserved across interactions. This means that even if the 
#   user interacts with widgets and the script re-runs, the session-specific data remains available and consistent.

#Here are the 'st.session_state' stuffs from Streamlit (Python) (pretty complicated stuff tbh) but its needed for 
#the confirmation function to work. Here are the learning sources on Streamlit (Python)'s 'st.session_state' function I 
#referred to: 
#- https://docs.streamlit.io/library/api-reference/session-state (Streamlit (Python)'s official documentation on
#  the 'st.session_state' function)
#- https://www.youtube.com/watch?v=92jUAXBmZyU) (Youtube video labekled 'Session State Basics' by Streamlit Youtube)

#Uncomment the below code to see the 'st.session_state' for each of the button 
#widget's session states.
# st.session_state object:", st.session_state
st.session_state["Button2"] = False


#Character count limit added to prevent any overlapping of the text displays in the song queue Streamlit (Python) 
#web application
name = st.text_input("Name: ", max_chars=10)
song_choice = st.text_input("Song choice: ", max_chars=25)
song_artist = st.text_input("Song artist: ", max_chars=20)

button_state = st.button(label="Submit", key="button1")


if button_state:
    if name == "" or song_choice == "" or song_artist == "":
        st.warning("Please fill up all the above fields!")
    else:
        #Confirm submission functionality
        st.write("Confirm?")
        st.write("Name: ", name)
        st.write("Song choice: ", song_choice)
        st.write("Song artist: ", song_artist)

        button_state2 = st.button(label="Confirm Submit", key="button2")
        if button_state2:
            st.session_state["button2"] = True

        #Not confirm submission functionality
        button_state3 = st.button(label="Back", key="button3")
        if button_state3:
            pass

#If confirmation submit button is pressed in the Streamlit (Python) web application, the program will 'push' 
#basically add this new pieces of user data into the Realtime database in Firebase
if "button2" in st.session_state:
    if st.session_state["button2"] == True:     
        reference_to_database.push({"name" : name, "song_choice" : song_choice, "song_artist" : song_artist})    
        st.success("You have been added to the song queue! It might take some time for your name to appear on the screen. Please give others a chance before adding yourself to the song queue again!")

# Read updated Realtime Database in Firebase and printing it in the terminal for debugging purposes
print(reference_to_database.get())
