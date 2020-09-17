import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile("file/Gombel.wav") as source:              # use "gombal.wav" as the audio source
    audio = r.record(source)                        # extract audio data from the file

try:
    print("Transkripsi: " + r.recognize_google(audio, language="id-ID"))   # recognize speech using Google Speech Recognition
except LookupError:                                 # speech is unintelligible
    print("Saya tidak mengerti")