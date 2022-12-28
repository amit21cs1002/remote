import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes  
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening..")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song) 
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("current time is " + time)
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "are you single" in command:
        talk("sorry, im in relationship with internet")
    elif "joke" in command:
        talk(pyjokes.get_joke())
    elif "how are you" in command:
        talk("I'm fine")
        print("I'm fine")
    elif "bye" in command:
        exit()        
    elif "who made you" in command:
        print("I was made by a guy named Amit Singh")
        talk("I was made by a guy named Amit Singh")
    elif "why" in command:
        print("i dont know, maybe he was bored")
        talk("i dont know, maybe he was bored")
   
    elif "how is he" in command:
        print("shut up, Amit is the best")
        talk("shut up, Amit is the best")
    else:
        talk("Sorry, please say it again")
        
while True:
    run_alexa()
run_alexa()

