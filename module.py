#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Neutral Bot Modules - various actions and responses to moods

Cohn-Kanade (CK+) dataset from (http://www.consortium.ri.cmu.edu/ckagree) 
"""
import random
import webbrowser

from PIL import Image
from pathlib import Path

__author__ = 'Duy N'

default_path = "response/"

# Use random seed to open an image 
def antiSURPRISE():
    local_path = "antiSup/"  
    data_path = Path(default_path + local_path)
    arr = ["0.jpg", "1.jpg", "2.jpg", "3.png", "4.jpg"]
    seed = random.randint(0, len(arr))
    if seed <= len(arr)-1:
        img = Image.open(data_path / arr[seed])     
        img.show()   
    else:
        url = 'https://www.youtube.com/watch?v=kXghgXg4Wss'
        webbrowser.open(url)   
    
def antiSAD():
    local_path = "antiSad/"
    data_path = Path(default_path + local_path)
    arr = ["0.jpg", "1.jpg", "2.jpg", "3.jpg", "4.jpeg", "5.jpeg", "6.jpg", "7.jpeg", "8.jpeg", "9.jpeg"]
    seed = random.randint(0, len(arr)-1)
    img = Image.open(data_path / arr[seed])     
    img.show()
    
def antiHAPPY():
    local_path = "antiHap/"
    data_path = Path(default_path + local_path)
    arr = ["0.jpeg", "1.jpg"]
    seed = random.randint(0, len(arr))
    if seed <= len(arr)-1:
        img = Image.open(data_path / arr[seed])     
        img.show()   
    else:
        url = 'https://youtu.be/XLK5OWU2YGw?t=10'
        webbrowser.open(url)
        
def antiFEAR():
    local_path = "antiFer/"
    data_path = Path(default_path + local_path)
    arr = ["0.jpg", "1.jpg"]
    seed = random.randint(0, len(arr))
    if seed <= len(arr)-1:
        img = Image.open(data_path / arr[seed])     
        img.show()   
    else:
        url = 'https://www.youtube.com/watch?v=-iBrGQZcR9U'
        webbrowser.open(url) 
        
def antiDISGUST():
    seed = random.randint(0, 1)
    if seed:
        url = 'https://www.youtube.com/watch?v=0wJIgGV1xss&list=PLjaFHgRkfurqcZMawP5fR6zbC1MYCnhKF'
    else:
        url = 'https://youtu.be/6YOSzUSEmoQ?t=8'
    webbrowser.open(url)    
    
def antiCONTEMPT():
    local_path = "antiCon/"
    data_path = Path(default_path + local_path)
    arr = ["0.jpg", "1.jpeg", "2.jpeg", "3.jpeg"]
    seed = random.randint(0, len(arr)-1)
    img = Image.open(data_path / arr[seed])     
    img.show()   

def antiANGER():
    local_path = "antiAng/"    
    data_path = Path(default_path + local_path)
    arr = ["0.jpg"]   
    seed = random.randint(0, len(arr)+1) 
    if seed <= len(arr)-1:
        img = Image.open(data_path / arr[seed])     
        img.show()  
    elif seed == len(arr)-1:
        url = 'https://youtu.be/L7BQRGXFLJs?t=56'
        webbrowser.open(url)
    elif seed == len(arr):
        url = 'http://www.letmegooglethat.com/?q=anger+management+near+me'
        webbrowser.open(url) 
    else:
        url = 'https://www.youtube.com/watch?v=LYN6DRDQcjI'
        webbrowser.open(url)
    