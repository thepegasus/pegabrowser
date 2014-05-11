#!/usr/bin/python3
from tkinter import *
from urllib.request import *
#from tkinter.ttk import *
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", str(tag))
    def handle_endtag(self, tag):
        print("Encountered an end tag :", str(tag))
    def handle_data(self, data):
        print("Encountered some data  :", str(data))


class pegaBrowser:
    url=None
    topFrame=None
    contentFrame=None
    frame_padx="1m"
    frame_pady="1m"
    frame_ipadx="1m"
    frame_ipady="1m"
    def __init__(self, master=None):
        mainContainer=Frame(master)
        mainContainer.pack(side=LEFT, fill=X, expand=YES,anchor=NW, padx=self.frame_padx,pady=self.frame_pady)

        self.topFrame=Frame(mainContainer, borderwidth=1)
        self.topFrame.pack(side=TOP, fill=X, expand=YES, anchor=W)

        self.contentFrame=Frame(mainContainer, borderwidth=1)
        self.contentFrame.pack(side=TOP, fill=BOTH, expand=YES,anchor=W) 

        self.initializeScreen()
        
    def initializeScreen(self):
        self.addressLabel=Label(self.topFrame, text="Address")
        #self.addressLabel.configure(padx="1m", pady="1m")
        self.addressLabel.pack(side=LEFT)
        self.addressBar=Entry(self.topFrame, width=50,borderwidth=1)
        
        #self.addressBar.configure(padx="1m", pady="1m")
        #For easy debug
        self.addressBar.insert(0,"http://google.com")
        self.addressBar.pack(side=LEFT, fill=X, expand=YES)
        self.goButton=Button(self.topFrame,text="Go")
        self.goButton.configure(padx="1m", pady="1m", width=6, height=1)
        self.goButton.pack(side=LEFT)
        self.goButton.bind("<Button-1>",self.goButtonHandler)        
        
        self.contentArea=Label(self.contentFrame)
        self.contentArea.pack(side=BOTTOM,fill=BOTH, expand=YES)
    def goButtonHandler(self, event):
        self.url=self.addressBar.get()
        #self.contentArea["text"]="Fetching "+self.url
        htmlData=getHttpResource(self.url)    
        self.contentArea["text"]=htmlData
        parser = MyHTMLParser()
        parser.feed(str(htmlData))

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
root.geometry("800x600") 
pegabrowser=pegaBrowser(root)
root.mainloop()
