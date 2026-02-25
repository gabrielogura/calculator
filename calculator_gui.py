import tkinter as tk
from calculator_logic import Calculator

#Config da janela
window = tk.Tk()
window.title('Calculadora')
window.geometry('300x400')

#Display
display = tk.Entry(window, font=('Arial', 20), justify='right')
display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)


current_operator = ''
num1 = None

def click_number(n):
    display.insert(tk.END, str(n))

def click_operator(op):
    global current_operator, num1
    num1 = float(display.get())
    current_operator = op
    display.delete(0, tk.END)

def calculate():
    global current_operator, num1
    try:
        num2 = float(display.get())
        calc = Calculator(num1, num2)

        if current_operator == '+':
            result = calc.add()
        elif current_operator == '-':
            result = calc.sub()
        elif current_operator == 'x':
            result = calc.mul()
        elif current_operator == '/':
            if num2 == 0:
                display.delete(0, tk.END)
                display.insert(tk.END, 'Erro: Divisão por 0')
                return
            result = calc.div()
        else:
            return

        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    
    except ValueError:
        display.delete(0, tk.END)
        display.insert(tk.END, 'Erro: Entrada inválida')

def clean():
    global current_operator, num1
    current_operator = ''
    num1 = None
    display.delete(0, tk.END)

#Botões
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text.isdigit():
        cmd = lambda x = text: click_number(x)
    elif text in '+-x/':
        cmd = lambda x = text: click_operator(x)
    elif text == '=':
        cmd = calculate
    else:
        cmd = clean

    tk.Button(window, text=text, font=('Arial', 18), command=cmd)\
              .grid(row=row, column=col, sticky='nsew', padx=2, pady=2)

for i in range(5):
    window.grid_rowconfigure(i,weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

#Inicia o Tkinter(essencial)
window.mainloop()