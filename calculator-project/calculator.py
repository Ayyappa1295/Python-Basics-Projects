
import tkinter as tk
from tkinter import messagebox
import ast
import operator

# Calculator window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#171717")

expression = tk.StringVar()

# Safe mathematical operations
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def safe_calculate(node):
    if isinstance(node, ast.Expression):
        return safe_calculate(node.body)

    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in operators:
        left = safe_calculate(node.left)
        right = safe_calculate(node.right)

        if isinstance(node.op, ast.Div) and right == 0:
            raise ZeroDivisionError

        return operators[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp) and type(node.op) in operators:
        return operators[type(node.op)](safe_calculate(node.operand))

    raise ValueError("Invalid expression")

def press(value):
    current = expression.get()

    if value == "C":
        expression.set("")
    elif value == "⌫":
        expression.set(current[:-1])
    elif value == "=":
        try:
            if not current.strip():
                return

            tree = ast.parse(current, mode="eval")
            result = safe_calculate(tree)

            if isinstance(result, float):
                result = round(result, 10)

            expression.set(str(result))

        except ZeroDivisionError:
            expression.set("Cannot divide by zero")
        except Exception:
            expression.set("Error")
    elif value == "%":
        try:
            if current.strip():
                tree = ast.parse(current, mode="eval")
                result = safe_calculate(tree)
                expression.set(str(result / 100))
        except Exception:
            expression.set("Error")
    else:
        if current in ("Error", "Cannot divide by zero"):
            expression.set("")
        expression.set(expression.get() + value)

def keyboard_input(event):
    if event.char in "0123456789.+-*/%()":
        press(event.char)
    elif event.keysym == "Return":
        press("=")
    elif event.keysym == "BackSpace":
        press("⌫")
    elif event.keysym == "Escape":
        press("C")

root.bind("<Key>", keyboard_input)

# Display
display = tk.Entry(
    root,
    textvariable=expression,
    font=("Arial", 24),
    bg="#252525",
    fg="white",
    insertbackground="white",
    bd=0,
    justify="right"
)
display.pack(fill="x", padx=15, pady=(25, 20), ipady=18)

# Buttons layout
buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["00", "0", ".", "="],
]

button_frame = tk.Frame(root, bg="#171717")
button_frame.pack(expand=True, fill="both", padx=10, pady=5)

for row_index, row in enumerate(buttons):
    for col_index, value in enumerate(row):

        if value == "=":
            color = "#16A085"
        elif value in ("C", "⌫", "%", "/", "*", "-", "+"):
            color = "#343434"
        else:
            color = "#252525"

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 17, "bold"),
            bg=color,
            fg="white",
            activebackground="#555555",
            activeforeground="white",
            bd=0,
            cursor="hand2",
            command=lambda v=value: press(v)
        )

        button.grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=4,
            pady=4
        )

for i in range(5):
    button_frame.rowconfigure(i, weight=1)

for i in range(4):
    button_frame.columnconfigure(i, weight=1)

# Start application
root.mainloop()
