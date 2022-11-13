import tkinter as tk
from tkinter import ttk

def main_window():
    def ok_cmd():
        other_button.configure(state=tk.Normal)
        print(f"Patient name {patient_name_entry.get()}")
        print(f"Patient name {patient_id_entry.get()}")
        print(f"Blood type {blood_letter_selection.get()}")
        print(f"Check state {rh_button.get()}")
        print("Clicked OK button")


    root = tk.Tk()
    root.title("Blood Donor Database Window")
    root.geometry("600x300")

    ttk.Label(root, text = "Blood Donor Database").grid(column=0, row=0, columnspan = 2, sticky=tk.W)
    ttk.Label(root, text="Name:").grid(column=0, row=1)
    ttk.Label(root, text="ID:").grid(column=0, row=2, sticky=tk.E)

    patient_name_entry = tk.StringVar()
    patient_name_entry.set("Enter patient name here")
    ttk.Entry(root, width= 50, textvariable=patient_name_entry).grid(column=1, row=1, sticky=tk.W)

    patient_id_entry = tk.IntVar()
    patient_id_entry.set("Enter patient id here")
    ttk.Entry(root, width= 50, textvariable=patient_id_entry).grid(column=1, row=2)

    blood_letter_selection = tk.StringVar()
    ttk.Radiobutton(root, text = "A", variable = blood_letter_selection, value = "A").grid(column = 0, row = 3)
    ttk.Radiobutton(root, text = "B", variable = blood_letter_selection, value = "B").grid(column = 0, row = 4)
    ttk.Radiobutton(root, text = "AB", variable = blood_letter_selection, value = "C").grid(column = 0, row = 5)
    ttk.Radiobutton(root, text = "O", variable = blood_letter_selection, value = "D").grid(column = 0, row = 6)
    
    rh_button = tk.StringVar()
    ttk.Checkbutton(root, text = "Rh Positive", variable=rh_button, onvalue="+", offvalue="-").grid(column=1,row=5)

    other_button = ttk.Button(root)

    ttk.Label(root, text="Closest Donation Center").grid(column=2, row=0)
    donor_center = tk.StringVar()
    donor_center_combo = ttk.Combobox(root, textvariable=donor_center)
    donor_center_combo.grid(column=2, row=1)
    donor_center_combo["values"] = ["Durham", "Carry", "Raleigh"]

    ttk.Button(root, text="Ok", command=ok_cmd).grid(column=1, row=6)


    root.mainloop()


if __name__ == '__main__':
    main_window()