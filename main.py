from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("calculadora")
root.resizable(0, 0)

# Configuración pantalla de salida
pantalla = Entry(root, width=23, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=0, pady=0)


def click(valor):
    click1 = pantalla.get()
    pantalla.delete(0, "end")
    pantalla.insert(0, str(click1) + str(valor))


def suma():
    global num1
    global operador
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, "end")
    operador = "+"


def resta():
    global num1
    global operador
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, "end")
    operador = "-"


def multiplicacion():
    global num1
    global operador
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, "end")
    operador = "*"


def division():
    global num1
    global operador
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, "end")
    operador = "/"


def punto():
    num1 = pantalla.get()
    pantalla.delete(0, "end")
    pantalla.insert(0, num1 + ".")


def igual():
    global num2
    num2 = pantalla.get()
    num2 = float(num2)
    pantalla.delete(0, "end")
    if operador == "+":
        pantalla.insert(0, num1 + num2)
    if operador == "-":
        pantalla.insert(0, num1 - num2)
    if operador == "*":
        pantalla.insert(0, num1 * num2)
    if operador == "/":
        pantalla.insert(0, num1 / num2)


# Configuración botones
Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
       command=lambda: click(1)).grid(row=1, column=0,
                                      padx=1, pady=1)
Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
       command=lambda: click(2)).grid(row=1, column=1,
                                      padx=1, pady=1)
Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
       command=lambda: click(3)).grid(row=1, column=2,
                                      padx=1, pady=1)
Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
       command=lambda: click(4)).grid(row=2, column=0,
                                      padx=1, pady=1)
Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
       command=lambda: click(5)).grid(row=2, column=1,
                                      padx=1, pady=1)
Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
       command=lambda: click(6)).grid(row=2, column=2,
                                      padx=1, pady=1)
Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
       command=lambda: click(7)).grid(row=3, column=0,
                                      padx=1, pady=1)
Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
       command=lambda: click(8)).grid(row=3, column=1,
                                      padx=1, pady=1)
Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
       command=lambda: click(9)).grid(row=3, column=2,
                                      padx=1, pady=1)

# Operadores

Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2",
       command=igual).grid(row=4, column=0,
                           columnspan=2,
                           padx=1, pady=1)

Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0,
       command=punto).grid(row=4,
                           column=2,
                           padx=1,
                           pady=1)

Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",
       command=suma).grid(row=1,
                          column=3,
                          padx=1,
                          pady=1)

Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",
       command=resta).grid(row=2,
                           column=3,
                           padx=1,
                           pady=1)

Button(root, text="*", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",
       command=multiplicacion).grid(row=3,
                                    column=3,
                                    padx=1,
                                    pady=1)

Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",
       command=division).grid(row=4,
                              column=3,
                              padx=1,
                              pady=1)

root.mainloop()
