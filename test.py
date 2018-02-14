import wx
import speech_recognition as sr
import pyaudio

class win(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Test',size=(400,100))
        panel=wx.Panel(self)
        schliessen=wx.Button(panel,label='Schließen',pos=(150,20),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.closebutton,schliessen)
        self.Bind(wx.EVT_CLOSE,self.closewin)
        self.start=wx.Button(panel,label="Start",pos=(20,20),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.go,self.start)
        self.stop=wx.Button(panel,label="Stop",pos=(20,50),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.halt,self.stop)
    def go(self,event):
        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Höre zu...")
            self.audio = self.r.listen(source,timeout=1,phrase_time_limit=10)
    def halt(self,event):
        print(self.r.recognize_google(self.audio,language="de_DE"))
    def closebutton(self,event):
        self.Close(True)
    def closewin(self,event):
        self.Destroy()

if __name__=='__main__':
    app=wx.App()
    frame=win(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
