import streamlit as st
import groq from Groq
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.title("MyChatbot")
