import tkinter as tk
import win32gui
from PIL import ImageGrab, Image
import numpy as np
#import tensorflow as tf
#from tensorflow.keras.models import load_model

#model = load_model('model.h5')

root = tk.Tk()
canvas = tk.Canvas(root, height=500, width=800, bg="#921ef7")
canvas.pack()

label1 = tk.Label(root, text="Draw a number", font=("Helvetica", 28))
label1.place(relx=0.02, rely=0.04, relwidth=0.5, relheight=0.9)

label2 = tk.Label(root, text="Thinking..", font=("Helvetica", 28))
label2.place(relx=0.54, rely=0.44, relwidth=0.43, relheight=0.5)

but_clr = tk.Button(root, text="Clear", font=("Helvetica", 18))
but_clr.place(relx=0.54, rely=0.08, relwidth=0.17, relheight=0.07)

but_rec = tk.Button(root, text="Recognise", font=("Helvetica", 18))
but_rec.place(relx=0.54, rely=0.17, relwidth=0.17, relheight=0.07)


root.mainloop()