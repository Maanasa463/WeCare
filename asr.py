import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Open the audio file
with sr.AudioFile('1.wav') as source:
    # listen for the data (load audio to memory)
    audio = r.record(source)

# Recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="YOUR_API_KEY")`
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))