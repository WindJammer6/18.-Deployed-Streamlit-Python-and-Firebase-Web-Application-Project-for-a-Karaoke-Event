#In this file, we will look at how we can improve on the form we have created in '910. creating_a_form.py' in Streamlit 
#(Python)


import streamlit as st

#Using markdown widget to include HTML and CSS into Streamlit (Python) to align this header to the center
st.markdown("<h1 style='text-align: center;'> User Registration </h1>", unsafe_allow_html=True)

with st.form(key="Form 2", clear_on_submit=True):
    column1, column2 = st.columns(2)
    #st.text_input("First Name")
    first_name_field = column1.text_input(label="First Name")
    last_name_field = column2.text_input(label="Last Name")
    email_address_field = st.text_input("Email Address")
    password_field = st.text_input("Password")
    confirm_password_field = st.text_input("Confirm Password")
    

    #Splitting the form widget into 3 columns to get the user (short) text inputs of the day, month and time
    day, month, year = st.columns(3)
    day_field = day.text_input("Day")
    month_field = month.text_input("Month")
    year_field = year.text_input("Year")

    
    #Improving the 'submit button' of our form, telling it to be able to detect if the any of the fields in the form are
    #not filled, and give the warning using the 'st.warning()' function/widget, and a success feedback using the
    #'st.success()' function/widget
    submit_button_state = st.form_submit_button("Submit button")    #'st.form_submit_button()' returns a boolean, 'True' 
                                                                    #when clicked, 'False' when it us not clicked
    if submit_button_state is True:
        if first_name_field == "" or last_name_field == "" or email_address_field == "" or password_field == "" or confirm_password_field == "" or day_field == "" or month_field == "" or year_field == "":
            st.warning("Please fill the above fields")
        else:
            st.success("Form submitted successfully")

