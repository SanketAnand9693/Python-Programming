import speech_recognition as sr
import pyttsx3
#from googlesearch import search

r = sr.Recognizer()


def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


while True:
    with sr.Microphone() as source:
        print("you can speak now")
        r.adjust_for_ambient_noise(source)
        audio_data = r.listen(source)
    text = r.recognize_google(audio_data)

    if ("hello" in text):
        print("Hello, how are you?")

    elif ("who created you" in text):
        print("I was created by Sanket Anand on 10th of October 2021.")
    elif ("contact creator" in text):
        print("The name is Sanket Anand. you can contact on sanketanand0202@gmail.com")
    # elif ("search" in text)
    #     search("Google", lang="fr")
    elif ("bye" in text):
        print("Good bye! Have a nice day.")
        break
    else:
        print("Sorry i dont know about that i am still learning")
