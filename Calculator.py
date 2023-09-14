import tkinter as tk


def click(event):
    text = event.widget.cget("text")

    if text == "=":

        try:

            result = str(eval(screen.get()))

            screen.set(result)

        except Exception as e:

            screen.set("Error")

    elif text == "C":

        screen.set("")

    else:

        screen.set(screen.get() + text)


root = tk.Tk()

root.geometry("400x600")

root.title("Calculator")

screen = tk.StringVar()

entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")

entry.pack(fill=tk.X, ipadx=8, padx=10, pady=10)

button_frame = tk.Frame(root)

button_frame.pack()

button_text = [

    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),

    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),

    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),

    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),

    ("=", 5, 0)

]

for (btn_text, i, j) in button_text:
    btn = tk.Button(button_frame, text=btn_text, font="lucida 20 bold", padx=20, pady=20)

    btn.grid(row=i, column=j)

    btn.bind("<Button-1>", click)

root.mainloop()