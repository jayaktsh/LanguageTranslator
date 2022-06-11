import googletrans


# Importing necessary modules required
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

# Creating Recogniser() class object
recog1 = spr.Recognizer()

# Creating microphone instance
mc = spr.Microphone()

# language to translate from
print("choose the language to translate from: 1. English\n 2. Hindi\n 3. Korean\n 4. French\n 5. Italian\n ")
lang1 = int(input("enter number of choice: "))
if (lang1 == 1):
    from_lang = 'en'
elif (lang1 == 2):
    from_lang = 'hi'
elif (lang1 == 3):
    from_lang = 'ko'
elif (lang1 == 4):
    from_lang = 'fr'
elif (lang1 == 5):
    from_lang = 'it'
else:
    print("enter valid input")

# language to translate to
print("choose the language to translate to: 1. English\n 2. Hindi\n 3. Korean\n 4. French\n 5. Italian\n ")
lang2 = int(input("enter number of choice: "))
if (lang2 == 1):
    to_lang = 'en'
elif (lang2 == 2):
    to_lang = 'hi'
elif (lang2 == 3):
    to_lang = 'ko'
elif (lang2 == 4):
    to_lang = 'fr'
elif (lang2 == 5):
    to_lang = 'it'
else:
    print("enter valid input")

print(from_lang)
print(to_lang)

# Capture Voice
with mc as source:
    print("Speak 'hello' to initiate the Translation !")
    print("Give it a second")
    recog1.adjust_for_ambient_noise(source, duration=0.2)
    audio = recog1.listen(source)
    MyText = recog1.recognize_google(audio)
    MyText = MyText.lower()

# Initializing with hello
if 'hello' in MyText:

    # Translator method for translation
    translator = Translator()


    with mc as source:

        print("Speak a stentence...")
        recog1.adjust_for_ambient_noise(source, duration=0.2)

        # Storing the speech into audio variable
        audio = recog1.listen(source)

        # Using recognize.google() method to convert audio into text
        get_sentence = recog1.recognize_google(audio)

        # Using try and except block to improve its efficiency.
        try:

            # Printing Speech which need to be translated.
            print("Phrase to be Translated :" + get_sentence)

            # translating
            text_to_translate = translator.translate(get_sentence,
                                                     src=from_lang,
                                                     dest=to_lang)

            # Storing the translated text in text variable
            text = text_to_translate.text

            # Using Google-Text-to-Speech 
            speak = gTTS(text=text, lang=to_lang, slow=False)

            # Using save() method to save the translated
            # speech in capture_voice.mp3
            speak.save("captured_voice.mp3")

            # Using OS module to run the translated voice.
            os.system("start captured_voice.mp3")

        # Here we are using except block for UnknownValue
        # and Request Error and printing the same to
        # provide better service to the user.
        except spr.UnknownValueError:
            print("Unable to Understand the Input")

        except spr.RequestError as e:
            print("Unable to provide Required Output".format(e))
