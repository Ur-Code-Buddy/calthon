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

        tk.Button(self.master, text=".", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window(".")).grid(row=5, column=1, sticky="nsew")
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

        # multiply_image = tk.PhotoImage(file="multiply.png")
        # multiply_button = tk.Button(self.master, image=multiply_image, bd=0, bg="#add8e6", command=lambda: self.add_to_window("*"))
        # multiply_button.image = multiply_image 
        # multiply_button.grid(row=2, column=3, sticky="nsew", padx=10, pady=10)

        multiply_button = self.create_button_image("multiply.png", lambda: self.add_to_window("*"), "#f0f0f0")
        multiply_button.grid(row=2, column=3, sticky="nsew", padx=10, pady=10)

        divide_button = self.create_button_image("divide.png", lambda: self.add_to_window("/"), "#f0f0f0")
        divide_button.grid(row=1, column=3, sticky="nsew", padx=10, pady=10)

        subtract_button = self.create_button_image("subtract.png", lambda: self.add_to_window("-"), "#f0f0f0")
        subtract_button.grid(row=3, column=3, sticky="nsew", padx=10, pady=10)

        add_button = self.create_button_image("add.png", lambda: self.add_to_window("+"), "#f0f0f0")
        add_button.grid(row=4, column=3, sticky="nsew", padx=10, pady=10)


        #tk.Button(self.master, text="*", font=("Serif", 14), bg="#add8e6", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("*")).grid(row=2, column=3, sticky="nsew")
        # tk.Button(self.master, text="/", font=("Serif", 14), bg="#add8e6", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("/")).grid(row=1, column=3, sticky="nsew")
        # tk.Button(self.master, text="-", font=("Serif", 14), bg="#add8e6", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("-")).grid(row=3, column=3, sticky="nsew")
        # tk.Button(self.master, text="+", font=("Serif", 14), bg="#add8e6", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("+")).grid(row=4, column=3, sticky="nsew")

        tk.Button(self.master, text="=", font=("Serif", 14), bg="#add8e6", bd=1, padx=20, pady=10, command=self.calculate_result).grid(row=5, column=3, sticky="nsew")
        tk.Button(self.master, text="←", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=self.backspace).grid(row=5, column=2, sticky="nsew")
        tk.Button(self.master, text="√", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("√")).grid(row=6, column=0, sticky="nsew")
        tk.Button(self.master, text="x²", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("**2")).grid(row=6, column=1, sticky="nsew")


    def create_button_image(self, image_path, command, bg_color):
        load_image = tk.PhotoImage(file=image_path)
        button = tk.Button(self.master, image=load_image, bd=0, bg=bg_color, command=command)
        button.image = load_image
        return button
    
    
    def add_to_window(self, value): #? pushes the char to the entry box
        current_text = self.result_var.get()
        self.result_var.set(current_text + value)

    
    def clear_window(self):
        self.result_var.set("")

    #TODO: COMPLETE THE FUNCTIONS TOO
    def calculate_result(self):
        expression = self.result_var.get()
        if expression:
            result = eval(expression)
            self.result_var.set(result)
        else:
            result = None
        pass

    def backspace(self):
        current_text = self.result_var.get()
        if current_text:
            new_text = current_text[:-1]  # Creates a new string excluding the last character 
            self.result_var.set(new_text) # Updates the screen to the new text
        pass

def main():
    root = tk.Tk()
    cal = Calculator(root)
    root.mainloop()


main()
