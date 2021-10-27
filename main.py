from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

# colors
fundo = '#3b3b3b'
cor_frame = '#ffffff'
cor_font = '#48b3e0'  # azul

root = Tk()
root.title('')
root.geometry('650x260')
root.config(bg=fundo)

frame_top = Frame(root, width=450, height=50, bg=cor_frame, padx=0, pady=3, relief='flat')
frame_top.place(x=2, y=2)

frame_e = Frame(root, width=450, height=220, bg=cor_frame, padx=0, pady=3, relief='flat')
frame_e.place(x=2, y=54)

frame_d = Frame(root, width=198, height=260, bg=cor_frame, padx=0, pady=3, relief='flat')
frame_d.place(x=454, y=2)

style_r = ttk.Style(root)
style_r.theme_use('clam')


l_title = Label(frame_top, text='CALCULADORA DE UNIDADES DE MEDIDAS', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 11 bold'), bg=cor_frame, fg=cor_font)
l_title.place(x=50, y=10)

# ---------------------------------funcioanlidades------------------------------------

unidades = {'massa':[{'kg':1000}, {'hg':100}, {'dag':10}, {'g':1}, {'dg':0.1}, {'cg':0.01}, {'dag':0.001}],
            'comprimento':[{'km':1000}, {'hm':100}, {'dam':10}, {'m':1}, {'dm':0.1}, {'cm':0.01}, {'mm':0.001}]
            }

def mostrar_menu(i):
    unidade_de = []
    unidade_para = []
    unidade_valores = []

    for j in unidades[i]:
        for k, v in j.items():
            unidade_de.append(k)
            unidade_para.append(k)
            unidade_valores.append(v)

    c_de['values'] = unidade_de
    c_para['values'] = unidade_para

    l_frame_d['text'] = i
    
    

    def calcular():
        # obter as unidades de medidas
        a = c_de.get()
        b = c_para.get()

        num_a_ser_convertido = float(e_numero.get())

        if unidade_para.index(a) <= unidade_de.index(b):

            distancia = unidade_para.index(b) - unidade_de.index(a)
            result = num_a_ser_convertido * (10 ** distancia)
            l_resultado['text'] = result
            

        else:
            distancia = unidade_de.index(a) - unidade_para.index(b)
            result = num_a_ser_convertido * (10 ** distancia)
            l_resultado['text'] = result

        # divisão -------------------------------------------

        if unidade_para.index(a) > unidade_de.index(b):

            if unidade_de.index(a) <= unidade_para.index(b):

                distancia = unidade_de.index(b) - unidade_para.index(a)
                result = num_a_ser_convertido / (10 ** distancia)
                l_resultado['text'] = result

            else:
                distancia = unidade_de.index(a) - unidade_para.index(b)
                result = num_a_ser_convertido / (10 ** distancia)
                l_resultado['text'] = result


    l_info = Label(frame_d, text='Digite o número.', width=16, height=2, padx=5, pady=3, relief='flat', anchor='center', font=('Ivy 9 bold'), bg=cor_frame, fg=fundo)
    l_info.place(x=0, y=110)

    e_numero = Entry(frame_d, text='', width=9, font=('Ivy 11 bold'), justify=('center'), relief=SOLID)
    e_numero.place(x=10, y=150)

    b_calcular = Button(frame_d, text='Calcular', command=calcular, width=6, relief='raised', justify=('center'), font=('Ivy 8'), bg=cor_font)
    b_calcular.place(x=118, y=150)

    l_resultado = Label(frame_d, text='', width=15, height=2, padx=5, pady=3, relief='groove', anchor='center', font=('Ivy 13 bold'), bg=cor_frame, fg=fundo)
    l_resultado.place(x=0, y=200)


# ----------------------------------Config frames-------------------------------------

img_1 = Image.open('images/volumeicon.png')
img_1 = img_1.resize((35,35), Image.ANTIALIAS)
img_1 = ImageTk.PhotoImage(img_1)
b_1 = Button(frame_e, command=lambda:mostrar_menu('massa'), text='Massa', image=img_1, compound=LEFT, width=112, height=41, relief='flat', overrelief='solid', anchor='nw', font=('Ivy 8 bold'), bg=cor_font, fg=cor_frame)
b_1.grid(row=0, column=0, sticky=NSEW, padx=5, pady=5)

img_2 = Image.open('images/timeicon.png')
img_2 = img_2.resize((35,35), Image.ANTIALIAS)
img_2 = ImageTk.PhotoImage(img_2)
b_2 = Button(frame_e, text='Tempo', image=img_2, compound=LEFT, width=112, height=41, relief='flat', overrelief='solid', anchor='nw', font=('Ivy 8 bold'), bg=cor_font, fg=cor_frame)
b_2.grid(row=0, column=1, sticky=NSEW, padx=5, pady=5)

img_3 = Image.open('images/regua.png')
img_3 = img_3.resize((35,35), Image.ANTIALIAS)
img_3 = ImageTk.PhotoImage(img_3)
b_3 = Button(frame_e, command=lambda:mostrar_menu('comprimento'), text='Comprimento', image=img_3, compound=LEFT, width=112, height=41, relief='flat', overrelief='solid', anchor='nw', font=('Ivy 8 bold'), bg=cor_font, fg=cor_frame)
b_3.grid(row=0, column=2, sticky=NSEW, padx=5, pady=5)

img_4 = Image.open('images/squareicon.png')
img_4 = img_4.resize((40,40), Image.ANTIALIAS)
img_4 = ImageTk.PhotoImage(img_4)
b_4 = Button(frame_e, text='Área', image=img_4, compound=LEFT, width=112, height=41, relief='flat', overrelief='solid', anchor='nw', font=('Ivy 8 bold'), bg=cor_font, fg=cor_frame)
b_4.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5)

img_5 = Image.open('images/volumeicon.png')
img_5 = img_5.resize((40,40), Image.ANTIALIAS)
img_5 = ImageTk.PhotoImage(img_5)
b_5 = Button(frame_e, text='Quantidade', image=img_5, compound=LEFT, width=112, height=41, relief='flat', overrelief='solid', anchor='nw', font=('Ivy 8 bold'), bg=cor_font, fg=cor_frame)
b_5.grid(row=1, column=1, sticky=NSEW, padx=5, pady=5)

img_6 = Image.open('images/speedicon.png')
img_6 = img_6.resize((40,40), Image.ANTIALIAS)
img_6 = ImageTk.PhotoImage(img_6)
b_6 = Button(frame_e, text='Velocidade', image=img_6, compound=LEFT, width=112, height=41, relief='flat', overrelief='solid', anchor='nw', font=('Ivy 8 bold'), bg=cor_font, fg=cor_frame)
b_6.grid(row=1, column=2, sticky=NSEW, padx=5, pady=5)

img_7 = Image.open('images/temperaturaicon.png')
img_7 = img_7.resize((40,40), Image.ANTIALIAS)
img_7 = ImageTk.PhotoImage(img_7)
b_7 = Button(frame_e, text='Temperatura', image=img_7, compound=LEFT, width=112, height=41, relief='flat', overrelief='solid', anchor='nw', font=('Ivy 8 bold'), bg=cor_font, fg=cor_frame)
b_7.grid(row=2, column=0, sticky=NSEW, padx=5, pady=5)

img_8 = Image.open('images/timeicon.png')
img_8 = img_8.resize((40,40), Image.ANTIALIAS)
img_8 = ImageTk.PhotoImage(img_8)
b_8 = Button(frame_e, text='Energia', image=img_8, compound=LEFT, width=112, height=41, relief='flat', overrelief='solid', anchor='nw', font=('Ivy 8 bold'), bg=cor_font, fg=cor_frame)
b_8.grid(row=2, column=1, sticky=NSEW, padx=5, pady=5)

img_9 = Image.open('images/timeicon.png')
img_9 = img_9.resize((40,40), Image.ANTIALIAS)
img_9 = ImageTk.PhotoImage(img_9)
b_9 = Button(frame_e, text='Pressão', image=img_9, compound=LEFT, width=112, height=41, relief='flat', overrelief='solid', anchor='nw', font=('Ivy 8 bold'), bg=cor_font, fg=cor_frame)
b_9.grid(row=2, column=2, sticky=NSEW, padx=5, pady=5)

# screen rigth
l_frame_d = Label(frame_d, text='Compreimento',width=16, height=2, padx=1, relief='groove', anchor='center', font=('Ivy 14 bold'), bg=cor_frame, fg=fundo)
l_frame_d.place(x=0, y=0)

l_de = Label(frame_d, text='De', height=1, padx=2, pady=3, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor_frame, fg=fundo)
l_de.place(x=10, y=70)
c_de = ttk.Combobox(frame_d, width=5, justify=('center'), font=('Ivy 8'))
c_de.place(x=38, y=70)

l_para = Label(frame_d, text='Para', height=1, padx=2, pady=3, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor_frame, fg=fundo)
l_para.place(x=100, y=70)
c_para = ttk.Combobox(frame_d, width=5, justify=('center'), font=('Ivy 8'))
c_para.place(x=138, y=70)







root.mainloop()
