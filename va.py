import speech_recognition as sr
import tkinter as tk

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        recognized_text = recognizer.recognize_google(audio)
        print("Recognized text:", recognized_text)
        # Perform actions based on recognized text
        # e.g. call a function to handle the recognized command
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error: {0}".format(e))

def on_button_click():
    recognize_speech()

root = tk.Tk()
root.title("Virtual Assistant")

button = tk.Button(root, text="Click to Speak", command=on_button_click)
button.pack()

root.mainloop()
