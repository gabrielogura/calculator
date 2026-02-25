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

should_clear = False

def click_number(n):
    global should_clear
    if should_clear:
        display.delete(0, tk.END)
        should_clear = False
    display.insert(tk.END, str(n))

def click_operator(op):
    global current_operator, num1

    text = display.get()

    if text and text[-1] in '+-x/':
        display.delete(len(text)-1, tk.END)
        display.insert(tk.END, f'{op}')
        current_operator = op
        return
    
    if not text:
        return

    try:
        num1 = float(text)
        current_operator = op
        display.insert(tk.END, f'{op}')
    except ValueError:
        pass


def calculate():
    global current_operator, num1, should_clear

    try:
        expression = display.get()

        if current_operator == '':
            return

        parts = expression.split(current_operator)

        if len(parts) != 2:
            return

        num2 = float(parts[1])

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
                should_clear = True
                return
            result = calc.div()

        if result.is_integer():
            result = int(result)

        display.delete(0, tk.END)
        display.insert(tk.END, str(result))

        current_operator = ''
        should_clear = True

    except ValueError:
        display.delete(0, tk.END)
        display.insert(tk.END, 'Erro')
        should_clear = True

def clean():
    global current_operator, num1
    current_operator = ''
    num1 = None
    should_clear = False
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