import time
import winsound

freq = 1000

short_duration = 500
long_duration = 1000

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',' ':'/'}

def code(message):
    for word in message:
        if word=='-':
            winsound.Beep(frequency=freq , duration=short_duration)
            time.sleep(0.3)
        elif word == '.':
            winsound.Beep(frequency=freq , duration=long_duration)
            time.sleep(0.3)
        elif word == ' ' or word == '/':
            time.sleep(1)

string = input("Enter the message - ").upper()
message = ' '.join(MORSE_CODE_DICT[key] for key in string)

code(message)