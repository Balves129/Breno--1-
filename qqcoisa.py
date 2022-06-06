from tkinter import *


def somar():
    try:
        label3['text']= int(entry1.get())+ int(entry2.get())
        label3['foreground']= 'Blue'
    except:
        label3['text']= 'Não válido'
        label3['foreground'] = 'Red'

janela= Tk()
janela.geometry('800x700+200+500')
janela.config(bg="white")
janela.minsize(width= 200, height= 200)
janela.maxsize(width= 2000, height= 2000)

#06/06 
fr1= Frame(janela, bg='white')
fr2= Frame(janela,bg='white')

label3 = Label(fr2, text="", font = "Arial 20 ",bg="white", foreground="blue")

label1 = Label(fr1, text="AULÃO DO BRENO 2022",
               font = "Algerian 47 ", bg="white",foreground="Blue")
label2= Label(fr1, text="+",font="Arial 20", foreground="blue" , bg='white')
entry1= Entry(fr1, font= "Rockwell 20")
entry2= Entry(fr2, font= "Rockwell 20")
btn1 = Button(fr2, text="somar", font='Rockwell 40', foreground= "blue", bg='white',command=somar)


fr1.pack()
fr2.pack()
label1.pack(side=TOP)
label3.pack(side=TOP)
entry1.pack(side=TOP)
label2.pack(side=TOP)
entry2.pack(side=TOP)
btn1.pack(side= TOP)

janela.mainloop()
