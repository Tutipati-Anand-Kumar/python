import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice_choice = input("choose voice - Male(1) or Female(2): ")
if voice_choice == "1":
    engine.setProperty('voice',voices[0].id)
elif voice_choice == "2":
    engine.setProperty('voice',voices[1].id)
else:
    print("invalid choice")
    engine.setProperty('voice',voices[1].id)
text = input("enter your text:")
engine.say(text)
engine.runAndWait()
rate = engine.getProperty("rate")
engine.setProperty('rate',rate-1)