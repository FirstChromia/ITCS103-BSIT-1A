import tkinter as tk

#Functions
bgcolor = "Darkblue"
fgcolor = "White"
space = 19

#Window
window = tk.Tk()
window.title("Terrence Skyler's Profile")
window.geometry("450x600")
window.resizable(False,True)
window.config(bg = bgcolor)

#Widgets
text = tk.Label(window,
                text = "Student Profile",
                font = ("timesnewroman", 25, "bold"),
                bg = bgcolor, 
                fg = fgcolor,
                )
text.pack()

name = tk.Label(window,
                text = "Name: Terrence Skyler C. Abril",
                font = ("timesnewroman", 12),
                bg = bgcolor, 
                fg = fgcolor,
                )
name.pack(pady = space, anchor = "w")
age = tk.Label(window,
                text = "Age: 19",
                font = ("timesnewroman", 12),
                bg = bgcolor, 
                fg = fgcolor,
                )
age.pack(pady = space, anchor = "w")
course = tk.Label(window,
                text = "Course: BSIT",
                font = ("timesnewroman", 12),
                bg = bgcolor, 
                fg = fgcolor,
                )
course.pack(pady = space, anchor = "w")
birthday = tk.Label(window,
                text = "Birthday: October 19,2006",
                font = ("timesnewroman", 12),
                bg = bgcolor, 
                fg = fgcolor,
                )
birthday.pack(pady = space, anchor = "w")
motto = tk.Label(window,
                text = "Motto:",
                font = ("timesnewroman", 12),
                bg = bgcolor, 
                fg = fgcolor,
                )
motto.pack(pady = 10, anchor = "w")
motto2 = tk.Label(window,
                text = "\tIf even one person is able to live a little bit easier\n because I existed,\n then I truly have succeeded",
                font = ("timesnewroman", 12),
                bg = bgcolor, 
                fg = fgcolor,
                )
motto2.pack(pady = space, anchor = "w")



window.mainloop()