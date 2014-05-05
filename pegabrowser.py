#!/usr/bin/python3
from tkinter import *
from urllib.request import *
#from tkinter.ttk import *
class pegaBrowser(Frame):
    url=None
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.initializeScreen()
    def initializeScreen(self):
        self.addressLabel=Label(text="Address")
        self.addressLabel.pack(side=LEFT)
        self.addressBar=Entry(width=100)
        #For easy debug
        self.addressBar.insert(0,"http://google.com")
        self.addressBar.pack(side=LEFT)
        self.goButton=Button(text="Go")
        self.goButton.pack(side=LEFT)
        self.goButton.bind("<Button-1>",self.goButtonHandler)
        self.contentArea=Label(text="Content Area")
        self.contentArea.pack(side=LEFT, fill=X, expand=1)
    def goButtonHandler(self, event):
        self.url=self.addressBar.get()
        #self.contentArea["text"]="Fetching "+self.url
        htmlData=getHttpResource(self.url)    
        self.contentArea["text"]=htmlData

def getHttpResource(url):
        #Get resource from server
        response=urlopen(url)
        html=response.read()
        return html

       

root=Tk()
root.title("PegaBrowser - 0.1")

#root.minsize(600,400)
#Start the window maximized
#w,h=root.winfo_screenwidth(), root.winfo_screenheight()
#root.geometry("%dx%d+0+0" % (w,h)) 
pegabrowser=pegaBrowser(root)
pegabrowser.mainloop()
