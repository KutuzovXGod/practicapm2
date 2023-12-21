from tkinter import *

root = Tk()

root['bg'] = '#fafafa'
root.title('Название программы') # имя формы
root.wm_attributes('-alpha', 0.7)
root.geometry('300x250') # размер формы

root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack()

frame = Frame(root, bg='red')
frame.place(relx=0.15, rely=0.5, relwidth=0.7, relheight=0.7)

title = Label(frame, text='Текста подсказка', bg='gray', font=40)
title.pack()
btn = Button(frame, text='Кнопка', bg='yellow')
btn.pack()

root.mainloop()