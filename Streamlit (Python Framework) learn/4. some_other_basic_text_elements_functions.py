#Here are some other basic text functions in Streamlit (Python)
# 1. st.markdown()
# 2. Some other basic text syntax
# 3. st.latex() (creating LaTeX in Streamlit (Python))
# 4. st.json() (creating json (JavaScript Object Notation) in Streamlit (Python))
# 5. st.code() (creating code snippets in Streamlit (Python))

import streamlit as st

#1. The 'st.markdown()' function is used to render and display text content with Markdown formatting. Markdown 
#   is a lightweight markup language that allows you to format text, create headings, lists, links, and more using 
#   plain text. 
st.markdown("Hello world")


#2. Some other basic text syntax in Streamlit (Python). The documentation to these other 
#   basic text syntax can be found here: https://www.markdownguide.org/cheat-sheet/
st.markdown("**This is in bold** *This is in italics*")

st.markdown("# Header 1")
st.markdown("## Header 2")
st.markdown("### Header 3")

st.markdown("> This is Blockquote")

st.markdown("---")                      #Creates a horizontal line

st.markdown("[This is Google's Link](https://www.google.com)")

st.markdown("`code`")                   #Creates code-format


#3. Creating LaTeX. LaTeX is a typesetting system and markup language used for document preparation, 
#   particularly in the fields of academia, science, and technical writing. It is widely used to create 
#   documents with complex formatting, such as research papers, theses, academic articles, books, and 
#   technical reports. The documentation to these other LaTeX syntax can be found here: 
#   https://katex.org/docs/supported
st.latex(r"\begin{pmatrix} a & b \\ c & d \end{pmatrix}")
st.latex(r"\begin{matrix} a & b \\ c & d \end{matrix}")


#4. Creating json. JSON, which stands for "JavaScript Object Notation," is a lightweight data interchange 
#   format that is easy for humans to read and write, and easy for machines to parse and generate. It is a
#    text-based data format that is often used to transmit data between a server and a web application, or
#    between different parts of an application. 
json_object = {"a":"1,2,3", "b":"4,5,6"}
st.json(json_object)


#5. Creating code snippets. The 'st.code(string, programming_language)' function takes in 2 arguments, the 
#   first argument is the string input variable which will be the code itself, and the second argument is
#   the type of programming language the code is supposed to be in
code = """
def func():
    return 0;

print("Hello world")
print(func())
"""
st.code(code, language="python")
