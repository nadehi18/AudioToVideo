#!/usr/bin/env python

import ffmpy
import multiprocessing
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter import *
from time import sleep
import sys
import os


class App():

    def __init__(self, master):

        
        # Init stuff
        frame = Frame(master)

        master.minsize(width=400, height=300)

        self.audio_text = StringVar() 
        self.image_text = StringVar()
        self.output_text = StringVar()
        self.converting_text = StringVar()
        self.audio_path = None
        self.image_path = None
        self.output_path = None
        self.master = master
        self.done = False

       
        
        
        self.import_audio_button = Button(master, text="Select Audio File", command=self.OpenAudioDialog)
        self.import_audio_button.pack()
        self.audio_textbox = Label(master, textvariable=self.audio_text).pack()
        
        self.import_image_button = Button(master, text="Select Image File", command=self.OpenImageDialog)
        self.import_image_button.pack()
        self.image_textbox = Label(master, textvariable=self.image_text).pack()

        self.output_video_button = Button(master, text="Select Output File Destination", command=self.OpenOutputDialog)
        self.output_video_button.pack()
        self.image_textbox = Label(master, textvariable=self.output_text).pack()

        self.convert_button = Button(master, text="Create Video", command=self.Convert)
        self.convert_button.pack()

        self.converting_textbox = Label(master, textvariable=self.converting_text).pack()
        
       
        frame.pack()

    def OpenAudioDialog(self):

        ftypes = [('MP3 Files', '*.mp3'), ('WAV Files', '*.wav'), ('All files', '*')]
        self.audio_path = askopenfilename(filetypes = ftypes)

        self.audio_text.set(self.audio_path)

    def OpenImageDialog(self):

        ftypes = [('PNG Files', '*.png'), ('JPG Files', '*.jpg'), ('All files', '*')]
        self.image_path = askopenfilename(filetypes = ftypes)

        self.image_text.set(self.image_path)

    def OpenOutputDialog(self):

        self.output_path = asksaveasfile(mode='w', defaultextension=".mkv").name

        self.output_text.set(self.output_path)

    def Convert(self):

        self.converting_text.set("Converting...  Please Wait.")

        self.master.update()

        os.remove(self.output_path)

        ff = ffmpy.FFmpeg( inputs={self.image_path: ['-loop', '1', '-r', '1'], self.audio_path: None}, 
                        outputs={self.output_path: ['-c:a', 'copy', '-c:v', 'libx264', '-preset', 'fast', '-threads', '0', '-shortest']})

        ff.run()

        self.converting_text.set("Done. \n Your video should now be available at: \n" + self.output_path)


   



        


if __name__ == '__main__':
  
    #Start the main GUI
    root = Tk()
    root.iconbitmap(default='favicon.ico')
    root.title("Audio To Video")  
    app = App(root)
    root.mainloop()
