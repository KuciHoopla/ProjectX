from tkinter import Canvas

from tkinter import *
from PIL import ImageTk

from RPA.creators.variables.variables import printscreen

canvas = Canvas(width = 200, height = 200, bg = 'blue')
canvas.pack(expand = YES, fill = BOTH)

image = ImageTk.PhotoImage(file = printscreen)
canvas.create_image(10, 10, image = image, anchor = NW)

mainloop()