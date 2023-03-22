import tkinter as tk
fenetre = tk.Tk()
fenetre.size = 400
fenetre.geometry('600x500')

valeur = ""
result = 0
list_result = []
def actionned_0():
    global valeur
    valeur = valeur + "0"
    texte_calculator.config(text=str(valeur))
def actionned_point():
    global valeur
    for i in valeur:
        if i == "":
            return 0
        else:
            valeur = valeur + "."
            texte_calculator.config(text=str(valeur))
def actionned_egal():
    global list_result
    global result
    global valeur
    list_result.append(valeur)
    print(list_result)
    for index,val in enumerate (list_result):
        if val == "+" and result == 0:
            result = float(list_result[index-1]) + float(list_result[index+1]) + result
        elif val == "+":
            result = result + float(list_result[index+1])

        if val == "x" and result == 0:
            result = float(list_result[index-1]) * float(list_result[index+1])+ result
        elif val == "x":
            result = result + float(list_result[index+1])
        
        if val == "/" and result == 0:
            result = float(list_result[index-1]) / float(list_result[index+1])+ result
        elif val == "/":
            result = result / float(list_result[index+1])

        if val == "-" and result == 0:
            result = float(list_result[index-1]) - float(list_result[index+1]) +result
        elif val == "-":
            result = result - float(list_result[index+1])
    
            
    

    resulttext.config(text=str(result))
    list_result = []
    valeur ="" 
    texte_calculator.config(text=str(valeur))

        


def actionned_1():
    global valeur
    valeur = valeur + "1"
    texte_calculator.config(text=str(valeur))
def actionned_2():
    global valeur
    valeur = valeur + "2"
    texte_calculator.config(text=str(valeur))
def actionned_3():
    global valeur
    valeur = valeur + "3"
    texte_calculator.config(text=str(valeur))
def actionned_4():
    global valeur
    valeur = valeur + "4"
    texte_calculator.config(text=str(valeur))
def actionned_5():
    global valeur
    valeur = valeur + "5"
    texte_calculator.config(text=str(valeur))
def actionned_6():
    global valeur
    valeur = valeur + "6"
    texte_calculator.config(text=str(valeur))
def actionned_7():
    global valeur
    valeur = valeur + "7"
    texte_calculator.config(text=str(valeur))
def actionned_8():
    global valeur
    valeur = valeur + "8"
    texte_calculator.config(text=str(valeur))
def actionned_9():
    global valeur
    valeur = valeur + "9"
    texte_calculator.config(text=str(valeur))
def actionned_moins():
    global valeur
    global list_result
    list_result.append(valeur)
    list_result.append("-")
    valeur = ""
    texte_calculator.config(text=str(valeur))

def actionned_plus():
    global valeur
    global list_result
    list_result.append(valeur)
    list_result.append("+")
    valeur = ""
    texte_calculator.config(text=str(valeur))

def actionned_fois():
    global valeur
    global list_result
    list_result.append(valeur)
    list_result.append("x")
    valeur = ""
    texte_calculator.config(text=str(valeur))

def actionned_divi():
    global valeur
    global list_result
    list_result.append(valeur)
    list_result.append("/")
    valeur = ""
    texte_calculator.config(text=str(valeur))

def actionned_rei():
    global valeur
    global list_result
    global result
    result = 0
    valeur = ""
    list_result =[]
    texte_calculator.config(text=str(valeur))
    resulttext.config(text=str(result))


fenetre.canv = tk.Canvas(fenetre, bg="light gray", height=330, width=430)
fenetre.canv.place(x=0,y=160)
fenetre.canv = tk.Canvas(fenetre, bg="light blue", height=160, width=430)
fenetre.canv.place(x=0,y=0)
fenetre.canv = tk.Canvas(fenetre, bg="cyan", height=160, width=150)
fenetre.canv.place(x=435,y=0)
fenetre.canv.create_rectangle(2,2, 151, 161, outline='black', fill='')

texte_calculator = tk.Label(fenetre,text="" ,font=("bold", 40), bg='light blue', fg='black', highlightthickness=0, bd=0, highlightbackground='light blue')
texte_calculator.place(x=0,y=0)

resulttext = tk.Label(fenetre,text="" ,font=("bold", 40), bg='cyan', fg='black', highlightthickness=0, bd=0, highlightbackground='cyan')
resulttext.place(x=470,y=50)

btn0 = tk.Button(fenetre, text='0', width=10, height=2, bd='10', command=actionned_0)
btn0.place(x=20, y=420)
btnpoint = tk.Button(fenetre, text='.', width=10, height=2, bd='10', command=actionned_point)
btnpoint.place(x=120, y=420)
btnegal = tk.Button(fenetre, text='=', width=10, height=2, bd='10', command=actionned_egal)
btnegal.place(x=220, y=420)

btn1 = tk.Button(fenetre, text='1', width=10, height=2, bd='10', command=actionned_1)
btn1.place(x=20, y=360)
btn2 = tk.Button(fenetre, text='2', width=10, height=2, bd='10', command=actionned_2)
btn2.place(x=120, y=360)
btn3 = tk.Button(fenetre, text='3', width=10, height=2, bd='10', command=actionned_3)
btn3.place(x=220, y=360)


btn4 = tk.Button(fenetre, text='4', width=10, height=2, bd='10', command=actionned_4)
btn4.place(x=20, y=300)
btn5 = tk.Button(fenetre, text='5', width=10, height=2, bd='10', command=actionned_5)
btn5.place(x=120, y=300)
btn6 = tk.Button(fenetre, text='6', width=10, height=2, bd='10', command=actionned_6)
btn6.place(x=220, y=300)


btn7 = tk.Button(fenetre, text='7', width=10, height=2, bd='10', command=actionned_7)
btn7.place(x=20, y=240)
btn8 = tk.Button(fenetre, text='8', width=10, height=2, bd='10', command=actionned_8)
btn8.place(x=120, y=240)
btn9 = tk.Button(fenetre, text='9', width=10, height=2, bd='10', command=actionned_9)
btn9.place(x=220, y=240)
        
btnmoins = tk.Button(fenetre, text='-', width=10, height=2, bd='10', command=actionned_moins)
btnmoins.place(x=320, y=360)
btnplus = tk.Button(fenetre, text='+', width=10, height=2, bd='10', command=actionned_plus)
btnplus.place(x=320, y=420)
btnfois = tk.Button(fenetre, text='x', width=10, height=2, bd='10', command=actionned_fois)
btnfois.place(x=320, y=300)
btndivi = tk.Button(fenetre, text='/', width=10, height=2, bd='10', command=actionned_divi)
btndivi.place(x=320, y=240)
btnrei = tk.Button(fenetre, text='AC', width=10, height=2, bd='10', command=actionned_rei)
btnrei.place(x=320, y=180)

fenetre.mainloop()
