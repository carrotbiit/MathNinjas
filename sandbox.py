import mathfinal
from tkinter import *
from time import sleep
from tkinter import messagebox

global points
points = 0

def window():
    root = Tk()
    subject = "Math"
    grade = "1"
    def change():
        global points
        points = 0
        string = entry.get()
        entry.delete(0, END)
        yayornay = mathfinal.isright(question, string)
        
        if yayornay == "Yes" or yayornay == "yes":
            points = points + 100
            messagebox.showinfo("Good Job!", "Correct! Plus 100 points! You are now at: " + str(points) + " points") 
        else:
            points = points - 20
            messagebox.showinfo("Better luck next time", "Good try. -20 points. You are now at: " + str(points) + " points") 
        right.set(yayornay)
        
        var.set(mathfinal.getquestions(subject, grade))
        root.update_idletasks()
        return points


    def end():
        root.destroy
        
        


        

    var = StringVar()
    right = StringVar()

    global question
    question = mathfinal.getquestions("Math", "1")

    var.set(question)



    quit = Button(root, text = "Exit", width = 20, command = end)
    quit.place(relx = 0, 
                    rely = 0,
                    anchor = 'nw')

    l = Label(root, textvariable = var)
    l.pack()

    r = Label(root, textvariable = right)
    r.pack()

    b = Button(root, text = "Check", command = change)
    b.pack()

    entry = Entry(root, width= 40)
    entry.focus_set()
    entry.pack()

    root.mainloop()
    return points