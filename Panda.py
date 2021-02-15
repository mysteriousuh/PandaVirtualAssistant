import pyttsx3 as p
import speech_recognition as sr
from Newsapi import news
from YoutubeSel import music
from weather import de, temp
import datetime

engine = p.init()

rate = engine.getProperty('rate')

engine.setProperty('rate', 170)   #for changing the rate of speed of speaking

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  #it Will change voices By default
print(voices)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishes():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return ("Morning")
    if hour>=12 and hour<16:
        return("afternoon")
    if hour>= 16 and hour<24:
        return("evening")

today_date = datetime.datetime.now()
r = sr.Recognizer()   #helps uss to get voice from microphone

speak("Hello Master Sidhant, good " +wishes())
speak("Today is" + today_date.strftime("%d") + "of" + today_date.strftime("%B") + "and the time right now is" + today_date.strftime("%I") + today_date.strftime("%M") + today_date.strftime("%p"))

with sr.Microphone() as source:

    r.energy_threshold = 10000  #it will capture voice at low note also
    r.adjust_for_ambient_noise(source, 1.2)  #will cancel the noise around

    print("listening")
    audio = r.listen(source)   #captures the voice from the microphone and save in the variable I.E aud
    # now will send this audio to google api engine which will convert it to text
    text = r.recognize_google(audio)   #sends audio to google api and google api converts it into text
    print(text)

if "what" and "about" and "you" in text:
    speak("I am Fine")
speak("how can i help you")

with sr.Microphone() as source:

    r.energy_threshold = 10000  #it will capture voice at low note also
    r.adjust_for_ambient_noise(source, 1.2)  #will cancel the noise around

    print("listening")
    audio = r.listen(source)
    tex = r.recognize_google(audio)
if "information" in tex:
    speak("on which topic you need information?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000  # it will capture voice at low note also
        r.adjust_for_ambient_noise(source, 1.2)  # will cancel the noise around

        print("listening")
        audio = r.listen(source)
        info = r.recognize_google(audio)
    speak("searching{} in wikipedia".format(info))
    print("searching{} in youtube".format(info))

    from SElWeb import infow
    assist = infow()
    assist.get_info(info)

elif "play" and "video" in tex:
    speak("which video you wanna play")
    with sr.Microphone() as source:
        r.energy_threshold = 10000  # it will capture voice at low note also
        r.adjust_for_ambient_noise(source, 1.2)  # will cancel the noise around

        print("listening")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    print("searching{} in youtube".format(vid))
    speak("searching{} in youtube".format(vid))
    assist = music()
    assist.play(vid)

elif "news" in tex:
    news("Sure master, I will read news")
    speak("Sure master, I will read news")
    ass = news()
    for i in range(len(ass)):
        print(ass[i])
        speak(ass[i])

elif "weather" and "atmosphere" in tex:
    speak("Master, the weather is " + str(temp())+"degree celsius" + " with " + str(de()))








