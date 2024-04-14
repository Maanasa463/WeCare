from gtts import gTTS 
import os 

mytext = 'please take advil now'

myobj = gTTS(text=mytext, lang='en', slow=False) 

myobj.save("welcome.mp3") 

os.system("mpg321 welcome.mp3") 
