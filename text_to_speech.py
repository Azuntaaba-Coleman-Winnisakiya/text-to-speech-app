import pyttsx3 as p3
import PySimpleGUI as sg

layout = [
    [sg.Text('Please enter text to:')],
    [sg.Input()],
    [sg.Radio('Female voice', 'VOICE', key='female',default=True), sg.Radio('Male voice', 'VOICE', key='male')],
    [sg.Button('Speak')]
]

window = sg.Window('SENG APP_2',layout)

engine = p3.init()

def speak(text, voice):
    if voice == 'male':
        engine.setProperty('voice', 'english+m7')
        engine.setProperty('rate', 100)  
        engine.setProperty('volume', 1.0)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id) 
        engine.say(text)
        engine.runAndWait()
    elif voice == 'female':
        engine.setProperty('voice', 'english+f4')
        engine.setProperty('rate', 100)  
        engine.setProperty('volume', 1.0)
        engine.say(text)
        engine.runAndWait()

    

    

while True:
    event,value = window.read()
    if event == sg.WIN_CLOSED:
     break
    if event == 'Speak':
       text = value[0]
       print(text)
       if value['female'] == True:
          voices = engine.getProperty('voices')
          engine.setProperty('voice', voices[1].id)
          engine.say(text)
          engine.runAndWait()
       elif value['male'] == True:
          voices = engine.getProperty('voices')
          engine.setProperty('voice', voices[0].id)
          engine.say(text)
          engine.runAndWait()
       

    """ if value[0]:
        if value['female']:
            voice = 'female'
        else:
            voice = 'male'
        speak(text, voice) """
    #       voice='male'
    # else :
    #       voice='female'
    #       speak(text, voice)
    # elif event == 'female':
    #    voice = 'female'
    # elif event == 'male':
    #     voice = 'male'
       
 

window.close()
engine.stop()