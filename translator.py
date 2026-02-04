from deep_translator import GoogleTranslator
from time import sleep

# The main program's structure
# This program auto detect the language's input, being unnecessary talk what language is the input
while True: 
    text = input('Type the text you want to translate: ')
    if text == '':
        print('The text must have some characters!')
        continue

    output = input('Whats the target language? (e.g, es, nl, en, and more than 100 languages): ')


    try:
        motor = GoogleTranslator(source='auto', target=output)
        result = motor.translate(text)
        print(f'Original text: {text}')
        print('Wait...')
        sleep(1)
        print(f'Translated text: {result}')

    except Exception:
        print('Error. Try again later.')
        continue

    choice = input('Do you want translate other text? (y/n): ')
    if choice != 'y':
        print('Thanks for using the translator! Drink water.')
        sleep(3)
        break