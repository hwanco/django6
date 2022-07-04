from gtts import gTTS

def speak(st):
    tts = gTTS(text=st, lang="en")
    filename = "test.mp3"
    tts.save(filename)