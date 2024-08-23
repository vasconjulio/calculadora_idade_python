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
black = "#000000" #black
grey = "#363636" #grey
white = "#ffffff" #white
orange = "#fcc058" #orange

# criacao de frames
frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=black)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=300, pady=0, padx=0, relief=FLAT, bg=grey)
frame_baixo.grid(row=1, column=0)

# ----------------- criando labels para frame cima -----------------
l_calculadora = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=black, fg=white)
l_calculadora.place(x=0, y=30)

i_idade = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0, relief='flat', anchor='center', font=('Arial 35 bold'), bg=black, fg=orange)
i_idade.place(x=0, y=70)

# ----------------- funcao calcular idade -----------------

def calcular():
    inicial=cal_1.get()
    terminio=cal_2.get()


    print(inicial, terminio)

# ----------------- criando labels para frame baixo -----------------
l_data_inicial = Label(frame_baixo, text="Data inicial", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Ivy 11 bold'), bg=grey, fg=white)
l_data_inicial.place(x=40, y=30)

cal_1 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=white, borderwidth=2, data_patter='mm/dd/y', y=2024)
cal_1.place(x=170, y=30)

l_data_nascimento = Label(frame_baixo, text="Data nascimento", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Ivy 11 bold'), bg=grey, fg=white)
l_data_nascimento.place(x=40, y=70)

cal_2 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=white, borderwidth=2, data_patter='mm/dd/y', y=2024)
cal_2.place(x=170, y=70)

l_app_anos = Label(frame_baixo, text="27", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Ivy 25 bold'), bg=grey, fg=white)
l_app_anos.place(x=60, y=135)
l_app_anos_nome = Label(frame_baixo, text="Anos", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Ivy 11 bold'), bg=grey, fg=white)
l_app_anos_nome.place(x=60, y=175)

l_app_meses = Label(frame_baixo, text="12", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Ivy 25 bold'), bg=grey, fg=white)
l_app_meses.place(x=140, y=135)
l_app_meses_nome = Label(frame_baixo, text="Meses", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Ivy 11 bold'), bg=grey, fg=white)
l_app_meses_nome.place(x=140, y=175)

l_app_dias = Label(frame_baixo, text="27", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Ivy 25 bold'), bg=grey, fg=white)
l_app_dias.place(x=220, y=135)
l_app_dias_nome = Label(frame_baixo, text="Dias", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Ivy 11 bold'), bg=grey, fg=white)
l_app_dias_nome.place(x=220, y=175)



janela.mainloop()