#Here are the basic display functions in Streamlit (Python) 
# 1. st.write()
# 2. st.metric()
# 3. st.table()
# 4. st.dataframe()

import streamlit as st
import pandas as pd


#1. 'st.write()' function is a versatile and user-friendly method for displaying content, whether it's text, 
#   data, or visual elements. It is designed to automatically adapt to the type of data you provide and render 
#   it accordingly. 

#   The similarity between 'st.write()' and 'st.markdown()' is that both are used to display text and content 
#   in your app, but they have different purposes and formatting options. However, they are different as 
#   'st.markdown()' is can only be used for rendering text content with Markdown formatting][], while
#   'st.write()' is a very versatile function for displaying content in Streamlit (Python) as it can 
#   automatically adapt to the type of data you pass to it and renders it accordingly (such as to display 
#   text, numbers, dataframes, charts, and more.)
st.write("## H2")

st.write("[This is Google's Link](https://www.google.com)")

st.write("`code`")

#Comparing 'st.write' and 'st.markdown' in this context 
json_object = {"a":"1,2,3", "b":"4,5,6"}
st.write(json_object)
st.markdown(json_object)

#   (About 'st.write()' function on LaTeX expressions: apparently 'st.write()' function can also create LaTeX 
#   expressions, but I'm not sure how to do it)


#2. 'st.metric()' function creates a metric in your web application. A metric is a quantifiable measurement 
#   used to assess, compare, and track the performance, status, or characteristics of a system, process, 
#   project, or entity. 'st.metric()' takes in 4 arguments in the form of,
#       'st.metric(label, value, delta=None, delta_color="normal")'

#   - 'label' represents the heading of the metric
#   - 'value' represents the current value of the metric
#   - 'delta' represents the change of that value in the 'value' argument
#   - 'delta_color' represents the colour of the text of the 'delta' argument being displayed in the web
#     web application. It only accepts: 'normal', 'inverse', or 'off'
st.metric(label="Wind Speed", value="120m/s", delta="1.4m/s")
st.metric(label="Wind Speed", value="120m/s", delta="-1.4m/s")
st.metric(label="Wind Speed", value="120m/s", delta="1.4m/s", delta_color="off")


#3. 'st.table()' function is used to display uninteractable tabular data
imported_pandas_data = pd.DataFrame({"Column 1" : [1,2,3,4,5,6,7], "Column 2" : [11,12,13,14,15,16,17]})
st.table(imported_pandas_data)


#4. 'st.dataframe()' function is used to display interactable tabular data (in the sense that you can click 
#   on the column headers in your dataframe in your web applciation to reverse sort the order of the column
#   data) 
imported_pandas_data = pd.DataFrame({"Column 1" : [1,2,3,4,5,6,7], "Column 2" : [11,12,13,14,15,16,17]})
st.dataframe(imported_pandas_data)