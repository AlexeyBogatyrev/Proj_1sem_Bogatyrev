from tkinter import*
from tkinter.font import BOLD
from tkinter.ttk import Combobox

root = Tk()

root.title("Обработка формы - Mozilla Firefox")
root.geometry("600x700")
Label(text="Форма регистрации пользователя", width=50, font=("Arial", 15, BOLD)).place(x=15, y=30)
Label(text="Форма регистрации пользователя", width=50, fg='black', font=('arial', 15, BOLD)).place(x=20, y=30)
Label(text="Ваше имя:", width=25, fg='black', font='arial 11').place(x=19, y=90)
Entry(width=25, bd=0, bg='silver', font='arial 15').place(x=250, y=90)
Label(text="Пароль:", width=25, fg='black', font='arial 11').place(x=10.5, y=125)
Entry(width=25, bd=0, bg='silver', font='arial 15').place(x=250, y=125)
Label(text="Возраст:", width=25, fg='black', font='arial 11').place(x=13.5, y=160)
Entry(width=25, bd=0, bg='silver', font='arial 15').place(x=250, y=160)
Label(text="Пол:", width=25, fg='black', font='arial 11').place(x=-1, y=195)
Radiobutton(root, text='Мужской', value=0).place(x=250, y=195)
Radiobutton(root, text='Женский', value=1).place(x=450, y=195)
Label(text="Ваши увлечения:", width=25, fg='black', font='arial 11').place(x=41, y=230)
Checkbutton(root, text='Музыка', onvalue=1, offvalue=0).place(x=250, y=230)
Checkbutton(root, text='Видео', onvalue=1, offvalue=0).place(x=350, y=230)
Checkbutton(root, text='Рисование', onvalue=1, offvalue=0).place(x=450, y=230)
Label(text="Ваша страна:", width=25, fg='black', font='arial 11').place(x=28.5, y=265)
combo = Combobox(root)

combo.current()
combo.place(x=250, y=265)
Label(text="Ваш город:", width=25, fg='black', font='arial 11').place(x=20, y=300)
combo = Combobox(root)
combo.current()
combo.place(x=250, y=300)
Label(text="Кратко о себе:", width=25, fg='black', font='arial 11').place(x=33, y=335)
Text(root, width=45, height=3, bg='silver', font='Arial 8').place(x=250, y=335)
Label(text="Решите пример, запишите результат в поле ниже:",
      width=100, fg='black', font='arial 11').place(x=-185, y=400)
Entry(width=25, bd=0, bg='silver', font='arial 15').place(x=250, y=450)
Button(root, text='Отменить ввод', bd=0, width=11,
       height=1, bg='silver', fg='black', font='arial 10').place(x=250, y=480)
Button(root, text='Данные подтверждаю', bd=0, width=21,
       height=1, bg='silver', fg='black', font='arial 10').place(x=353, y=480)
root.mainloop()
