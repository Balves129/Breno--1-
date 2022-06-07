from tkinter import*
import os 

janela= Tk()

janela.geometry('450x500+500+550')
janela.config(bg="#F8F8FF")
janela.minsize(width=200, height=500 )
janela.maxsize(width=2000, height=2000)


fr1= Frame(janela, bg='white', highlightbackground='#FF4500', highlightthickness=2)
fr2= Frame(janela,bg='white', highlightbackground='#FF4500',highlightthickness=2)


img=PhotoImage(file="Cod.png")


labelimg= Label(janela, image=img, bg='#F8F8FF')

label1= Label(fr1, text='Dados', font='Arial 16', bg='white', foreground='Black')
label2= Label(fr1, text='Nome:', font='Arial 16', bg='white', foreground='Black')
label3= Label(fr1, text='Data Nasc:', font='Arial 16', bg='white', foreground='Black')
label4= Label(fr1, text='CPF:', font='Arial 16', bg='white', foreground='Black')
label5= Label(fr1, text='Telefone:', font='Arial 16', bg='white', foreground='Black')

label6= Label(fr2, text='Endereço', font='Arial 16', bg='white', foreground='Black')
label7= Label(fr2, text='Rua:', font='Arial 16', bg='white', foreground='Black')
label8= Label(fr2, text='Bairro:', font='Arial 16', bg='white', foreground='Black')
label9= Label(fr2, text='Cidade:', font='Arial 16', bg='white', foreground='Black')
label10=Label(fr2, text='Nº:', font='Arial 16', bg='white', foreground='Black')
label11=Label(fr2, text='UF:', font='Arial 16', bg='white', foreground='Black')

entry1= Entry(fr1, font= "Arial 12", highlightbackground='purple', highlightthickness=1)
entry2= Entry(fr1, font='Arial 12',highlightbackground='purple', highlightthickness=1)
entry3= Entry(fr1, font='Arial 12',highlightbackground='purple', highlightthickness=1)
entry4= Entry(fr1, font='Arial 12',highlightbackground='purple', highlightthickness=1)
entry5= Entry(fr2, font='Arial 12',highlightbackground='purple', highlightthickness=1)
entry6= Entry(fr2, font='Arial 12',highlightbackground='purple', highlightthickness=1)
entry7= Entry(fr2, font='Arial 12',highlightbackground='purple', highlightthickness=1)
entry8= Entry(fr2, font='Arial 12',highlightbackground='purple', highlightthickness=1)
entry9= Entry(fr2, font='Arial 12',highlightbackground='purple', highlightthickness=1)


btn1 = Button(fr2, text="Gravar Dados", font='Arial 12', foreground= "Black", bg='#708090')
btn2 = Button(fr2, text="Listar Dados", font='Arial 12', foreground= "Black", bg='#708090')

fr1.grid(row=1, column=0, sticky=EW)
fr2.grid(row=2, column=0)


labelimg.grid(row=0, column=0)
label1.grid(row=0, column=0, sticky=EW)
label2.grid(row=1, column=0 ,sticky= EW)
label3.grid(row=2, column=0 ,sticky=EW)
label4.grid(row=3, column=0 ,sticky=EW)
label5.grid(row=4, column=0 ,sticky=EW)
label6.grid(row=0, column=0 ,sticky=EW)
label7.grid(row=1, column=0 ,sticky=EW)
label8.grid(row=2, column=0 ,sticky=EW)
label9.grid(row=1, column=2 ,sticky=EW)
label10.grid(row=2, column=4 ,sticky=EW)
label11.grid(row=2, column=2 ,sticky=EW)

entry1.grid(row=1, column=1 ,sticky=EW)
entry2.grid(row=2, column=1 ,sticky=EW)
entry3.grid(row=3, column=1 ,sticky=EW)
entry4.grid(row=4, column=1 ,sticky=EW)
entry5.grid(row=1, column=1 ,sticky=EW)
entry6.grid(row=1, column=3 ,sticky=EW)
entry7.grid(row=2, column=1 ,sticky=EW)
entry8.grid(row=2, column=3 ,sticky=EW)
entry9.grid(row=2, column=5 ,sticky=EW)
btn1.grid(row=3, column=0, sticky= EW)
btn2.grid(row=3, column=1, sticky= EW)


janela.mainloop()
