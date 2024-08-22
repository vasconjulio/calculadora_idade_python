# importanto biblioteca Tkinter
from tkinter import *
from tkinter import ttk

# importando tkcalendar
from tkcalendar import Calendar, DateEntry

# criação janela e configurações basicas
janela =Tk()
janela.title("Calculadora de Idade")
janela.geometry('310x400')

# cores
cor1 = "#000000" #black
cor2 = "#363636" #grey
cor3 = "#ffffff" #white
cor4 = "#fcc058" #orange

# criacao de frames
frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=cor1)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=300, pady=0, padx=0, relief=FLAT, bg=cor2)
frame_baixo.grid(row=1, column=0)


# criacao label cima
l_calculadora = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=cor1, fg=cor3)
l_calculadora.place(x=0, y=30)

i_idade = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0, relief='flat', anchor='center', font=('Arial 35 bold'), bg=cor1, fg=cor4)
i_idade.place(x=0, y=70)

# criacao label baixo
l_data_inicial = Label(frame_baixo, text="Data inicial", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Ivy 11 bold'), bg=cor2, fg=cor3)
l_data_inicial.place(x=50, y=30)

cal_1 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, data_patter='dd/mm/y', y=2024)
cal_1.place(x=170, y=30)

l_data_nascimento = Label(frame_baixo, text="Data nascimento", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Ivy 11 bold'), bg=cor2, fg=cor3)
l_data_nascimento.place(x=50, y=70)



janela.mainloop()