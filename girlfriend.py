import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine. setProperty('voice', voices[1]. id)
engine. say('Hi! dheirya you are looking smart and i love you')
engine. runAndWait()