#Here are the basic interactive widget functions in Streamlit (Python)
# 1. st.checkbox() (Checkbox widget (does not allow multiple options))
# 2. st.button() (Button widget (does not allow multiple options))
# 3. st.radio() (Radio button widget, basically a MCQ widget (allows multiple options))
# 4. st.selectbox() (Select/Dropdown box widget (allows multiple options))
# 5. st.multiselect() (Multiple Select/Dropdown box widget (allows multiple options))

import streamlit as st

#1. 'st.checkbox()' checkbox widget can take many arguments, the most important 4 are the 'label', 'value' 'on_change' 
#   and 'key' arguments.
#   -> the 'label' argument is used to label the name of the checkbox
#   -> the 'value' argument is used to specify the initial or default state of the checkbox. This parameter allows you 
#      to set whether the checkbox is initially checked (selected) or unchecked (deselected) when it is first displayed 
#      in your Streamlit app. The 'value' parameter accepts a Boolean (True or False) value. If you set value to True, 
#      the checkbox will be initially checked, and if you set it to False, the checkbox will be initially unchecked.
#   -> the 'on_change' argument allows you to do a 'WidgetCallback', which is basically a function that will be called 
#      in responce to changes in the state of a widget, such as a button, checkbox, slider, or any other interactive 
#      element.
#   -> the 'key' arguement is an optional string or integer to use as the unique key for the widget
def indicate_change():
    print("Checkbox Changed")            #printing the string 'printed' in the terminal whenever the checkbox is clicked

#'st.checkbox("Checkbox")' works similarly as well without having to specify the 'label=' argument
checkbox_state = st.checkbox(label="Checkbox", value=True, on_change=indicate_change)

if checkbox_state is True:               #'if checkbox_state:' works too
    st.write("You checked the checkbox!")
else:
    pass


#   Apparently you can do this too, where when you check the checkbox, Streamlit (Python) will print 'True' in the terminal
#   and 'False' when you uncheck the checkbox. This code makes use of the 'st.session' function, and the '.checker' is not 
#   a function, it just needs to be the same as the input at the 'key' argument in the 'st.checkbox()' widget function in
#   order for this to work
def indicate_change2():
    print(st.session_state.checkbox_checker)

checkbox_state2 = st.checkbox(label="Checkbox", value=True, on_change=indicate_change2, key="checkbox_checker")

#   This will work too:
#   def indicate_change2():
#         print(st.session_state.a)

#   state = st.checkbox(label="Checkbox", value=True, on_change=indicate_change2, key="a")




#2. 'st.button()' button widget can take many arguments, the most important 2 are the 'label' and 'on_click' arguments
#   -> the 'label' argument is used to label the name of the button button widget
#   -> the 'on_click' argument allows you to do a 'WidgetCallback', which is basically a function that will be called 
#      in responce to changes in the state of a widget, such as a button, checkbox, slider, or any other interactive 
#      element
def indicate_clicked():
    print("Button Clicked")

button = st.button(label="Button", on_click=indicate_clicked)




#3. 'st.radio()' radio button widget (basically a MCQ widget) can take many arguments, the most important 4 are the 
#   'label', 'options', 'on_change' and 'key' arguments.
#   -> the 'label' argument is used to label the name of the radio button widget
#   -> the 'options' argument takes in a tuple, with each element in the tuple being a option in the radio button (MCQ
#      widget)
#   -> the 'on_change' argument allows you to do a 'WidgetCallback', which is basically a function that will be called 
#      in responce to changes in the state of a widget, such as a button, checkbox, slider, or any other interactive 
#      element
#   -> the 'key' arguement is an optional string or integer to use as the unique key for the widget
def indicate_change3():
    print(st.session_state.radio_button_checker)

radio_button = st.radio(label="Which country do you live in?", options=("US", "UK", "Canada"), on_change=indicate_change3, key="radio_button_checker")
print(radio_button)




#4. 'st.selectbox()' selectbox button widget (basically a MCQ widget) can take many arguments, the most important 4 are the 
#   'label', 'options', 'on_change' and 'key' arguments.
#   -> the 'label' argument is used to label the name of the select box button widget
#   -> the 'options' argument takes in a tuple, with each element in the tuple being a option in the select box widget
#   -> the 'on_change' argument allows you to do a 'WidgetCallback', which is basically a function that will be called 
#      in responce to changes in the state of a widget, such as a button, checkbox, slider, or any other interactive 
#      element
#   -> the 'key' arguement is an optional string or integer to use as the unique key for the widget
select_box = st.selectbox(label="What is your favourite car?", options=("Audi", "BMW", "Ferrari"))
print("You have selected", select_box, "!")




#5. 'st.multiselect()' multi-select box widget can take many arguments, the most important 4 are the 'label', 'value', 
#   'on_change' and 'key' arguments.
#   -> the 'label' argument is used to label the name of the multi-select box widget
#   -> the 'options' argument takes in a tuple, with each element in the tuple being a option in the multi-select box
#   -> the 'on_change' argument allows you to do a 'WidgetCallback', which is basically a function that will be called 
#      in responce to changes in the state of a widget, such as a button, checkbox, slider, or any other interactive 
#      element
#   -> the 'key' arguement is an optional string or integer to use as the unique key for the widget
multi_select_box = st.multiselect(label="What is your favourite Tech Brand", options=("Amazon", "Apple", "Microsoft", "Oracle"))
st.write(multi_select_box)