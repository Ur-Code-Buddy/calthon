import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("285x420")
        self.master.configure(bg="#ffffff")
        self.master.resizable(False,False)

        self.result_var = tk.StringVar()#primary layout
        self.result_var.set("")
        self.current_result = tk.StringVar() #secondary layout
        self.current_result.set("")

        validate_command = master.register(self.validate_input)
        # self.entry = tk.Entry(self.master, textvariable=self.result_var, font=("Serif", 20), bd=1, relief=tk.SOLID,bg="#add8e6", validate="key", validatecommand=(validate_command, '%P'))
        # self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
        self.result_label = tk.Label(self.master, textvariable=self.result_var, font=("Serif", 24), bd=1.5, relief=tk.SOLID, bg="#add8e6", anchor="e")
        self.result_label.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=(5, 2)) 

        self.current_result_label = tk.Label(self.master, textvariable=self.current_result, font=("Serif", 16), bd=0.5, relief=tk.SOLID, bg="#6fcbfc", anchor="e")
        self.current_result_label.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=10, pady=(2, 5)) 

        tk.Button(self.master, text=".", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window(".")).grid(row=7, column=1, sticky="nsew")
        tk.Button(self.master, text="0", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("0")).grid(row=7, column=0, sticky="nsew")
        tk.Button(self.master, text="1", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("1")).grid(row=6, column=0, sticky="nsew")
        tk.Button(self.master, text="2", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("2")).grid(row=6, column=1, sticky="nsew")
        tk.Button(self.master, text="3", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("3")).grid(row=6, column=2, sticky="nsew")
        tk.Button(self.master, text="4", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("4")).grid(row=5, column=0, sticky="nsew")
        tk.Button(self.master, text="5", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("5")).grid(row=5, column=1, sticky="nsew")
        tk.Button(self.master, text="6", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("6")).grid(row=5, column=2, sticky="nsew")
        tk.Button(self.master, text="7", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("7")).grid(row=4, column=0, sticky="nsew")
        tk.Button(self.master, text="8", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("8")).grid(row=4, column=1, sticky="nsew")
        tk.Button(self.master, text="9", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("9")).grid(row=4, column=2, sticky="nsew")

        tk.Button(self.master, text="AC", font=("Serif", 14), bg="#ffb6c1", bd=1, padx=20, pady=10, command=self.clear_window).grid(row=2, column=0, sticky="nsew")
        tk.Button(self.master, text="(", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("(")).grid(row=2, column=1, sticky="nsew")
        tk.Button(self.master, text=")", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window(")")).grid(row=2, column=2, sticky="nsew")
        tk.Button(self.master, text="√", font=("Serif", 14), bg="#add8e6", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("√")).grid(row=2, column=3, sticky="nsew")
        
        tk.Button(self.master, text="*", font=("Serif", 14), bg="#add8e6", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("*")).grid(row=4, column=3, sticky="nsew")
        tk.Button(self.master, text="/", font=("Serif", 14), bg="#add8e6", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("/")).grid(row=3, column=3, sticky="nsew")
        tk.Button(self.master, text="-", font=("Serif", 14), bg="#add8e6", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("-")).grid(row=5, column=3, sticky="nsew")
        tk.Button(self.master, text="+", font=("Serif", 14), bg="#add8e6", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("+")).grid(row=6, column=3, sticky="nsew")

        tk.Button(self.master, text="=", font=("Serif", 14), bg="#7dcae3", bd=1, padx=20, pady=10, command=self.evaluate_and_set).grid(row=7, column=3, sticky="nsew")
        tk.Button(self.master, text="←", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=self.backspace).grid(row=7, column=2, sticky="nsew")
        tk.Button(self.master, text="π", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("π")).grid(row=3, column=0, sticky="nsew")
        tk.Button(self.master, text="x²", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("^2")).grid(row=3, column=1, sticky="nsew")
        tk.Button(self.master, text="^", font=("Serif", 14), bg="#d3d3d3", bd=1, padx=20, pady=10, command=lambda: self.add_to_window("^")).grid(row=3, column=2, sticky="nsew")


    def create_button_image(self, image_path, command, bg_color):  #this is for the PIL library when we were supposed to use images, since that changed, we can ignore this for now. 
        width = 40
        height = 40
        additional_path = "GitImage"
        load_image = Image.open(additional_path + "/" + image_path)
        load_image = load_image.resize((width, height))
        render = ImageTk.PhotoImage(load_image)
        button = tk.Button(self.master, image=render, bd=0, bg=bg_color, command=command)
        button.image = render
        return button
    

    def add_to_window(self, value):
        """
        Appends characters or operators to the expression displayed in a GUI window.
        
        Parameters:
            value (str): The character or operator to be added.
            
        How it works:
            - Retrieves the current expression from the GUI window.
            - If the value is '√', wraps the current expression with square root brackets.
            - If the value is a digit:
                - If the last character is a closing parenthesis, appends a multiplication symbol before adding the digit. ) -> )*
                - Otherwise, directly appends the digit.
            - For other characters or operators, directly appends them to the current expression.
        """
        current_text = self.result_var.get()
        if value == "√":
            self.result_var.set("√(" + current_text + ")")
        elif value.isdigit():
            if current_text and current_text[-1] == ")":
                self.result_var.set(current_text + "*" + value)
            else:
                self.result_var.set(current_text + value)
        else:
            self.result_var.set(current_text + value)

        currentResult = self.calculate_result()
        self.current_result.set(currentResult)

    def clear_window(self):  #clears the screen to ""
        self.result_var.set("")
        self.current_result.set("")

    def calculate_result(self):
        """
        Evaluates the mathematical expression in the GUI window and updates the result accordingly.
        
        How it works:
            - Modifies the expression to ensure proper multiplication syntax.
            - Replaces the square root symbol with the appropriate function call.
            - Checks for division by zero and handles potential errors during evaluation.
            - Updates the GUI window with the calculated result or displays an error message.
        """
        expression = self.result_var.get()
        operators = set("(+-*/√π")
        pi_operators = set(")0987654321")
        modified_expression = ""

        for i, char in enumerate(expression):
            #! Try equation: (8/99)*5(5**6)
            if char == "(" and i != 0 and (expression[i - 1] not in operators):
                modified_expression += "*("
            elif char == "π" and i != 0 and (expression[i-1] in pi_operators):
                modified_expression += "*3.141592"
            else:
                modified_expression += char

            
        if expression:
            modified_expression = modified_expression.replace("√", "math.sqrt").replace("^","**").replace("π","3.141592")
            # Check for division by zero
            if "/0" in modified_expression:
                raise ZeroDivisionError #if divided by zero throw an error
            print(modified_expression)
            result = eval(modified_expression, {}, {"math": math})
            result = round(result, 5)
            # self.result_var.set(result)
            return result
        # Replaces the square root symbol with the appropriate function call from the 'math' module.
        # Evaluates the modified expression using Python's 'eval' function, with 'math' module available for use.
        # Rounds the result to 5 decimal places for precision then sets the result in the GUI window for display.

        else:
            result = None

    def evaluate_and_set(self):
        try:
            self.result_var.set(self.calculate_result() )
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero") #if its divided by zero
        except Exception as e:
            messagebox.showerror("Error", str(e))

        self.current_result.set("") #updating the 2nd layout to ""
        

    def validate_input(self, new_text): #This goes through the char, checks if its in the list, if its not it just ignores it. 
        allowed_chars = set("0123456789+-*/().")
        return all(char in allowed_chars for char in new_text)

    def backspace(self):
        current_text = self.result_var.get()
        if current_text:
            new_text = current_text[:-1]  # Creates a new string excluding the last character 
            self.result_var.set(new_text) # Updates the screen to the new text
    


def main():
    root = tk.Tk()
    cal = Calculator(root)
    root.mainloop()


main()
