import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from functools import lru_cache
import math

# Set the appearance mode and default color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class RecursionCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Recursion Calculator")
        self.geometry("800x600")
        self.minsize(800, 600)

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Title
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="Advanced Recursion Calculator",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Description
        self.desc_label = ctk.CTkLabel(
            self.main_frame,
            text="Calculate Factorial, Permutation, and Combination values\nwith optimized memory usage",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        self.desc_label.grid(row=1, column=0, padx=20, pady=(0, 20))

        # Operation selection
        self.operation_var = ctk.StringVar(value="Factorial")
        self.operation_frame = ctk.CTkFrame(self.main_frame)
        self.operation_frame.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="ew")
        self.operation_frame.grid_columnconfigure((0,1,2), weight=1)

        operations = ["Factorial", "Permutation", "Combination"]
        for i, op in enumerate(operations):
            btn = ctk.CTkButton(
                self.operation_frame,
                text=op,
                command=lambda x=op: self.change_operation(x),
                fg_color="transparent" if op != "Factorial" else None,
                border_width=2 if op != "Factorial" else 0
            )
            btn.grid(row=0, column=i, padx=10, pady=10, sticky="ew")
            setattr(self, f"{op.lower()}_btn", btn)

        # Input frame
        self.input_frame = ctk.CTkFrame(self.main_frame)
        self.input_frame.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="ew")
        self.input_frame.grid_columnconfigure((0,1), weight=1)

        # First number (n)
        self.n_label = ctk.CTkLabel(self.input_frame, text="n:", font=ctk.CTkFont(size=16))
        self.n_label.grid(row=0, column=0, padx=(20,10), pady=20, sticky="e")
        self.n_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Enter n")
        self.n_entry.grid(row=0, column=1, padx=(10,20), pady=20, sticky="ew")

        # Second number (r) - initially hidden
        self.r_label = ctk.CTkLabel(self.input_frame, text="r:", font=ctk.CTkFont(size=16))
        self.r_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Enter r")
        
        # Calculate button
        self.calc_button = ctk.CTkButton(
            self.main_frame,
            text="Calculate",
            command=self.calculate,
            height=40,
            font=ctk.CTkFont(size=16)
        )
        self.calc_button.grid(row=4, column=0, padx=20, pady=(0, 20))

        # Result
        self.result_frame = ctk.CTkFrame(self.main_frame)
        self.result_frame.grid(row=5, column=0, padx=20, pady=(0, 20), sticky="ew")
        self.result_frame.grid_columnconfigure(0, weight=1)

        self.result_label = ctk.CTkLabel(
            self.result_frame,
            text="Result will appear here",
            font=ctk.CTkFont(size=16),
            wraplength=700
        )
        self.result_label.grid(row=0, column=0, padx=20, pady=20)

    @lru_cache(maxsize=1000)
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n <= 1:
            return 1
        return n * self.factorial(n - 1)

    @lru_cache(maxsize=1000)
    def permutation(self, n, r):
        if r > n:
            raise ValueError("r cannot be greater than n")
        return self.factorial(n) // self.factorial(n - r)

    @lru_cache(maxsize=1000)
    def combination(self, n, r):
        if r > n:
            raise ValueError("r cannot be greater than n")
        return self.factorial(n) // (self.factorial(r) * self.factorial(n - r))

    def change_operation(self, operation):
        self.operation_var.set(operation)
        
        # Update button appearances
        for op in ["Factorial", "Permutation", "Combination"]:
            btn = getattr(self, f"{op.lower()}_btn")
            if op == operation:
                btn.configure(fg_color=["#3B8ED0", "#1F6AA5"], border_width=0)
            else:
                btn.configure(fg_color="transparent", border_width=2)

        # Show/hide r input
        if operation == "Factorial":
            self.r_label.grid_remove()
            self.r_entry.grid_remove()
        else:
            self.r_label.grid(row=1, column=0, padx=(20,10), pady=20, sticky="e")
            self.r_entry.grid(row=1, column=1, padx=(10,20), pady=20, sticky="ew")

    def calculate(self):
        try:
            n = int(self.n_entry.get())
            operation = self.operation_var.get()

            if n < 0:
                raise ValueError("n must be non-negative")

            if operation == "Factorial":
                result = self.factorial(n)
                formula = f"{n}!"
            else:
                r = int(self.r_entry.get())
                if r < 0:
                    raise ValueError("r must be non-negative")
                
                if operation == "Permutation":
                    result = self.permutation(n, r)
                    formula = f"P({n},{r})"
                else:  # Combination
                    result = self.combination(n, r)
                    formula = f"C({n},{r})"

            # Format large numbers with commas
            formatted_result = f"{result:,}"
            self.result_label.configure(
                text=f"{formula} = {formatted_result}",
                text_color="white"
            )

        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except OverflowError:
            messagebox.showerror("Error", "Result is too large to compute")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = RecursionCalculator()
    app.mainloop()
