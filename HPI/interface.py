import tkinter as tk

root = tk.Tk()
root.title("My App")

label = tk.Label(root, text="KKSCTS")
label.pack(padx=128, pady=5)
canvas = tk.Canvas(root, width = 512, height = 256, bg="black")
canvas.pack()

button = tk.Button(root, text="Close", command=root.destroy)
button.pack()

canvas.create_line(25, 25, 999, 487, fill="green", width=5)

root.mainloop()

