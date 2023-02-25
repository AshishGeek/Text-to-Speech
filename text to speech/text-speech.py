from gtts import gTTS
from playsound import playsound

text = input("Enter the text to convert to speech: ")
tts = gTTS(text)
tts.save('output.mp3')
playsound('output.mp3')
