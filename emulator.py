import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import threading

# Function to simulate a barcode scan
def simulate_scan():
    barcode_data = entry.get()  # Get data from the barcode entry box
    try:
        delay = float(delay_entry.get())  # Get delay time in seconds
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid delay time.")
        return

    if barcode_data:
        # Start a separate thread to avoid freezing the Tkinter GUI
        threading.Thread(target=type_barcode, args=(barcode_data, delay)).start()
    else:
        messagebox.showwarning("Warning", "Please enter a barcode to scan.")

def type_barcode(barcode_data, delay):
    time.sleep(delay)  # Wait specified seconds before simulating barcode scan
    pyautogui.write(barcode_data)
    pyautogui.press('enter')

# Initialize main window
window = tk.Tk()
window.title("Barcode Scanner Emulator")
window.geometry("300x250")

# Create an entry box for barcode input
entry_label = tk.Label(window, text="Enter Barcode:")
entry_label.pack(pady=5)
entry = tk.Entry(window, width=30)
entry.pack(pady=5)

# Create an entry box for delay input
delay_label = tk.Label(window, text="Enter Delay (seconds):")
delay_label.pack(pady=5)
delay_entry = tk.Entry(window, width=10)
delay_entry.pack(pady=5)

# Create a button to simulate the scan
scan_button = tk.Button(window, text="Simulate Scan", command=simulate_scan)
scan_button.pack(pady=10)

# Run the main loop
window.mainloop()
