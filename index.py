

import os, requests
import json
import apiai
import local_settings
from time import gmtime, strftime
import speech_recognition as sr

CLIENT_ACCESS_TOKEN=local_settings.CLIENT_ACCESS_TOKEN

def ascolta_microfono():
    r = sr.Recognizer()
    with  sr.Microphone() as source :
        audio = r.listen(source)
        testo=r.recognize_google(audio,language='it')
        print(testo)
        return testo

def ascolta_tastiera():
    ascolto=input('Enter your input:')
    return ascolto
#dialogflow
def elabora(richiesta):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'id'  # optional, default value equal 'en'

    request.session_id = "1"

    request.query = richiesta

    #response = request.getresponse()

    response = json.loads(request.getresponse().read().decode('utf-8'))
    action= response['result']['action']
   
    print(action)
    if (action == 'direora'):
        message = ' sono le ore '+ strftime("%H:%M ", gmtime())
    else :
        message = response['result']['fulfillment']['speech']
    return (message)


def parla(testo):
    os.system("say "+testo )

ascolto=''
while (ascolto != 'Addio'):
    ascolto=ascolta_microfono()
    if (ascolto!='Addio') :
        risponde=elabora(ascolto)
    else :
        risponde='alla prossima'    
    parla(risponde)