#
# Python 3.10
#
# Program: File Transfer
#
# Author: Lily Kiousis, The Tech Academy
#
# Purpose: To build a program that allows files to be moved from one folder to
#          another with the click of a button. 
#          This script will serve to create a GUI that will act as the 
#          interface for users to transfer files from one directory to another.
#
# OS: This program was written and tested on Windows 10.



#   import tkinter module
import tkinter as tk
from tkinter import *

#   importing tkinter.filedialog module to add functions that allow the user to select
#   a source directory and destination directory for text documents made in provided
#   customer source/destination folders.
import tkinter.filedialog
import os
import shutil
import time
from datetime import datetime
from datetime import timedelta

#   creating ParentWindow() with master and giving a title to GUI window
#   Using Frame widget for grouping and organization of program widgets
class ParentWindow(Frame):
    def __init__(self, master): 
        Frame.__init__(self)
        # Sets title of GUI window
        self.master.title("File Transfer")


        # Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width = 20, command=self.sourceDir)
        # Positions source button int GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30,0))

        # Creates entry for source direction selection
        self.source_dir = Entry(width=75)
        # Positions entry GUI using tkinter grid() padx and pady are the same
        # as the button to ensure they will line up.
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        # Creates button to select destination of file from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        # Positions destination button in GUI using tkinter grid()
        # on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        # Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        # Positions entry in GUI using tkinter grid() padx and pady are the same as the
        # button to ensure they will line up.
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))

        # Creates a button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        # Positions transfer file button
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        # Creates an Exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        # Positions the Exit button
        self.exit_btn.grid(row=2, column=2, padx=(10,10), pady=(0,15))

    # Creates function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        # The .delete(0,END) will clear the content that is inserted in the Entry widget,
        # this allows the path to be inserted into the Entry widget properly.
        self.source_dir.delete(0,END)
        # The .insert method will insert the user selevtion to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)


    # Creates function to select destination directory.
    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        # The .delete(0,END) will clear the content that is inserted in the Entry widget,
        # this allows the path to be inserted into the Entry widget properly.
        self.destination_dir.delete(0,END)
        # The .insert method will insert the user selevtion to the destination_dir Entry
        self.destination_dir.insert(0, selectDestDir)


    # Creates function to transfer files from one directory to another
    def transferFiles(self):
        #Gets source directory
        source = self.source_dir.get()
        #Gets destination directory
        destination = self.destination_dir.get()
        #Gets a list of files in the source directory
        source_files = os.listdir(source)
        # To save time at moment of command, give current time
        # and create parameters for 24 hour cycle.
        current_time = datetime.now()
        cycle = current_time - timedelta(days=1)
        #Runs through each file in the source directory
        for i in source_files:
            # Set i to represent files regardless of folder choice
            i = os.path.join(source,i)
            # Tell program to get the created/modification time of each
            # individual file
            modification_time = os.path.getmtime(i)
            # Change modification time to datetime data type instead of float
            mod_datetime = datetime.fromtimestamp(modification_time)
            # Tell program to transfer files only within mod_datetime and cycle time frame
            if mod_datetime >= cycle:
                # Moves each file from the source to the destination
                # Changed to i since I made 
                shutil.move(i, destination)
                print(i + ' was successfully transferred.')

    # Creates function to exit program
    def exit_program(self):
        # root is the main GUI window, the Tkinter destroy method tells python to
        # terminate root.mainloop and all widgets inside the GUI window
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
