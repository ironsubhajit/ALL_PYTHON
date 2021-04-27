from gtts import gTTS
import os

text = input("Enter any thing to convert to speech: ")
language = 'en'
converted_audio = gTTS(text=text, lang=language, slow=False)
converted_audio.save("S:\\Download\\audio.mp3")
os.system("S:\\Download\\audio.mp3")
