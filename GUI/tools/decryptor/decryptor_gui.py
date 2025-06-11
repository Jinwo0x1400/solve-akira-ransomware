import tkinter as tk
from tkinter import filedialog, messagebox
import os

def simulate_decrypt(file_path):
    if file_path.endswith('.akira'):
        decrypted_file = file_path.replace('.akira', '.decrypted')
        try:
            with open(decrypted_file, 'w') as f:
                f.write("Simulated file content.")
            return f"[✓] Decrypted: {decrypted_file}"
        except Exception as e:
            return f"[✗] Error: {e}"
    else:
        return "[!] Not an AKIRA file."

def browse_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        result = simulate_decrypt(filepath)
        messagebox.showinfo("Result", result)

def main():
    root = tk.Tk()
    root.title("AKIRA Decryptor Simulator")
    root.geometry("400x200")

    label = tk.Label(root, text="AKIRA Decryptor Simulator", font=("Helvetica", 16))
    label.pack(pady=20)

    browse_btn = tk.Button(root, text="Select Encrypted File", command=browse_file)
    browse_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
