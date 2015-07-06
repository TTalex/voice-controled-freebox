import speech_recognition as sr
import requests

//Language set to French
r = sr.Recognizer("fr-FR")
r.energy_threshold = 300
while 1:
    with sr.Microphone() as source:
        print("Listening")
        audio = r.listen(source)
        
        try:
            print("Recognizing")
            s = r.recognize(audio)
            print("You said " + s)
            if (s=="Freebox" or s=="freebox"):
                print("POWER")
                requests.get('http://hd1.freebox.fr/pub/remote_control?code=34679945&key=power')
            if (s=="ok"):
                print("OK")
                requests.get('http://hd1.freebox.fr/pub/remote_control?code=34679945&key=ok')
            if (s=="menu" or s=="Menu"):
                print("MENU")
                requests.get('http://hd1.freebox.fr/pub/remote_control?code=34679945&key=home')
            if (s == "un"):
                requests.get('http://hd1.freebox.fr/pub/remote_control?code=34679945&key=1')
            numbers = ["1","2","3","4","5","6","7","8","9"]
            if s in numbers:
                print(s)
                requests.get('http://hd1.freebox.fr/pub/remote_control?code=34679945&key='+s) 
            
        except LookupError:
            print("Couldn't decipher voice")
