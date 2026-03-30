import pyttsx3
def TextToSpeech(text):
	engine = pyttsx3.init()

	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate+1) #скорость
	volume = engine.getProperty('volume')
	engine.setProperty('volume', volume + 0.1) #громкость

	engine.say(text)
	engine.runAndWait()

TextToSpeech(input("Введите текст для озвучки: "))
