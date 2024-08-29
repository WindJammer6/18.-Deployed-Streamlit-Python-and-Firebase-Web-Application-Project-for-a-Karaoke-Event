#Here are the basic text functions/syntax in Streamlit (Python)
# 1. st.title()
# 2. st.header()
# 3. st.subheader()
# 4. st.text()

#(There are some minor differences between the 'st.header' and 'st.subheader' functions)


import streamlit as st

st.title("Hi, I am the title")
st.header("Hi , I am a header")
st.subheader("Hi, I am the subheader")

st.text("Hi, I am the 'text' function. Here is the text: Lorem ipsum dolor sit amet, \nconsectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore \nmagna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris \nnisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in \nvoluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint \noccaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id \nest laborum.")
