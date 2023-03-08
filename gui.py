#starting with buttons for enter, delete and letters
import tkinter as tk
from tkinter import PhotoImage


#creating gui window called dis (display)
#dis=tk.Tk('Wordle')
#dis.geometry('500x500')

#creating a button making function

list_of_button_labels=[
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

'''
gr_gr = PhotoImage(file='b_gr_gr.png')
y_y = PhotoImage(file='b_y_y.png')
g_g = PhotoImage(file='b_g_g.png')
gr_y = PhotoImage(file='b_gr_y.png')
y_gr = PhotoImage(file='b_y_gr.png')
gr_y = PhotoImage(file='b_gr_y.png')
y_gr = PhotoImage(file='b_y_gr.png')
y_g = PhotoImage(file='b_y_g.png')
g_y = PhotoImage(file='b_g_y.png')
'''
#bt=tk.Button(dis, text="A", compound ="center", font=("Arial",20), fg="white",bg = "black").pack()

#def color_changer():


#Dataset for buttons
row_1_dict=dict()
row_2_dict=dict()
row_3_dict=dict()


#code for creating dictionary of button codes
for i in 'qwertyuiop':
    print(f'button{1}{i}=tk.Button(frame_keyboard_1, text={i.upper()}, compound ="center", font=("Arial",20), fg="white",bg = "black", command=button_func(i)).grid(row = 1,column = {"qwertyuiop".index(i)})')
for i in 'asdfghjkl':
    print(f'button{2}{i}=tk.Button(frame_keyboard_2, text={i.upper()}, compound ="center", font=("Arial",20), fg="white",bg = "black", command=button_func(i)).grid(row = 2,column = {"asdfghjkl".index(i)})')
for i in 'zxcvbnm':
    print(f'button{3}{i}=tk.Button(frame_keyboard_3, text={i.upper()}, compound ="center", font=("Arial",20), fg="white",bg = "black", command=button_func(i)).grid(row = 3,column = {"zxcvbnm".index(i)})')
#print(row_1_dict,row_2_dict,row_3_dict,sep='\n')


   



#dis.mainloop()    