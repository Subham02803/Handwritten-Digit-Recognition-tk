import tkinter as tk
import win32gui
from PIL import ImageGrab, Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

model = load_model('model.h5')


root = tk.Tk()
canvas = tk.Canvas(root, height=500, width=800, bg="#e6e6ff")
canvas.pack()

root.mainloop()