#Created by John07-noob
#Sep/30/2020

import googletrans 
from googletrans import Translator
from os import system
#print(googletrans.LANGUAGES)

def clear_screen():
    clear = system('clear')

trans = Translator()
while True:
    trans_from = input("Translate From: ")
    trans_to = input("Translate To: ")

    user = input("Put Text Here: ")
    done_trans = trans.translate(f'{user}', src=f'{trans_from}', dest=f'{trans_to}')
    print(f"Translated: {done_trans.text}")

    again_exit = input("Press any key to Continue q(quit)... ")
    if again_exit == "q":
        exit()
    clear_screen()
