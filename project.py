import streamlit as st
st.title("welcome to dt12-demo session") 
name=st.text_input("Enter your name: ")
B=st.button("submit")
if B:
    st.write(f"Hi {name},welcome to dt12")
    

