import streamlit as st
from groq import Groq
st.title("Mychatbot")
cilent = Groq(api_key=st.secrets["GROQ_API_KEY"])
if "messages" not in st.session_state:
  st.session_state.messages = []
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.write(message["content"])
prompt_text = st.chat_input("write your text")
if prompt_text:
  st.session_state.messages.append({"role" : "user" , "content" : prompt_text})
  with st.chat_message("user"):
    st.write(pronpt_text)
    with st.chat_message("assistant"):
      with st.spinner("Thing..."):
         try:
           messages = [{"role" : "system" , "content" : "you are a helpful assistant "}]
           for msg in st.session_state.messages:
             messages.append({"role" : msg["role"] , "content" : msg["content"]})
             respon = cilent.chat.completions.create(
             model = "llama-3.3-70b-versatile",
             messages=messages,
             max_tokens = 5000,
             temperature = 1
            )
           answer = respon.choices[0].message.content
         except Exception as e:
           answer = str(e)
           st.write(answer)
           st.session_state,messages.append({"role" :  "assistant" , "content" : answer})
