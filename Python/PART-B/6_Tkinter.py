# 6. Create a GUI using Tkinter module 
import tkinter as tk

w = tk.Tk()
w.title('Tkinter GUI')
l = tk.Label(w,text='')
b = tk.Button(w,text='Click Me', command=lambda:l.config(text='Button Clicked!')).pack()
l.pack()
tk.mainloop()





# window = tk.Tk()

# window.title('Tkinter GUI by me') # main window

# # window.geometry('500x500') # size of the window  

# # window.config(bg='lightblue') # background color of the window

# tk.Label(window,text='Hi this Tkinter GUI Lable').pack() # lable property of tk module -> Lable is a  function of tk module 
# # pack()->set position automatically in a window

# tk.mainloop() # is used to run the main window


