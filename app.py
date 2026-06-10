import streamlit as st
from groq import Groq
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.title("MY CHATBOT")

if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.write(message["content"])

prompt_text = st.chat_input("Write your message...")

if prompt_text:
  st.session_state.messages.append({"role" : "user", "content" : prompt_text})
  with st.chat_message("user"):
    st.write(prompt_text)










