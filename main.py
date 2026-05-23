import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox, filedialog
window = tk.Tk()
window.title("Dynamic Chart Generator")
window.geometry("400x400")
df_global = [None]
x_var = tk.StringVar(window)
y_var = tk.StringVar(window)
def load_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if filepath:
        df_global[0] = pd.read_csv(filepath)
        columns = list(df_global[0].columns)
        x_var.set(columns[0])
        y_var.set(columns[1])
        x_menu["menu"].delete(0, "end")
        y_menu["menu"].delete(0, "end")
        for col in columns:
            x_menu["menu"].add_command(label=col, command=tk._setit(x_var, col))
            y_menu["menu"].add_command(label=col, command=tk._setit(y_var, col))
        messagebox.showinfo("Done", "File Loaded Successfully!")

    else:
        messagebox.showerror("Cancelled", "No File Selected!")
def generate_charts():
    if df_global[0] is None:
        messagebox.showerror("Error", "Please load a file first!")
        return
    df = df_global[0]
    x = x_var.get()
    y = y_var.get()
    fig, axes = plt.subplots(1, 1)
    axes.bar(df[x], df[y], color="blue")
    axes.set_title(f"{y} by {x}")
    axes.set_xlabel(x)
    axes.set_ylabel(y)
    axes.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.show()
    messagebox.showinfo("Done", "Chart Generated Successfully!")
tk.Label(window, text="Dynamic Chart Generator", font=("Arial", 14, "bold")).pack(pady=10)
tk.Button(window, text="Load CSV File", command=load_file).pack(pady=5)
tk.Label(window, text="X Axis:").pack()
x_menu = tk.OptionMenu(window, x_var, "")
x_menu.pack()
tk.Label(window, text="Y Axis:").pack()
y_menu = tk.OptionMenu(window, y_var, "")
y_menu.pack()
tk.Button(window, text="Generate Chart", command=generate_charts).pack(pady=10)
window.mainloop()
