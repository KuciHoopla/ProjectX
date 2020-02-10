from PIL import Image, ImageTk
import tkinter as tk

from RPA.creators.variables.variables import printscreen


class BkgrFrame(tk.Frame):
    def __init__(self, parent, file_path, width, height):
        super(BkgrFrame, self).__init__(parent, borderwidth=0, highlightthickness=0)

        self.canvas = tk.Canvas(self, width=width, height=height)
        self.canvas.pack()

        try:
            pil_img = Image.open(file_path)
            self.img = ImageTk.PhotoImage(pil_img.resize((width, height), Image.ANTIALIAS))
            self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        except:
            print("no printscreen")


    def add(self, widget, x, y):
        canvas_window = self.canvas.create_window(x, y, anchor=tk.NW, window=widget)
        return widget


if __name__ == '__main__':


    tk.mainloop()