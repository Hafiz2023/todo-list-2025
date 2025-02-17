import tkinter as tk
from tkinter import ttk, messagebox

class SchoolManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("800x600")
        
        self.data = {
            "students": [],
            "teachers": [],
            "courses": []
        }
        
        self.create_ui()
    
    def create_ui(self):
        ttk.Label(self.root, text="School Management System", font=("Arial", 20)).pack(pady=10)
        
        ttk.Button(self.root, text="Manage Students", command=self.manage_students).pack(pady=5)
        ttk.Button(self.root, text="Manage Teachers", command=self.manage_teachers).pack(pady=5)
        ttk.Button(self.root, text="Manage Courses", command=self.manage_courses).pack(pady=5)
    
    def manage_students(self):
        self.new_window("Student Management", self.add_student, "students")
    
    def manage_teachers(self):
        self.new_window("Teacher Management", self.add_teacher, "teachers")
    
    def manage_courses(self):
        self.new_window("Course Management", self.add_course, "courses")
    
    def new_window(self, title, add_func, category):
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry("400x300")
        
        ttk.Label(win, text=title, font=("Arial", 15)).pack(pady=10)
        
        entry = ttk.Entry(win)
        entry.pack(pady=5)
        ttk.Button(win, text="Add", command=lambda: add_func(entry.get(), category, win)).pack(pady=5)
        
        listbox = tk.Listbox(win)
        listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        
        for item in self.data[category]:
            listbox.insert(tk.END, item)
    
    def add_student(self, name, category, win):
        self.data[category].append(name)
        messagebox.showinfo("Success", f"{name} added successfully!")
        win.destroy()
    
    def add_teacher(self, name, category, win):
        self.data[category].append(name)
        messagebox.showinfo("Success", f"{name} added successfully!")
        win.destroy()
    
    def add_course(self, name, category, win):
        self.data[category].append(name)
        messagebox.showinfo("Success", f"{name} added successfully!")
        win.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolManagementSystem(root)
    root.mainloop()
