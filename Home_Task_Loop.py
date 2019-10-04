

import requests
import re
import xml


while False:
    print("Type 'quit' to exit")
    phrase = input("Your message:")
    if phrase == 'quit':
        break
    elif phrase == 'Hello':
        print("How it is going?")
    elif phrase == "What is your name":
        print("I don't want to have name")
    else:
        print("I don't understand you")


