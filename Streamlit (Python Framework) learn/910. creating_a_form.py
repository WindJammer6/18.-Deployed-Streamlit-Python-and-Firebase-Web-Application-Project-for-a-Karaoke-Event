#In this file, we will look at how to create a form in Streamlit (Python)


import streamlit as st

#The 'st.markdown()' Markdown widget allows you to use HTML and CSS context in Streamlit (Python), which can be done in
#this way. Make sure to set the 'unsafe_allow_html' parameter to be True instead of False.
st.markdown("<h1>User Registration</h1>", unsafe_allow_html=True)

#There are 2 ways to create a form in Streamlit (Python). 


#First way to create a form widget is to just continuously add in widgets into your web application to create your form:

#Some key things to look for when using 'st.form()' form widget:
#- The 'st.form()' form widget can only take 2 arguments, the 'key' and 'clear_on_submit' arguments.
#  -> the 'key' arguement is an optional string or integer to use as the unique key for the widget
#  -> the 'clear_on_submit' argument accepts a Boolean (True or False) value. If you set value to True, all the user inputs
#     will be cleared upon clicking the 'submit' button, and if you set it to False, all the user inputs will not be cleared 
#     upon clicking the 'submit' button

#- It is compulsory for it to have the 'key' parameter in it or else you will get an error prompting you to add the 
# 'key' parameter

#- When you first create this form with 'st.form()', you'll immediately get an error in your web application. The reason 
#  for this error is because every form widget needs a 'submit' widget accompanying it to make it complete, which can be
#  created with the function '[form object variable name].form_submit_button()'
form1 = st.form(key="Form 1", clear_on_submit=True)
form1.text_input(label="First Name")

form1.form_submit_button(label="Submit button")


#Second way to create a form widget is to create widgets into your form widget instead of the web application directly:

#Here is how the contnext work. You can split your form widget into different columns if you like via the 'st.columns()' 
#function/widget.
with st.form(key="Form 2", clear_on_submit=True):
    column1, column2 = st.columns(2)

    #If your form is without the columns 'column1' and 'column2' variables, you will need to create your 'st.text_input()' 
    #user (short) text widget in this manner instead
    #st.text_input("First Name")
    column1.text_input(label="First Name")
    column2.text_input(label="Last Name")
    st.text_input(label="Email Address")
    st.text_input(label="Password")
    st.text_input(label="Confirm Password")

    st.form_submit_button(label="Submit button")

