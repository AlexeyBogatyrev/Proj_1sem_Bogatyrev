#Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы
#неравенства A > 2 и B < 3».

from tkinter import *


def num(event):
    x = int(num1.get())
    y = int(num2.get())
    if x > 2 and y < 3:
        plus["text"] = "Высказывание верно"
    if x < 2 and y > 3:
        plus["text"] = "Высказывание не верно"


root = Tk()
root.title("Проверка высказывания")
root.geometry("300x100")

Label(text="Число A:").grid(row=1, column=0)
num1 = Entry()
num1.grid(row=1, column=1)

Label(text="Число B:").grid(row=2, column=0)
num2 = Entry()
num2.grid(row=2, column=1)

button1 = Button(text="Узнать результат")
button1.grid(row=4, column=1)

plus = Label()
plus.grid(row=5, column=1)

button1.bind("<Button-1>", num)

root.mainloop()
