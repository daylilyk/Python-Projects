#
# Python 3.10
#
# Program: Web Page Generator
#
# Author(s): Lily Kiousis, The Tech Academy
#
# Purpose: Creating a tool that can automatically create a basic HTML web page.
#          The page will be very simple, but my task is to create a Tkinter GUI
#          and python script that will create the .html file needed.

#   import needed modules
import tkinter as tk
from tkinter import *
import webbrowser

#   Creating master window
class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")

        # Custom text and default text
        self.lbl_entry = tk.Label(self.master, text ='Enter custom text or click the Default HTML page button')
        self.lbl_entry.grid(row=0, column=0, padx=(10,10), pady=(10,10), sticky= N+W)
        # Custom text entry window
        self.txt_entry = tk.Entry(self.master, text='')
        self.txt_entry.grid(row=1,column=0,columnspan=6,padx=(10,10),pady=(0,0), sticky = N+E+W)
        # Submit Custom Text button
        self.btn1 = Button(self.master, text="Submit Custom Text", width=20, height=2,command = self.customHTML)
        self.btn1.grid(row = 2, column=4, padx=(10,10), pady=(10,10), sticky=S+E)        
        # Creating Default Button
        self.btn = Button(self.master, text="Default HTML Page", width=20, height=2, command = self.defaultHTML)
        self.btn.grid(row = 2, column=3, padx=(10,10), pady=(10,10), sticky= S+E)

    #   Adding functionality to Default Button
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    #   Adding functionality to Custom Text Button
    #   Duplicate of defaultHTML function with edits to htmlText and htmlContent.
    def customHTML(self):
        htmlText = self.txt_entry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
