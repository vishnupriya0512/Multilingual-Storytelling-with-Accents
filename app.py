import streamlit as st
from gtts import gTTS
from IPython.display import Audio
import os
import openai
from io import BytesIO
#from openai import GPT, Completion

# Initialize OpenAI GPT-3.5-turbo model
openai.api_key = "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"
client = openai.Client(api_key=openai.api_key)

#gpt = GPT(engine="davinci", api_key=openai.api_key)

# Function to translate text using OpenAI GPT-3
def translate_text(input_text, target_language):
   response1=client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[{
        "role":"system","content":"You are a translator"},{
        "role":"user","content":f'Translate the following English text to {target_language}:"{input_text}"'
      }])
   translated_text = response1.choices[0].message.content
   print(translated_text)
   return translated_text


# Streamlit UI
def main():
    st.title("Multilingual Storytelling with Accents")

    # Text input
    input_text = st.text_area("Enter text for translation:", "")

    # Language selection
    target_language = st.selectbox("Select target language:", ["English", "Spanish", "French"])
    translated_text = None
    language_code = "en"
    # Translate button
    if st.button("Translate"):
        translated_text = translate_text(input_text, target_language)
        st.write(f"Translated text ({target_language}): {translated_text}")   
    
    if st.button("Convert to Speech"):
            # Default to English  
     if target_language == "Spanish":
         language_code = "es"
     elif target_language == "French":
        language_code = "fr"    
     translated_text = translate_text(input_text, target_language) 
     sound_file = BytesIO()
     tts = gTTS(translated_text, lang=language_code)
     tts.write_to_fp(sound_file)
     st.audio(sound_file) 
     st.download_button(label="Download Audio", data=sound_file.getvalue(), file_name="translated_audio.mp3", mime="audio/mp3")      

       
if __name__ == "__main__":
    main()