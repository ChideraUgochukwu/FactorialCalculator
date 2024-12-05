import tkinter as tk
from tkinter import ttk, messagebox
import math
from decimal import Decimal
from typing import Callable
import ttkbootstrap as ttk

class CalculatorGUI:
    def __init__(self):
        self.window = ttk.Window(themename="darkly")
        self.window.title("Advanced Calculator")
        self.window.geometry("800x600")
        self.window.resizable(False, False)

        # Main frame
        self.main_frame = ttk.Frame(self.window, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(
            self.main_frame,
            text="Advanced Mathematical Calculator",
            font=("Helvetica", 24, "bold"),
            bootstyle="inverse-primary"
        )
        title_label.pack(pady=20)

        # Operation selection
        self.operation_frame = ttk.LabelFrame(
            self.main_frame,
            text="Select Operation",
            padding="10"
        )
        self.operation_frame.pack(fill=tk.X, padx=20, pady=10)

        self.operation_var = tk.StringVar(value="factorial")
        operations = [
            ("Factorial (n!)", "factorial"),
            ("Permutation (nPr)", "permutation"),
            ("Combination (nCr)", "combination")
        ]

        for text, value in operations:
            ttk.Radiobutton(
                self.operation_frame,
                text=text,
                value=value,
                variable=self.operation_var,
                command=self.update_input_fields,
                bootstyle="primary-toolbutton"
            ).pack(side=tk.LEFT, padx=10, expand=True)

        # Input frame
        self.input_frame = ttk.LabelFrame(
            self.main_frame,
            text="Input Values",
            padding="10"
        )
        self.input_frame.pack(fill=tk.X, padx=20, pady=10)

        # First number (n)
        self.n_frame = ttk.Frame(self.input_frame)
        self.n_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(
            self.n_frame,
            text="n = ",
            font=("Helvetica", 12)
        ).pack(side=tk.LEFT, padx=5)
        
        self.n_entry = ttk.Entry(
            self.n_frame,
            width=20,
            font=("Helvetica", 12)
        )
        self.n_entry.pack(side=tk.LEFT, padx=5)

        # Second number (r)
        self.r_frame = ttk.Frame(self.input_frame)
        self.r_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(
            self.r_frame,
            text="r = ",
            font=("Helvetica", 12)
        ).pack(side=tk.LEFT, padx=5)
        
        self.r_entry = ttk.Entry(
            self.r_frame,
            width=20,
            font=("Helvetica", 12)
        )
        self.r_entry.pack(side=tk.LEFT, padx=5)

        # Calculate button
        self.calc_button = ttk.Button(
            self.main_frame,
            text="Calculate",
            command=self.calculate,
            bootstyle="success-outline",
            width=20
        )
        self.calc_button.pack(pady=20)

        # Result frame
        self.result_frame = ttk.LabelFrame(
            self.main_frame,
            text="Result",
            padding="10"
        )
        self.result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.result_text = tk.Text(
            self.result_frame,
            height=8,
            width=50,
            font=("Courier", 12),
            wrap=tk.WORD,
            bg="#2b2b2b",
            fg="#ffffff"
        )
        self.result_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Initialize the UI
        self.update_input_fields()
        
    def update_input_fields(self):
        """Update input fields based on selected operation"""
        operation = self.operation_var.get()
        if operation == "factorial":
            self.r_frame.pack_forget()
        else:
            self.r_frame.pack(fill=tk.X, pady=5)

    def factorial(self, n: int) -> int:
        """Calculate factorial iteratively"""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def permutation(self, n: int, r: int) -> int:
        """Calculate permutation iteratively"""
        if n < 0 or r < 0:
            raise ValueError("Permutation is not defined for negative numbers")
        if r > n:
            raise ValueError("r cannot be greater than n in permutation")
        result = 1
        for i in range(n, n - r, -1):
            result *= i
        return result

    def combination(self, n: int, r: int) -> int:
        """Calculate combination iteratively"""
        if n < 0 or r < 0:
            raise ValueError("Combination is not defined for negative numbers")
        if r > n:
            raise ValueError("r cannot be greater than n in combination")
        r = min(r, n - r)  # Use the smaller value for efficiency
        num = 1
        den = 1
        for i in range(r):
            num *= (n - i)
            den *= (i + 1)
        return num // den

    def format_large_number(self, num: int) -> str:
        """Format large numbers with scientific notation if needed"""
        if num < 1000000:
            return format(num, ',')
        return f"{num:.2e}"

    def calculate(self):
        """Perform the calculation based on selected operation"""
        try:
            operation = self.operation_var.get()
            n = int(self.n_entry.get())
            
            if operation == "factorial":
                result = self.factorial(n)
                operation_text = f"{n}!"
            else:
                r = int(self.r_entry.get())
                if operation == "permutation":
                    result = self.permutation(n, r)
                    operation_text = f"{n}P{r}"
                else:  # combination
                    result = self.combination(n, r)
                    operation_text = f"{n}C{r}"

            # Display result
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, 
                f"Operation: {operation_text}\n"
                f"Result: {self.format_large_number(result)}\n\n"
                f"Scientific Notation: {result:e}\n"
                f"Decimal Form: {result:,}")

        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def run(self):
        """Start the application"""
        self.window.mainloop()

if __name__ == "__main__":
    app = CalculatorGUI()
    app.run()
