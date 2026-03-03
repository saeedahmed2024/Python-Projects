import pyttsx3

def roboSpeaker():
    print("Welcome to RoboSpeaker 1.1. Created by Saeed")
    engine = pyttsx3.init()
    while True:
        x = input("Enter what you want me to speak: ")
        if x == 'q':
            engine.say("Thank you for using RoboSpeaker")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()


roboSpeaker()