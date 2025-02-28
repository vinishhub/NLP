from playsound import playsound
from gtts import gTTS
mytext="Welcome to NLP PRACTICALS"
language="en"
myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save("myfile.mp3")
playsound("myfile.mp3")

#pip install --user --Upgrade pip
#pip install --user -U nltk

