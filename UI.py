import tkinter as tk
from tkinter import *
from PIL import ImageDraw, Image
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import load_model

model = load_model('model.h5')

def predict_digit(img):
    #resize image to 28x28 pixels
    img = img.resize((28,28))
    #convert rgb to grayscale
    img = img.convert('L')
    img = np.array(img)
    #reshaping to support our model input and normalizing
    img = img.reshape(1,28,28,1)
    img = img/255.0
    #predicting the class
    res = model.predict([img])[0]
    return np.argmax(res), max(res)

root = tk.Tk()
root.title("Handwritten Digit Recognition")
canvas = tk.Canvas(root, height=500, width=400, bg="#ffffff")
canvas.pack(side='left')

control = tk.Canvas(root, height=500, width=400, bg="#921ef7")
control.pack(side='left')

def paint(event):
    x = event.x
    y = event.y
    r=7
    canvas.create_oval(x-r, y-r, x + r, y + r, fill='black')

image1 = Image.new('RGB', (400, 500), 'white')
draw = ImageDraw.Draw(image1)
canvas.bind('<B1-Motion>', paint)
#canvas.pack(expand=YES, fill=BOTH)

def get_image():
    digit, acc = predict_digit(image1)
    label.configure(text= str(digit)+', '+ str(int(acc*100))+'%')

def clear_all():
    canvas.delete("all")
    label.configure(text = "")

label = tk.Label(control, text="", font=("Helvetica", 48))
label.place(relx = 0.1, rely = 0.3, relwidth = 0.8, relheight = 0.5)

classify_btn = tk.Button(control, text = "Recognise", command = lambda: get_image())
classify_btn.place(relx = 0.04, rely = 0.1, relwidth = 0.2, relheight = 0.1)

clear_btn = tk.Button(control, text= "Clear", command = lambda: clear_all())
clear_btn.place(relx = 0.34, rely = 0.1, relwidth = 0.2, relheight = 0.1)

root.mainloop()