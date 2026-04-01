import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return ""

# Main
speak("Hello Shavya, I am your Jarvis")

while True:
    command = listen()

    if "hello" in command:
        speak("Hello, how can I help you?")
        
    elif "time" in command:
        import datetime
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")
        
    elif "exit" in command:
        speak("Goodbye")
        break