import speech_recognition as sr

listner=sr.recognizer()
try:
    with sr.Microphone() as source:
        print('listening')
        voice=listner.listen(source)
        command=listner.recognize_google(voice)
        print(command)
expect:

