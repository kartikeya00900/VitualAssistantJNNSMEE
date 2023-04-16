import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Define a function for speech recognition
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand you.")
    except sr.RequestError:
        print("Sorry, I am having trouble with speech recognition.")
    return None

# Main loop for listening to user input
while True:
    # Call the speech recognition function
    text = recognize_speech()
    if text is not None:
        print("You said: ", text)
        # Add your virtual assistant logic here
        # Example: if text == "hello": print("Hello, how can I help you?")
