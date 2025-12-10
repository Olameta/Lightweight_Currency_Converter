# ------------------- Import Libraries -------------------
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import json
import os

# ------------------- File for Storing Rates -------------------
RATES_FILE = "exchange_rates.json"

# ------------------- Load Exchange Rates -------------------
def load_rates():
    """Load rates from file if exists, otherwise use defaults"""
    if os.path.exists(RATES_FILE):
        try:
            with open(RATES_FILE, "r") as f:
                return json.load(f)
        except Exception:
            # Fallback to defaults if file is corrupt
            messagebox.showerror("Error", "Could not load existing rates file. Using defaults.")
            return get_default_rates()
    else:
        # Default rates if file doesn't exist
        return get_default_rates()

def get_default_rates():
    """Provides a baseline set of rates against USD"""
    return {
        "USD": 1.0,
        "EUR": 0.93,
        "GBP": 0.80,
        "NGN": 1530.00,
        "JPY": 149.00
    }

# ------------------- Save Exchange Rates -------------------
def save_rates():
    """Save current rates to file"""
    try:
        with open(RATES_FILE, "w") as f:
            json.dump(exchange_rates, f, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save rates: {e}")

# ------------------- Load rates into dictionary -------------------
exchange_rates = load_rates()

# ------------------- Conversion Function -------------------
def convert_currency():
    """Perform currency conversion based on user input"""
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_cb.get()
        to_currency = to_currency_cb.get()

        if from_currency not in exchange_rates or to_currency not in exchange_rates:
             messagebox.showerror("Error", "Invalid currency selected.")
             return

        # Convert: From → USD → To
        # 1. Convert source amount to USD equivalent
        amount_in_usd = amount / exchange_rates[from_currency]
        # 2. Convert USD equivalent to target currency
        converted_amount = amount_in_usd * exchange_rates[to_currency]

        result_var.set(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

    except ValueError:
        messagebox.showerror("Error", "Invalid amount entered. Please enter a number.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# ------------------- Swap Function -------------------
def swap_currencies():
    """Swaps the selected 'From' and 'To' currencies"""
    from_val = from_currency_cb.get()
    to_val = to_currency_cb.get()
    from_currency_cb.set(to_val)
    to_currency_cb.set(from_val)

# ------------------- Update Rate Function -------------------
def update_rate():
    """Allows user to update the exchange rate for an existing currency"""
    currency_to_update = simpledialog.askstring("Update Rate", "Enter the currency code to update (e.g., NGN):")
    if currency_to_update in exchange_rates:
        new_rate = simpledialog.askfloat("Update Rate", f"Enter the NEW rate for 1 USD to {currency_to_update}:")
        if new_rate is not None and new_rate > 0:
            exchange_rates[currency_to_update] = new_rate
            save_rates()
            messagebox.showinfo("Success", f"Rate for {currency_to_update} updated successfully.")
        else:
            messagebox.showwarning("Warning", "Invalid rate entered. Rate must be positive.")
    else:
        messagebox.showerror("Error", "Currency not found. Use 'Add New Currency' to add it.")

# ------------------- Add New Currency Function -------------------
def add_currency():
    """Allows user to add a new currency and its rate against USD"""
    new_currency = simpledialog.askstring("Add Currency", "Enter the NEW currency code (e.g., CAD):").upper()
    if new_currency and new_currency not in exchange_rates:
        new_rate = simpledialog.askfloat("Add Rate", f"Enter the rate for 1 USD to {new_currency}:")
        if new_rate is not None and new_rate > 0:
            exchange_rates[new_currency] = new_rate
            save_rates()
            # Update the combobox lists
            currencies = list(exchange_rates.keys())
            from_currency_cb['values'] = currencies
            to_currency_cb['values'] = currencies
            messagebox.showinfo("Success", f"Currency {new_currency} added successfully.")
        else:
            messagebox.showwarning("Warning", "Invalid rate entered. Rate must be positive.")
    elif new_currency:
        messagebox.showerror("Error", "Currency already exists.")

# ------------------- Tkinter Setup -------------------
root = tk.Tk()
root.title("Offline Currency Converter")
root.geometry("400x550")
root.resizable(False, False)
root.configure(bg="#f5f5f5")
style = ttk.Style(root)
style.theme_use('clam')

# ------------------- Variables -------------------
result_var = tk.StringVar(root)
result_var.set("Result will appear here")

# ------------------- Title -------------------
tk.Label(root, text="Offline Currency Converter", font=("Arial", 16, "bold"),
         bg="#f5f5f5", fg="#333").pack(pady=10)

# ------------------- Amount Input -------------------
tk.Label(root, text="Amount:", font=("Arial", 12), bg="#f5f5f5").pack()
amount_entry = tk.Entry(root, font=("Arial", 12), justify='center', width=20)
amount_entry.pack(pady=5)
amount_entry.focus_set()

# ------------------- Result Display -------------------
tk.Label(root, textvariable=result_var, font=("Arial", 14, "italic"),
         bg="#f5f5f5", fg="#007BFF", relief=tk.SUNKEN, padx=10, pady=10).pack(pady=10)

# ------------------- Currency Options -------------------
currencies = list(exchange_rates.keys())

# ------------------- From Currency -------------------
tk.Label(root, text="From Currency:", font=("Arial", 12), bg="#f5f5f5").pack()
from_currency_cb = ttk.Combobox(root, values=currencies, font=("Arial", 12))
from_currency_cb.set("USD")
from_currency_cb.pack(pady=5)

# ------------------- To Currency -------------------
tk.Label(root, text="To Currency:", font=("Arial", 12), bg="#f5f5f5").pack()
to_currency_cb = ttk.Combobox(root, values=currencies, font=("Arial", 12))
to_currency_cb.set("NGN")
to_currency_cb.pack(pady=5)

# ------------------- Buttons -------------------
convert_btn = tk.Button(root, text="Convert", command=convert_currency,
                        font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", activebackground="#45a049")
convert_btn.pack(pady=10, padx=20, fill=tk.X)

swap_btn = tk.Button(root, text="Swap Currencies", command=swap_currencies,
                     font=("Arial", 12, "bold"), bg="#2196F3", fg="white", activebackground="#0b7dda")
swap_btn.pack(pady=5, padx=20, fill=tk.X)

update_btn = tk.Button(root, text="Update Exchange Rate", command=update_rate,
                       font=("Arial", 12, "bold"), bg="#FF9800", fg="white", activebackground="#fb8c00")
update_btn.pack(pady=5, padx=20, fill=tk.X)

add_btn = tk.Button(root, text="Add New Currency", command=add_currency,
                    font=("Arial", 12, "bold"), bg="#9C27B0", fg="white", activebackground="#8e24aa")
add_btn.pack(pady=5, padx=20, fill=tk.X)

# ------------------- Run Application -------------------
if __name__ == "__main__":
    root.mainloop()
