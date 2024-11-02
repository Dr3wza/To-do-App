import streamlit as st
import Functions

todos = Functions.get_todos()

st.title("My Todo App")
st.subheader("This app aims to boost productivity")
st.write("Created by Dr3wza")

for todo in todos:
    st.checkbox(todo)

st.text_input(placeholder="Enter a todo...", label="")
