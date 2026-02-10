from deep_translator import GoogleTranslator
from time import sleep

# The main program's structure
# This program auto detect the language's input, being unnecessary talk what language is the input
while True: 
    text = input('Type the text you want to translate (or tip exit or quit): ').strip()
    # I put these ifs, to prevent typing problems
    if not text:
        print('The text must be some characters!')
        continue
    if text.lower() in ['exit', 'quit']:
        print('Bye! Drink water.')
        break

    while True:
        output = input('Whats the target language? (e.g, es, nl, en, and more than 100 languages): ').lower().strip()
        if not output: 
            print('The output must be some characters.')
            continue
        else:
            break


    try:
        # The translating part of program
        motor = GoogleTranslator(source='auto', target=output)
        result = motor.translate(text)
        print(f'Original text: {text}')
        print('Wait...')
        print(f'Translated text: {result}')

    except Exception:
        print('Error. Try again later.')
        continue

# Here, I put the while True, so, the program dont get back for initial part without necessity
    while True:
        choice = input('Do you want translate other text? (y/n or tip quit or exit): ').lower().strip()
        if not choice:
            print('Please, tip y, or n, or quit, or exit.')
            continue
        if choice != 'y' or 'quit' or 'exit':
            print('Thanks for using the translator! Drink water.')
            sleep(3)
            break