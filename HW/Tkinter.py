from tkinter import *
# Python 2.X 可以用from Tkinter import *
 
def showPopoutMenu(w, menu):
    def popout(event):
        menu.post(event.x + w.winfo_rootx(), event.y + w.winfo_rooty()) 
        w.update() 
    w.bind('<Button-3>', popout) 
 
w = Tk()
w.title('Pop-Out Menu')
 
menu = Menu(w)
menu.add_cascade(label = '功能一')
menu.add_cascade(label = '功能二')
showPopoutMenu(w, menu)
 
w.mainloop()