import tkinter as tk

dis=tk.Tk('Wordle')
dis.geometry('500x500')
a=tk.Text(dis,height = 5,width = 20)
a.pack()

def changecolour():
        bta.config(bg = "white",fg="red")


bta=tk.Button(dis, text="A", compound ="center", font=("Arial",20), fg="white",bg = "black", command=changecolour)
bta.pack()




































dis.mainloop()