import tkinter as tk
from tkinter import messagebox, Toplevel
from tkinter import ttk
import subprocess

def open_student_registration():
    reg_win = Toplevel(root)
    reg_win.title("Student Registration")
    reg_win.geometry("400x420")
    reg_win.configure(bg="#93f8f3")

    tk.Label(reg_win, text="University Student Registration", font=("Helvetica", 16, "bold"), bg="#1c1c1c", fg="white").pack(pady=20)

    tk.Label(reg_win, text="Student ID:", bg="#1c1c1c", fg="white").pack()
    entry_id = tk.Entry(reg_win, width=30)
    entry_id.pack(pady=5)

    tk.Label(reg_win, text="Full Name:", bg="#1c1c1c", fg="white").pack()
    entry_name = tk.Entry(reg_win, width=30)
    entry_name.pack(pady=5)

    tk.Label(reg_win, text="Department:", bg="#1c1c1c", fg="white").pack()
    combo_dept = ttk.Combobox(reg_win, values=["CSE", "EEE", "BBA", "LAW", "ENG", "Others"], state="readonly")
    combo_dept.set("Select")
    combo_dept.pack(pady=5)

    tk.Label(reg_win, text="Semester:", bg="#1c1c1c", fg="white").pack()
    combo_semester = ttk.Combobox(reg_win, values=["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th"], state="readonly")
    combo_semester.set("Select")
    combo_semester.pack(pady=5)

    def submit_form():
        id = entry_id.get()
        name = entry_name.get()
        dept = combo_dept.get()
        semester = combo_semester.get()

        if not id or not name or dept == "Select" or semester == "Select":
            messagebox.showerror("Error", "Please fill all the fields!")
            return

        with open("student_info.txt", "a") as f:
            f.write(f"{id},{name},{dept},{semester}\n")

        try:
            subprocess.run(['python', 'capture_images.py', id, name], check=True)
            messagebox.showinfo("Success", "Images captured successfully!")
            reg_win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to capture images:\n{e}")

    tk.Button(reg_win, text="📸 Submit & Capture", width=25, height=2, bg="#4CAF50", fg="white", command=submit_form).pack(pady=15)
    tk.Button(reg_win, text="❌ Cancel", width=25, height=2, bg="#9E9E9E", fg="white", command=reg_win.destroy).pack()

def train_faces():
    try:
        subprocess.run(['python', 'train_model.py'], check=True)
        messagebox.showinfo("Training", "Model trained and saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Training failed:\n{e}")

def take_attendance():
    try:
        subprocess.run(['python', 'recognize_and_log.py'], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Recognition failed:\n{e}")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("AttendXFace - All-in-One")
root.geometry("400x350")
root.configure(bg="#F5F5FC")

tk.Label(root, text="Face ID: Smart Attendance System", font=("Helvetica", 14, "bold"), fg="white", bg="#222222", wraplength=350).pack(pady=20)

tk.Button(root, text="1️⃣ Student Register", width=30, height=2, bg="#86C588", fg="white", command=open_student_registration).pack(pady=10)
tk.Button(root, text="2️⃣ Train Faces", width=30, height=2, bg="#A8D4F8", fg="white", command=train_faces).pack(pady=10)
tk.Button(root, text="3️⃣ Take Attendance", width=30, height=2, bg="#46E6D8", fg="white", command=take_attendance).pack(pady=10)
tk.Button(root, text="❌ Exit", width=30, height=2, bg="#CAC8C8", fg="white", command=exit_app).pack(pady=10)

root.mainloop()


#pip install -r requirements.txt
#python3 -m venv env
#pip install -r requirements.txt
#python main.py