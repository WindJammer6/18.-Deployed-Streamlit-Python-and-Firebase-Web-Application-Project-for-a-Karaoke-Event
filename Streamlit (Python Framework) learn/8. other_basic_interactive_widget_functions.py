#Here are some other basic interactive widget functions in Streamlit (Python)
# 1. st.slider() ((number) slider widget)
# 2. st.select_slider() (select slider widget)
# 3. st.text_input() (user (short) text input widget)
# 4. st.text_area() (user (long) text input widget)
# 5. st.date_input() (user date input widget)
# 6. st.time_input() (user time input widget)
# 7. st.progress() (progress bar widget)


import streamlit as st
import datetime
import time

#1. 'st.slider()' (number) slider widget can take many arguments, the most important 5 are the 'label', 'value' 'min_value' 
#   'max_value' and 'step' arguments.
#   -> the 'label' argument is used to label the name of the slider
#   -> the 'value' argument is used to specify the initial or default value of the slider. This parameter allows you 
#      to set at which value the slider is initially at when it is first displayed in your Streamlit app
#   -> the 'min_value' argument sets the smallest value on the (number) slider widget
#   -> the 'max_value' argument sets the largest value on the (number) slider widget
#   -> the 'step' argument sets the gap between the value of the options on the (number) slider
current_value = st.slider(label="This is a (number) slider", value=6, min_value=2, max_value=10, step=2)
st.write(current_value)



#2. 'st.select_slider()' select slider widget can take many arguments, the most important 3 are the 'label', 'options' 
#   and 'value' arguments.
#   -> the 'label' argument is used to label the name of the select slider widget
#   -> the 'options' argument takes in a tuple, with each element in the tuple being a option in the select slider widget
#   -> the 'value' argument is used to specify the initial or default value of the select slider. This parameter allows 
#      you to set at which value the select slider is initially at when it is first displayed in your Streamlit app
current_value2 = st.select_slider(label="This is a select slider", options=("Very Unhappy", "Unhappy", "Neutral", "Happy", "Very Happy"), value="Neutral")
st.write(current_value2)



#3. 'st.text_input()' user (short) text input widget can take many arguments, the most important 3 are the 'label', 'value' 
#   and 'max_char' arguments.
#   -> the 'label' argument is used to label the name of the user (short) text input widget
#   -> the 'value' argument is used to specify the initial or default value of the user (short) text input widget. This 
#      parameter allows you to set at which value the user (short) text input widget is initially at when it is first 
#      displayed in your Streamlit app
#   -> the 'max_chars' argument is used to set the maximum number of characters the user can put into the user (short)
#      text input widget
user_text_input = st.text_input(label="This gets the user's text input", max_chars=50)
st.write(user_text_input)



#4. 'st.text_area()' user (long) text input widget can take many arguments, the most important 3 are the 'label', 'value' 
#   and 'max_char' arguments.
#   -> the 'label' argument is used to label the name of the user (long) text input widget
#   -> the 'value' argument is used to specify the initial or default value of the user (long) text input widget. This 
#      parameter allows you to set at which value the user (long) text input widget is initially at when it is first 
#      displayed in your Streamlit app
#   -> the 'max_chars' argument is used to set the maximum number of characters the user can put into the user (long)
#      text input widget

#- This difference between the 'st.text_input()' and 'st.text_area()' widgets is that 'st.text_input()' creates a small
#  text box for user input in your web application while 'st.text_area()' creates a large text box for user input in your
#  web application)

#- For 'st.text_area()', the user need to press 'ctrl' + 'enter' in order to submit their response. (cuz 'enter' is used 
#  to go to next line in the large text box) If they only click 'enter', they will be prompted by the widget to press
#  'ctrl' + 'enter' instead
user_text_area_input = st.text_area(label="This gets the user's text area input", max_chars=300)
st.write(user_text_area_input)



#5. 'st.date_input()' user date input widget can take many arguments, the most important 4 are the 'label', 'value',
#   'min_value' and 'max_value' arguments.
#   -> the 'label' argument is used to label the name of the user date input widget
#   -> the 'value' argument is used to specify the initial or default date of the user date input widget. This parameter 
#      allows you to set at which date the user date input widget is initially at when it is first displayed in your 
#      Streamlit app
#   -> the 'min_value' argument sets the oldest date option on the user date input widget
#   -> the 'max_value' argument sets the furthest (into the future) date option on the user date input widget

#- Note that the 'value', 'min_value' and 'max_value' arguments only accept Python's datetime module's 'datetime.date()'
#  objects as input
min_date = datetime.date(2022, 12, 31)
max_date = datetime.date(2023, 12, 31)
default_date = datetime.date(2023, 10, 12)          #can use this to replace the value parameter
user_date_input = st.date_input(label="This gets the user's date input", value="today", min_value=min_date, max_value=max_date)
st.write(user_date_input)



#6. 'st.time_input()' user time input widget can take many arguments, the most important 2 are the 'label' and 'value',
#   'min_value' and 'max_value' arguments.
#   -> the 'label' argument is used to label the name of the user time input widget
#   -> the 'value' argument is used to specify the initial or default time of the user time input widget. This parameter 
#      allows you to set at which time the user time input widget is initially at when it is first displayed in your 
#      Streamlit app

#- Note that the 'value' argument only accept Python's datetime module's 'datetime.time()' objects as input

#- The 'time' shown in this user time input widget represents the current clock time (rather than like a countdown clock
#  sort of time)
default_time = datetime.time(11,30,00)                  #'default_time = datetime.time(11,30)' (basically 11:30) or 
                                                        #'default_time = datetime.time(11)' (basically 11:00) works too
user_time_input = st.time_input(label="This gets the user's time input", value=default_time)
st.write(user_time_input)



#7. 'st.progress()' progress bar widget can take many arguments, the most important 2 are the 'value' and 'text' arguments.
#   -> the 'value' argument is used to specify the progress value for the progress bar
#   -> the 'text' argument is used to provide a text label or description that appears next to the progress bar
# 
#- The most common usage of progress bar widgets is when you link it to show progress of activity which the program is 
#  undertaking. 

#- For some reason, the 'text' argument's input just doesn't apoear in the web application

#- Here is how you link the progress bar widget to a button widget
def start_progress_bar_function(): 
    progress_bar = st.progress(10, "Hi")    #Here is the progress bar, which will appear when the button widget (see below)
    for i in range(10):                     #is pushed
        progress_bar.progress((i+1)*10)
        time.sleep(1)

start_progress_bar_button = st.button(label="Start the progress bar by pushing this button!", on_click= start_progress_bar_function)


