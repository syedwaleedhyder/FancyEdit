from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import filedialog
import tkinter as tk
from PIL import ImageTk, Image
import os
import cv2

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.button = tk.Button(self, text="Load Image", command=self.openImage)
        self.recolor = tk.Button(self, text="ReColor Image", command=self.editImage)
        self.edgeDetect = tk.Button(self, text="Edge Detection", command=self.editImage)
        self.spatialFiltering = tk.Button(self, text="Spatial Filtering", command=self.editImage)
        self.title_text = tk.StringVar()
        self.display_text = tk.StringVar()
        self.editOptions = tk.Label(self, textvariable=self.display_text)
        self.title_name = tk.Label(self, textvariable=self.title_text)
        self.title_name.config(font=("Courier", 44))
        self.editOptions.config(font=("Courier", 24))
        self.title_text.set("FancyEdit")
        self.display_text.set("Edit Options")
        self.frame = tk.Frame(self)
        self.frame.place(x=10, y=100)
        self.recolor.place(x=650, y=120)
        self.edgeDetect.place(x=650, y=170)
        self.spatialFiltering.place(x=650, y=220)
        self.editOptions.place(x=610, y=80)
        self.title_name.place(x=400, y=10)
        self.create_canvas()
        self.button.place(x=250, y=600)

    def editImage(self):
        '''
            This is the code for editing the image as per user requirements. 
        '''
        pass

    def openImage(self):
        self.filePath = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              filetypes=(("JPEG", ".jpg"), ("PNG", ".png"),
                                                         ("All Files", "*.*")),
                                              title="Open Image")
        img = cv2.imread(self.filePath)
        self.ax1.imshow(img)
        self.canvas.draw()

    def create_canvas(self):
        ''' Add a canvas to plot images '''
        self.fig1 = Figure(frameon=False, figsize=(6, 4.5))
        self.canvas = FigureCanvasTkAgg(self.fig1, master=self.frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
        self.canvas.set_window_title("AutoEdit")
        self.ax1 = self.fig1.add_axes([0, 0, 1, 1])
        self.ax1.axis('off')

# Run program
app = GUI()
app.config()
app.title("FancyEdit")
app.geometry("900x650")
app.mainloop()