#Here are what we will be learning to display in Streamlit (Python)
# 1. st.sidebar.[enter widget name here (e.g. radio, checkbox, write, etc.)]()
# 2. st.write([variable name storing the matplotlib figure]) 

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#1. Creating a side bar using the 'st.sidebar.[enter widget name here (e.g. radio, checkbox, etc.)]() widget
st.sidebar.write("This is a side bar")
radio_option_chosen = st.sidebar.radio(label="Select a graph type", options=["Line Graph", "Bar Graph", "H-bar Graph"])



#2. Creating a matplotlib figure using the 'st.write([variable name storing the matplotlib figure]) ' widget
#'np.linspace' is a function provided by the NumPy library that is used to create an array of evenly spaced values over a 
#specified range. It is particularly useful when you want to generate a sequence of values that are evenly spaced, which 
#can be helpful in various numerical and scientific computing applications.
x = np.linspace(0,10,100)
bar_x = np.array([1,2,3,4,5])           #whats this for??? and why the bar graph and h-bar graphs need this?

if radio_option_chosen == "Line Graph":
    figure = plt.figure()

    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x), "--")
    
    #Dont do 'plt.show()' here!! You will get an error messgae: 
    #   'UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.'
    #   plt.show()

    #If you want your graph/figure/chart drawn by matplotlib to show up in your Streamlit (Python) web application, you 
    #just have to do this:
    st.write(figure)


#Creating the 2 other Graphs in the Streamlit (Python) web application when their options are selected in the radio 
#button widget, the 'Bar Graph' and 'H-bar Graph' respectively 

#Creating a bar graph for the "Bar Graph" option
elif radio_option_chosen == "Bar Graph":
    figure = plt.figure()

    plt.bar(bar_x, bar_x*10)
    st.write(figure)

#Creating a h-bar graph for the "H-bar Graph" option
elif radio_option_chosen == "H-bar Graph":
    figure = plt.figure()

    plt.barh(bar_x*10, bar_x)
    st.write(figure)