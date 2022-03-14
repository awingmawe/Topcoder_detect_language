# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 11:16:56 2022

@author: Moch. Rafi
         Kevin Sunjaya
         Arya Jonathan
"""

import re
import detectlanguage
detectlanguage.configuration.api_key = "4fa0b3ddd87eb443923b738b8bb87f30"

# Input
text = input("Type in or paste text here: ")

# Exclusion for Hindi
#ex = detectlanguage.simple_detect(text)
#if ex == "hi":
    #hres = ex.replace("hi", "hin")
   # print(text + "_" + hres)
#else:
    
#Regex
text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t'])|(\w+:\/\/\S+)|^rt|http.+?", "", text)

#Tokenization
text = text.split()

# API
for x in text:
    response = detectlanguage.simple_detect(x)
    if response == "es":
        result = response.replace("es", "spa")
    elif response == "en":
        result = response.replace("en", "eng")
    elif response == "hi":
        result = response.replace("hi", "hin")
    else:
        result = response
    # Output
    print(x + "_"  + result)


