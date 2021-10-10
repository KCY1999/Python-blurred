import os.path
import cv2
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import ImageTk, Image
'''
img = cv2.imread("a1.png")

cv2.imshow("show", img)
cv2.waitKey(0)
cv2.imwrite("a1.png", img)

graImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("show2", graImg)
cv2.waitKey(0)

_, binImg = cv2.threshold(graImg, 0, 255, cv2.THRESH_BINARY)
cv2.imshow("show3", binImg)
cv2.waitKey(0)

cv2.destroyWindow('show')
'''
##########################################################################################################
'''
window = tk.Tk()
window.title("CLASS")
window.geometry('600x480')

class aaa():
    def __init__(self):

        nb = ttk.Notebook(window)

        p1 = tk.Frame(nb, bg='gray')

        nb.add(p1, text="page1")
        nb.pack(fill="both", expand="yes")

        self.xf = tk.Frame(p1)
        self.xf.pack(side=tk.TOP)
        self.x_l = tk.Label(self.xf)
        self.x_l.pack(side=tk.LEFT)

        self.calculate = tk.Button(p1, text='go', command=self.labelshow, fg='Red')
        self.calculate.pack()

    def labelshow (self):
        try:
            img = cv2.imread("a1.png")
            resImg = cv2.resize(img, (650, 400), interpolation=cv2.INTER_CUBIC)#後面調整大小
            oimg = cv2.cvtColor(resImg, cv2.COLOR_BGR2GRAY)  ##cv2.COLOR_BGR2GRAY
            im = Image.fromarray(oimg)
            image2 = ImageTk.PhotoImage(image=im)
        
            if self.x_l is None:
                self.x_l.image = image2
                self.x_l.pack()
            else:
                self.x_l.configure(image=image2)
                self.x_l.image = image2
        except:
            print("error")

main=aaa()
window.mainloop()
'''
#=============================Median Filter====================================
import numpy as np
import cv2

image = cv2.imread('baboon.Bmp')

blured=cv2.medianBlur(image, 5)

mean = cv2.blur(image, (5, 5))

blurred = np.hstack([image, blured, mean])

cv2.imshow('Original+Median+Mean',blurred)

cv2.waitKey(0)