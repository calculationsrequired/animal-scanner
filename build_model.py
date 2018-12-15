#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CNN for the Expression Network

Starting structure from Krishna's CNN model (https://github.com/mahakal/FacialEmotionRecognition)
Cohn-Kanade (CK+) dataset from (http://www.consortium.ri.cmu.edu/ckagree) 
"""
import pickle
import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D, AveragePooling2D, BatchNormalization
from keras.layers.advanced_activations import PReLU
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils, plot_model
from keras.preprocessing.image import ImageDataGenerator

__author__ = 'Duy N'

# Configuration, run epoch = 1 to fine tune, takes a while though
data_path = "ckplus3.pickle"
save = 0
epoch = 20
runs = 200
batch_size = 32
class_num = 8
filter_num = 96
pool_size = (2, 2)
kernel_size = (3, 3)

# Data structures and parameters set
with open(data_path, 'rb') as dataset:
    data_obj = pickle.load(dataset)
(training_data, validation_data, test_data) = data_obj['training_data'], data_obj['validation_data'], data_obj['test_data']
(X_train, y_train), (X_test, y_test) = (training_data[0],training_data[1]), (test_data[0],test_data[1])
img_rows, img_cols = data_obj['img_dim']['width'], data_obj['img_dim']['height'] 
# Reshaping to image dimensions 
X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
input_shape = (img_rows, img_cols, 1) 
Y_train = np_utils.to_categorical(y_train, class_num)
Y_test = np_utils.to_categorical(y_test, class_num)

# Data augmentation
datagen = ImageDataGenerator(rotation_range=20,
                             horizontal_flip=True)
datagen.fit(X_train)

# Feed Forward
model = Sequential()
def build_model(class_num, filter_num, pool_size, kernel_size):
    """ Home-Grown Architecture for the CNN model. Sequential model. """
    # Conv Layer 1    
    model.add(Convolution2D(filter_num, (kernel_size[0], kernel_size[1]), strides=1, padding='valid', input_shape=input_shape)) 
    model.add(PReLU()) 
    model.add(MaxPooling2D(pool_size=pool_size, strides=2))   
    model.add(BatchNormalization())
    #Conv Layer 2
    model.add(Convolution2D(filter_num*2, (kernel_size[0], kernel_size[1]), strides=1, padding='valid'))     
    model.add(PReLU())        
    model.add(MaxPooling2D(pool_size=pool_size, strides=2))
    model.add(BatchNormalization())
    #Conv Layer 3    
    model.add(Convolution2D(filter_num*4, (kernel_size[0], kernel_size[1]), strides=1, padding='valid'))     
    model.add(PReLU())        
    model.add(MaxPooling2D(pool_size=pool_size, strides=2))
    model.add(BatchNormalization())    
    # Full Connected Layer
    model.add(Flatten())
    model.add(Dense(512, activation='relu')) 
    model.add(Dropout(0.5))
    model.add(Dense(256, activation='relu')) 
    model.add(Dropout(0.5))   
    model.add(Dense(128, activation='relu')) 
    model.add(Dropout(0.5))     
    model.add(Dense(class_num, activation='softmax'))
    
def main():
    top_score = 0.74
    # Run Model
    build_model(class_num, filter_num, pool_size, kernel_size)
    # Saving after every run
    for i in range(runs):
        print("Run:", i)
        try:
            model.load_weights('my_model_best.hdf5')
            print("Loading Checkpoint...")            
        except:
            print("No Checkpoint Detected") 
        if i == 0:
            plot_model(model, to_file='model.png', show_shapes=True)
        model.compile(loss='categorical_crossentropy',
                      optimizer='adadelta',
                      metrics=['accuracy'])          
        model.fit_generator(datagen.flow(X_train, Y_train, batch_size), steps_per_epoch=len(X_train)/32, epochs=epoch,
                  verbose=1, validation_data=(X_test, Y_test))
        score = model.evaluate(X_test, Y_test, verbose=0)
        # To fine tune the accuracy and save model
        if save:
            model.save('ckp_model.h5')
        if epoch == 1:
            if score[1] > top_score:
                print("Saving higher score:", score[1], ">", top_score)
                model.save_weights('my_model_best.hdf5')
                top_score = score[1]
        else:
            print("Saving model at:", score[1])
            model.save_weights('my_model_best.hdf5')
    
if __name__ == '__main__':
    main()