import streamlit as st
from groq import Groq
import tempfile, os

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
  with st.chat_message("assistant"):
    with st.spinner("جاري التفكير..."):
      try:
        messages = [{"role" : "system" , "content" : "You are a helpful assistant."}]
        for msg in st.session_state.messages:
          messages.append({"role" : msg["role"], "content" : msg["content"]})
        response = client.chat.completions.create(
          model="llama-3.3-70b-versatile",
          messages=messages,
          max_tokens=500,
          temperature=0.7
        )
        answer = response.choices[0].message.content
      except Exception as error:
        answer = f"خطأ {str(error)}"
    st.write(answer)
  st.session_state.messages.append({"role" : "assistant", "content" : answer})
        

st.markdown("---")
st.markdown("Speak")
audio = st.audio_input("Start your audio")

if audio:
  if st.button("Send"):
    with st.spinner("جاري تحويل صوتك إلى نص..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(audio.read())
                path = tmp.name
            try:
                with open(path, "rb") as f:
                    transcript = client.audio.transcriptions.create(
                        model="whisper-large-v3",
                        file=(os.path.basename(path), f),
                        response_format="text"
                    )
            finally:
              os.unlink(path)
        
        
        
      














        
