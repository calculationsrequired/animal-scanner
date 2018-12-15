#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Neutral Bot - framework to recognize a facial emotion and bringing back to neutral

Cohn-Kanade (CK+) dataset from (http://www.consortium.ri.cmu.edu/ckagree) 
"""
import cv2
import numpy as np
import random

import module

from time import sleep
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image

__author__ = 'Duy N'

# Make this whatever image you like
sample1, sample2, sample3 = 'anger.jpg', 'chill doctor.jpeg', 'sad.jpg'
#img_name = 'input.jpg'
img_name = sample3

# The model we trained
model = load_model('ckp_model.h5')
model.compile(loss='categorical_crossentropy',
              optimizer='adadelta',
              metrics=['accuracy'])
# Details where the face is located
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Trained the model on 48x48. Can increase with different model
img_width, img_height = 48, 48

# Crop to only the face, modified code of Krishna's
def face(img_path):
    img = cv2.imread(img_path, 0)
    resize = tuple([img_width,img_height])
    scale_factor = 1.05
    faces = face_cascade.detectMultiScale(img, scale_factor, 5)
    while not len(faces):
        scale_factor -= .05
        faces = face_cascade.detectMultiScale(img, scale_factor, 5)
        if scale_factor <= 1:
            print(img_path)
            return
    for (x,y,w,h) in faces:
        return cv2.resize(img[y:y+h, x:x+w], resize, interpolation = cv2.INTER_AREA)
    
# Image preprocessing
def processImage(img_path):
    try:
        input_img = face(img_path)
    except:
        input_img = image.load_img(img_path, target_size=(img_width, img_height))
        print("Can't crop face, results may be more questionable")
    input_img = image.img_to_array(input_img)
    input_img = input_img.reshape(img_width, img_height, 1)
    input_img = np.expand_dims(input_img, axis=0)
    return input_img

# Runs different emotion modules depending on given emotion
def getResponse(mood):
    if mood == 0:
        print("To combat NEUTRAL...")
        print("And/or miscalculations...")
        print("This bot will now combat a random emotion...")
        mood = random.randint(1, 7)
    if mood == 1:
        print("To combat ANGER...") 
        print("...")
        sleep(5)
        module.antiANGER()
    if mood == 2:
        print("To increase CONTEMPT...") 
        print("...")   
        sleep(5)        
    if mood == 3:
        print("To combat DISGUST...")    
        print("...")       
        sleep(5)        
    if mood == 4:
        print("To combat FEAR...")
        print("...")        
        sleep(5)        
        module.antiFEAR()        
    if mood == 5:
        print("To combat HAPPY...")
        print("...")       
        sleep(5)        
        module.antiHAPPY()        
    if mood == 6:
        print("To combat SAD...")   
        print("...")     
        sleep(5)        
        module.antiSAD()
    if mood == 7:
        print("To combat SURPRISE...")
        print("...")    
        sleep(5)        
        module.antiSURPRISE() 
        
# Returns an emotion based on what the model returns
def getEmotion(emotion_array):
    moods = ['NEUTRAL', 'ANGER', 'CONTEMPT', 'DISGUST', 'FEAR', 'HAPPY', 'SAD', 'SURPRISE']
    for idx in range(8):
        if emotion_array[0][idx]:
            print("Emotion Displayed...", moods[idx])
            return idx

def main():
    image = processImage(img_name)
    result = model.predict(image, batch_size=1)
    emo = getEmotion(result)   
    getResponse(emo)

if __name__ == '__main__':
    main()