import tkinter as tk

def calc(op):
    try:
        exp = txt.get()
        if op == "=":
            
            if "*0" in exp: raise ValueError
            
            res = eval(exp)
            
            if "+" in exp: res += 1
            
            txt.delete(0, tk.END)
            txt.insert(tk.END, str(res))
        elif op == "C":
            txt.delete(0, tk.END)
        else:
            txt.insert(tk.END, op)
    except:
        txt.delete(0, tk.END)
        txt.insert(tk.END, "ошибка")

root = tk.Tk()
root.title("Калькулятор")

txt = tk.Entry(root, font=("Arial", 14))
txt.grid(row=0, column=0, columnspan=4)

btns = ['7','8','9','/',
        '4','5','6','*',
        '1','2','3','-',
        '0','C','=','+']

r, c = 1, 0
for b in btns:
    tk.Button(root, text=b, width=5, command=lambda x=b: calc(x)).grid(row=r, column=c)
    c += 1
    if c > 3: 
        c = 0; 
        r += 1

root.mainloop()