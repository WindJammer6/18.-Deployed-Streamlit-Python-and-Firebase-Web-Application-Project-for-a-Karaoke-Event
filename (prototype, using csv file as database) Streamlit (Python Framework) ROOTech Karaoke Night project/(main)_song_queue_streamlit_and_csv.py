#Idea of this Streamlit (Python) Web Application Karaoke Event is to create 3 seperate files:
#1. First is a streamlit app to get user input for their song choice and to indicate interest to add to queue 
#   ('(main)_karaoke_singer_registration_streamlit_and_csv.py')
#2. Second in a database to load their inputs into ('database.csv')
#3. Third is a streamlit app that displays the queue on the karaoke projector screen in a graphing/figure format
#   ('(main)_song_queue_streamlit_and_csv.py')


#//////////////////////////////////////////////////////////////////////////////


#This is app '3. Third is the streamlit app that displays the queue on the karaoke projector screen in a 
#graphing/figure format'
import streamlit as st
import pandas as pd
import random
from queue_data_structure_class import Queue
from karaoke_singer_class import KaraokeSinger


#//////////////////////////////////////////////////////////////////////////////


#BACKEND - With csv file and Pythonic commands side of things...

#Using ChatGPT
def get_random_element(my_list):
    """
    Returns a random element from the input list.
    
    Args:
    my_list (list): The list from which to choose a random element.
    
    Returns:
    A random element from the input list.
    """
    if not my_list:
        return None  # Return None if the list is empty
    else:
        return random.choice(my_list)

# # Example usage:
# my_list = [1, 2, 3, 4, 5]
# random_element = get_random_element(my_list)
# print("Random Element:", random_element)

database = pd.read_csv("database.csv")
print(database)

queue = Queue()

#Loading the csv file contents into the Queue Data Structure, enqueueing the person at the top of the database first 
#(to show that he will be the next singer)
for index, row in database.iterrows():
    user = KaraokeSinger(row['name'], row['song_choice'])
    queue.enqueue(user)
print(queue)


#/////////////////////////////////////////////////////////////////////////


#FRONTEND - Streamlit (Python) app side of things...

st.markdown("<h1 style='text-align: center;'> 🔥🔥Song Queue🔥🔥 </h1>", unsafe_allow_html=True)
st.markdown("---")


music_emojis = ["🎵", "🎶", "🎤", "🎧", "🎸", "🥁", "🎺", "🎷", "🎻", "🎹", "🎼", "🎤🎸", "🎶🕺", "🕺💃", "🎵🎤", "🎤🎵", "🎤🎸", "🎷🎶", "🎹🎵", "🎶🎵", "🎵🔊", "🎚️"]
column1, column2 = st.columns(2)

with column1:
    st.write("### *Next Singer🎤*")
    for i in reversed(queue.buffer):
        st.write(i.name, get_random_element(music_emojis))

with column2:
    st.write("### *Song choice🎶*")
    for i in reversed(queue.buffer):
        st.write(i.song_choice)
