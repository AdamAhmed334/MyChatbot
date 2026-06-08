import streamlit as st
from groq import Groq
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.title("MyChatbot")
if "messages" is not st.session_state:
  st.session_state.messages = []
