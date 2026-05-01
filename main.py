import tkinter as tk

window = tk.Tk()
window.title("AsserCalcul")
window.resizable(False, False)
window.config(bg="grey")
for i in range(4):
    window.columnconfigure(i, weight=1)

icon = tk.PhotoImage(file="icon.png")

window.iconphoto(True, icon)

entry = tk.Entry(window, font=("Arial", 20), width=10, justify="right", highlightthickness=0, relief="flat", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4, padx=2, pady=2, sticky="ew")

imgplus = tk.PhotoImage(file="imgplus.png")
imgminus = tk.PhotoImage(file="imgminus.png")
imgmulti = tk.PhotoImage(file="imgmulti.png")
imgdivi = tk.PhotoImage(file="imgdivi.png")
imgdel = tk.PhotoImage(file="imgdel.png")
imgc = tk.PhotoImage(file="imgc.png")
imgdot = tk.PhotoImage(file="imgdot.png")
imgequa = tk.PhotoImage(file="imgequa.png")
img0 = tk.PhotoImage(file="img0.png")
img1 = tk.PhotoImage(file="img1.png")
img2 = tk.PhotoImage(file="img2.png")
img3 = tk.PhotoImage(file="img3.png")
img4 = tk.PhotoImage(file="img4.png")
img5 = tk.PhotoImage(file="img5.png")
img6 = tk.PhotoImage(file="img6.png")
img7 = tk.PhotoImage(file="img7.png")
img8 = tk.PhotoImage(file="img8.png")
img9 = tk.PhotoImage(file="img9.png")

def press(num):
    if entry.get() == "Error":
        entry.delete(0, tk.END)
    elif entry.get() == "Ellipsis":
        entry.delete(0, tk.END)
    entry.insert(tk.END, str(num))

def clear():
   entry.delete(0, tk.END)

def result():
 try:
  result = eval(entry.get())
  entry.delete(0, tk.END)
  entry.insert(tk.END, str(result))
 except:
   entry.delete(0, tk.END)
   entry.insert(0, "Error")

def baks():
    text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, text[:-1])

btnplus = tk.Button(window, text="+", relief="flat", highlightthickness=0, image=imgplus, borderwidth=0, command=lambda: press('+'))
btnplus.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")

btn1 = tk.Button(window, text="1", relief="flat", highlightthickness=0, borderwidth=0, image=img1, command=lambda: press(1))
btn1.grid(row=1, column=1, padx=2, pady=2, sticky="nsew")

btn2 = tk.Button(window, text="2", relief="flat", highlightthickness=0, borderwidth=0, image=img2, command=lambda: press(2))
btn2.grid(row=1, column=2, padx=2, pady=2, sticky="nsew")

btn3 = tk.Button(window, text="3", relief="flat", highlightthickness=0, borderwidth=0, image=img3, command=lambda: press(3))
btn3.grid(row=1, column=3, padx=2, pady=2, sticky="nsew")

btnminus = tk.Button(window, text="-", relief="flat", highlightthickness=0, image=imgminus, borderwidth=0, command=lambda: press("-"))
btnminus.grid(row=2, column=0, padx=2, pady=2, sticky="nsew")

btn4 = tk.Button(window, text="4", relief="flat", highlightthickness=0, borderwidth=0, image=img4, command=lambda: press(4))
btn4.grid(row=2, column=1, padx=2, pady=2, sticky="nsew")

btn5 = tk.Button(window, text="5", relief="flat", highlightthickness=0, borderwidth=0, image=img5, command=lambda: press(5))
btn5.grid(row=2, column=2, padx=2, pady=2, sticky="nsew")

btn6 = tk.Button(window, text="6", relief="flat", highlightthickness=0, borderwidth=0, image=img6, command=lambda: press(6))
btn6.grid(row=2, column=3, padx=2, pady=2, sticky="nsew")

btnmulti = tk.Button(window, text="*", relief="flat", highlightthickness=0, borderwidth=0, image=imgmulti, command=lambda: press("*"))
btnmulti.grid(row=3, column=0, padx=2, pady=2, sticky="nsew")

btn7 = tk.Button(window, text="7", relief="flat", highlightthickness=0, borderwidth=0, image=img7, command=lambda: press(7))
btn7.grid(row=3, column=1, padx=2, pady=2, sticky="nsew")

btn8 = tk.Button(window, text="8", relief="flat", highlightthickness=0, borderwidth=0, image=img8, command=lambda: press(8))
btn8.grid(row=3, column=2, padx=2, pady=2, sticky="nsew")

btn9 = tk.Button(window, text="9", relief="flat", highlightthickness=0, borderwidth=0, image=img9, command=lambda: press(9))
btn9.grid(row=3, column=3, padx=2, pady=2, sticky="nsew")

btndivi = tk.Button(window, text="/", relief="flat", highlightthickness=0, image=imgdivi, borderwidth=0, command=lambda: press("/"))
btndivi.grid(row=4, column=0, padx=2, pady=2, sticky="nsew")

btneq = tk.Button(window, text="=", relief="flat", highlightthickness=0, image=imgequa, borderwidth=0, command=result)
btneq.grid(row=5, column=1, padx=2, pady=2, sticky="nsew")

btn0 = tk.Button(window, text="0", relief="flat", highlightthickness=0, borderwidth=0, image=img0, command=lambda: press(0))
btn0.grid(row=4, column=2, padx=2, pady=2, sticky="nsew")

btndel = tk.Button(window, text="x", relief="flat", highlightthickness=0, image=imgdel, borderwidth=0, command=baks)
btndel.grid(row=4, column=3, padx=2, pady=2, sticky="nsew")

btnc = tk.Button(window, text="C", relief="flat", highlightthickness=0, image=imgc, borderwidth=0, command=clear)
btnc.grid(row=5, column=0, padx=2, pady=2, sticky="nsew")

btndot = tk.Button(window, text=".", relief="flat", highlightthickness=0, image=imgdot, borderwidth=0, command=lambda: press("."))
btndot.grid(row=4, column=1, padx=2, pady=2, sticky="nsew")

window.mainloop()
