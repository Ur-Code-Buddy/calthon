import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("330x380")
        self.master.configure(bg="#f0f0f0")
        self.master.resizable(False,False)

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.entry = tk.Entry(self.master, textvariable=self.result_var, font=("Serif", 20), bd=1, relief=tk.SOLID, bg="#add8e6")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        tk.Button(self.master, text=".", font=("Serif", 14), bg="#d3d3d3", bd=0, padx=20, pady=10, command=lambda: self.add_to_window(".")).grid(row=5, column=1, sticky="nsew")
        tk.Button(self.master, text="0", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("0")).grid(row=5, column=0, sticky="nsew")
        tk.Button(self.master, text="1", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("1")).grid(row=4, column=0, sticky="nsew")
        tk.Button(self.master, text="2", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("2")).grid(row=4, column=1, sticky="nsew")
        tk.Button(self.master, text="3", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("3")).grid(row=4, column=2, sticky="nsew")
        tk.Button(self.master, text="4", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("4")).grid(row=3, column=0, sticky="nsew")
        tk.Button(self.master, text="5", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("5")).grid(row=3, column=1, sticky="nsew")
        tk.Button(self.master, text="6", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("6")).grid(row=3, column=2, sticky="nsew")
        tk.Button(self.master, text="7", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("7")).grid(row=2, column=0, sticky="nsew")
        tk.Button(self.master, text="8", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("8")).grid(row=2, column=1, sticky="nsew")
        tk.Button(self.master, text="9", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("9")).grid(row=2, column=2, sticky="nsew")

        tk.Button(self.master, text="AC", font=("Serif", 14), bg="#ffb6c1", bd=1, padx=20, pady=10, command=self.clear_window).grid(row=1, column=0, sticky="nsew")
        tk.Button(self.master, text="(", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("(")).grid(row=1, column=1, sticky="nsew")
        tk.Button(self.master, text=")", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window(")")).grid(row=1, column=2, sticky="nsew")

        tk.Button(self.master, text="*", font=("Serif", 14), bg="#add8e6", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("*")).grid(row=2, column=3, sticky="nsew")
        tk.Button(self.master, text="/", font=("Serif", 14), bg="#add8e6", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("/")).grid(row=1, column=3, sticky="nsew")
        tk.Button(self.master, text="-", font=("Serif", 14), bg="#add8e6", bd=0, padx=20, pady=10, command=lambda: self.add_to_window("-")).grid(row=3, column=3, sticky="nsew")
        tk.Button(self.master, text="+", font=("Serif", 14), bg="#add8e6", bd=0, padx=20, pady=10, command=lambda: self.add_to_window("+")).grid(row=4, column=3, sticky="nsew")

        tk.Button(self.master, text="=", font=("Serif", 14), bg="#add8e6", bd=1, padx=20, pady=10, command=self.calculate_result).grid(row=5, column=3, sticky="nsew")
        tk.Button(self.master, text="←", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=self.backspace).grid(row=5, column=2, sticky="nsew")
        tk.Button(self.master, text="√", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("√")).grid(row=6, column=0, sticky="nsew")
        tk.Button(self.master, text="x²", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("**2")).grid(row=6, column=1, sticky="nsew")
    
    
    def add_to_window(self, value): #? pushes the char to the entry box
        current_text = self.result_var.get()
        self.result_var.set(current_text + value)

    
    def clear_window(self):
        self.result_var.set("")

    #TODO: COMPLETE THE FUNCTIONS TOO
    def calculate_result(self):
        pass

    def backspace(self):
        pass

def main():
    root = tk.Tk()
    Calculator(root)
    root.mainloop()


main()
