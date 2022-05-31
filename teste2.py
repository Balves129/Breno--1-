from tkinter import *
def aumentar():
    if int(label1['text'])< 10:
        label1['text']= int(label1['text']) +1

def diminuir():
    if int(label1['text'])> -10:
        label1['text']= int(label1['text']) -1
    
janela = Tk()

janela.minsize(width= 600, height= 500)
janela.maxsize(width= 2000, height= 2000)
janela.grid_rowconfigure(0, weight=1)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.bind('-', lambda event: diminuir())
janela.bind('+', lambda event: aumentar())


bt1 = Button(janela, text="+", font="Arial 30 bold",bg='red' ,command=aumentar)
label1=Label(janela, text="0", font="Arial 22",bg='white')
bt2 = Button(janela, text="-", font="Arial 30 bold",bg='red' ,command=diminuir)



bt1.grid(row=0, column=0, sticky=NSEW)
label1.grid(row=0,column=1,sticky=NSEW)
bt2.grid(row=0,column=2,sticky=NSEW)

janela.mainloop()
 
 