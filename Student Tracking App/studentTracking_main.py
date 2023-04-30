#
# Python 3.10
#
# Project: Student Tracking application
#
# Author: Lily Kiousis
#
# Purpose: Here we will be creating a functioning application that allows a user to input student information and current course.
#          Utilizing sqlite3 and Tkinter that will store the first name, last name, phone number, email address, and current course.
#          The user will be able to add, submit, and delete students.
#
# Script Contents: This script will be used to provide the basic information and make the classes that will allow this script
#               to work.
#
# Tested OS: This code was written and tested with Windows 10.

# import Tkinter Module
from tkinter import *
import tkinter as tk

# importing author made modules
import student_gui
import student_func

# Frame is the tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define master frame configuration
        self.master = master
        self.master.minsize(500,350) #(Height, Width)
        self.master.maxsize(500,350)
        # This CenterWindow method will center the app on the user's screen
        student_func.center_window(self,500,350)
        self.master.title("The Tkinter Student Tracking App")
        self.master.configure(bg="#F0F0F0")
        # This protocol (rule) method is a tkinter built-in method to catch if
        # the user clicks the upper conrner, "X" on Window OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a seperate module,
        # keeping the code compartmentalized and clutter free.
        student_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

