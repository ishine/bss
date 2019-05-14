# coding: utf-8
# -*- coding: utf-8 -*-

"""General"""
import numpy as np
from tkinter import *
import tkinter.font as font
import os
import cv2

"""recording"""
import pyaudio

"""Separation Methods"""
from FDICA import FDICA
from IVA import IVA
from AuxIVA import AuxIVA
from ILRMA import ILRMA

"""Voice and Face recognition"""
from FacialRecog import FacialRecog

path = "./groups"


def dircount(path):
    dirlist = []
    for dir in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir)):
            dirlist.append(dir)
    return len(dirlist)


class Separater(Frame):

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.ngroup = dircount(path)
        # self.makeFolders()
        self.font_b = font.Font(self, family="", size=12, weight="bold")
        self.font_n = font.Font(self, family="", size=11)
        self.makeWidgets()

    def makeFolders(self):
        group = "group{}".format(self.ngroup)
        grouppath = os.path.join(path, group)
        os.mkdir(grouppath)
        for i in range(3):
            os.mkdir(os.path.join(grouppath, "speaker{}".format(i+1)))
        self.ngroup += 1

    def makeWidgets(self):
        l1 = Label(self, text="1. Recording", font=self.font_b)
        l1.grid(row=0, column=0, pady=5, padx=5, sticky=W)

        l1_1_1 = Label(self, text="record speaker 1's voice", bg='LightSkyBlue', relief=RIDGE, font=self.font_n)
        l1_1_1.grid(row=1, column=0, pady=3, padx=3, sticky=W)
        b1_1_1 = Button(self, text="rec start", bg='red', relief=RIDGE, font=self.font_n)
        b1_1_1.grid(row=1, column=1, pady=3, padx=3)

        l1_1_2 = Label(self, text="record speaker 2's voice", bg='LightSkyBlue', relief=RIDGE, font=self.font_n)
        l1_1_2.grid(row=2, column=0, pady=3, padx=3, sticky=W)
        b1_1_2 = Button(self, text="rec start", bg='red', relief=RIDGE, font=self.font_n)
        b1_1_2.grid(row=2, column=1, pady=3, padx=3)

        l1_1_3 = Label(self, text="record speaker 3's voice", bg='LightSkyBlue', relief=RIDGE, font=self.font_n)
        l1_1_3.grid(row=3, column=0, pady=3, padx=3, sticky=W)
        b1_1_3 = Button(self, text="rec start", bg='red', relief=RIDGE, font=self.font_n)
        b1_1_3.grid(row=3, column=1, pady=3, padx=3)

        l1_2 = Label(self, text="*** train MFCC on another PC ***", font=self.font_n)
        l1_2.grid(row=4, column=0, pady=5, padx=3, sticky=W)

        l1_3 = Label(self, text="*** set video angle ***", font=self.font_n)
        l1_3.grid(row=5, column=0, pady=5, padx=3, sticky=W)

        l1_4 = Label(self, text="record video and mix voice", bg='LightSkyBlue', relief=RIDGE, font=self.font_n)
        l1_4.grid(row=6, column=0, pady=3, padx=3, sticky=W)
        b1_4 = Button(self, text= "rec start", bg='red', relief=RIDGE, font=self.font_n)
        b1_4.grid(row=6, column=1, pady=3, padx=3)

        l2 = Label(self, text="2. Separation", font=self.font_b)
        l2.grid(row=7, column=0, pady=7, padx=7, sticky=W)

        l2_1 = Label(self, text="run ILRMA on this PC", bg='LightSkyBlue', relief=RIDGE, font=self.font_n)
        l2_1.grid(row=8, column=0, pady=3, padx=3, sticky=W)
        b2_1 = Button(self, text="run !!", bg='yellow', relief=RIDGE, font=self.font_n)
        b2_1.grid(row=8, column=1, pady=3, padx=3)

        l2_2 = Label(self, text="*** run FDICA & AuxIVA on another PC ***", font=self.font_n)
        l2_2.grid(row=9, column=0, pady=3, padx=3, sticky=W)

        self.result = Listbox(self, selectmode=EXTENDED, height=5)
        self.result.grid(row=10, column=0, pady=3, padx=3, sticky=W+E)

        l2_3_1 = Label(self, text="play results of FDICA", bg='LightSkyBlue', relief=RIDGE, font=self.font_n)
        l2_3_1.grid(row=11, column=0, pady=3, padx=3, sticky=W)
        b2_3_2 = Button(self, text="1", bg='red', relief=RIDGE, font=self.font_n)
        b2_3_2.grid(row=11, column=1, pady=3, padx=3, sticky=E)
        b2_3_3 = Button(self, text="2", bg='red', relief=RIDGE, font=self.font_n)
        b2_3_3.grid(row=11, column=2, pady=3, padx=3)
        b2_3_4 = Button(self, text="3", bg='red', relief=RIDGE, font=self.font_n)
        b2_3_4.grid(row=11, column=3, pady=3, padx=3, sticky=W)

        l2_3_1 = Label(self, text="play results of　AuxIVA", bg='LightSkyBlue', relief=RIDGE, font=self.font_n)
        l2_3_1.grid(row=12, column=0, pady=3, padx=3, sticky=W)
        b2_3_2 = Button(self, text="1", bg='red', relief=RIDGE, font=self.font_n)
        b2_3_2.grid(row=12, column=1, pady=3, padx=3, sticky=E)
        b2_3_3 = Button(self, text="2", bg='red', relief=RIDGE, font=self.font_n)
        b2_3_3.grid(row=12, column=2, pady=3, padx=3)
        b2_3_4 = Button(self, text="3", bg='red', relief=RIDGE, font=self.font_n)
        b2_3_4.grid(row=12, column=3, pady=3, padx=3, sticky=W)

        l2_3_1 = Label(self, text="play results of ILRMA", bg='LightSkyBlue', relief=RIDGE, font=self.font_n)
        l2_3_1.grid(row=13, column=0, pady=3, padx=3, sticky=W)
        b2_3_2 = Button(self, text="1", bg='red', relief=RIDGE, font=self.font_n)
        b2_3_2.grid(row=13, column=1, pady=3, padx=3, sticky=E)
        b2_3_3 = Button(self, text="2", bg='red', relief=RIDGE, font=self.font_n)
        b2_3_3.grid(row=13, column=2, pady=3, padx=3)
        b2_3_4 = Button(self, text="3", bg='red', relief=RIDGE, font=self.font_n)
        b2_3_4.grid(row=13, column=3, pady=3, padx=3, sticky=W)

        l3 = Label(self, text="3. Make Video", font=self.font_b)
        l3.grid(row=14, column=0, pady=7, padx=7, sticky=W)

        b3_1 = Button(self, text="make video", bg='green', relief=RIDGE, font=self.font_n)
        b3_1.grid(row=15, column=0, pady=3, padx=3, sticky=W+E)

        b3_2 = Entry(self)
        b3_2.grid(row=16, column=0, pady=3, padx=3, sticky=W+E)

        b3_3 = Button(self, text="play !!", bg='red', relief=RIDGE, font=self.font_n)
        b3_3.grid(row=17, column=0, pady=3, padx=3, sticky=W+E)

        b4 = Button(self, text="restart", bg='green', relief=RIDGE, font=self.font_n)
        b4.grid(row=18, column=3, pady=5, padx=5, sticky=W)


def main():
    root = Tk()
    root.geometry('480x720')
    root.title("Blind Source Separation")
    st = Separater(root)
    st.pack(side=TOP)

    root.mainloop()

if __name__=="__main__":
    main()

