import customtkinter as ctk
from tkinter import messagebox, ttk
from pymongo import MongoClient
import csv

# ---------- App Configuration ----------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SimpleInventory(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Inventory System - Authentication")
        self.geometry("400x350")
        self.show_login()

    def show_login(self):
        """Creates the Login UI"""
        self.login_frame = ctk.CTkFrame(self)
        self.login_frame.pack(pady=40, padx=40, fill="both", expand=True)

        ctk.CTkLabel(self.login_frame, text="Admin Login", font=("Roboto", 24, "bold")).pack(pady=20)

        self.user_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Username", width=200)
        self.user_entry.pack(pady=10)

        self.pass_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Password", show="*", width=200)
        self.pass_entry.pack(pady=10)

        ctk.CTkButton(self.login_frame, text="Login", command=self.check_login, corner_radius=10).pack(pady=20)

    def check_login(self):
        """Credential validation"""
        if self.user_entry.get() == "admin" and self.pass_entry.get() == "1234":
            self.login_frame.destroy()
            self.setup_main_app()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    def setup_main_app(self):
        """Initializes the Inventory Dashboard"""
        self.geometry("1200x750")
        self.title("Inventory Management System - Dashboard")

        # Database Connection
        try:
            self.client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
            self.db = self.client["inventory_db"]
            self.products_col = self.db["inventory"]
        except:
            messagebox.showerror("DB Error", "Could not connect to MongoDB!")

        # Variables
        self.id_var, self.name_var = ctk.StringVar(), ctk.StringVar()
        self.qty_var, self.price_var = ctk.StringVar(), ctk.StringVar()

        # Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar - Forms
        self.sidebar = ctk.CTkFrame(self, width=300, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        ctk.CTkLabel(self.sidebar, text="📦 DATA ENTRY", font=("Roboto", 22, "bold")).pack(pady=30)
        
        fields = [("Product ID", self.id_var), ("Name", self.name_var), 
                  ("Quantity", self.qty_var), ("Unit Price", self.price_var)]
        
        for label, var in fields:
            ctk.CTkLabel(self.sidebar, text=label).pack(anchor="w", padx=30)
            ctk.CTkEntry(self.sidebar, textvariable=var, width=240).pack(pady=(0, 15), padx=30)

        # Action Buttons
        ctk.CTkButton(self.sidebar, text="Add Record", command=self.add_item).pack(pady=10)
        ctk.CTkButton(self.sidebar, text="Update Record", fg_color="#3b82f6", command=self.update_item).pack(pady=5)
        ctk.CTkButton(self.sidebar, text="Delete Record", fg_color="#dc2626", command=self.delete_item).pack(pady=5)
        ctk.CTkButton(self.sidebar, text="Export to CSV", fg_color="#10b981", command=self.export_to_csv).pack(pady=30)

        # Main Table
        self.main_view = ctk.CTkFrame(self, fg_color="transparent")
        self.main_view.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.tree = ttk.Treeview(self.main_view, columns=("ID", "Name", "Qty", "Price"), show="headings")
        for col in ("ID", "Name", "Qty", "Price"):
            self.tree.heading(col, text=col.upper())
            self.tree.column(col, anchor="center")
        self.tree.pack(fill="both", expand=True)
        
        self.refresh_table()

    def refresh_table(self):
        """Read operation: Fetch all records"""
        for i in self.tree.get_children(): self.tree.delete(i)
        for row in self.products_col.find():
            self.tree.insert("", "end", values=(row.get("pid"), row.get("name"), row.get("qty"), row.get("price")))

    def add_item(self):
        """Create operation with validation"""
        try:
            if not self.id_var.get() or not self.name_var.get():
                raise ValueError("Required")
            self.products_col.insert_one({
                "pid": self.id_var.get(), "name": self.name_var.get(), 
                "qty": int(self.qty_var.get()), "price": float(self.price_var.get())
            })
            self.refresh_table()
        except ValueError:
            messagebox.showwarning("Validation Error", "Check your inputs (Numbers only for Qty/Price)")

    def update_item(self):
        """Update operation"""
        self.products_col.update_one({"pid": self.id_var.get()}, {"$set": {
            "name": self.name_var.get(), "qty": int(self.qty_var.get()), "price": float(self.price_var.get())
        }})
        self.refresh_table()

    def delete_item(self):
        """Delete operation with confirmation"""
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this record?"):
            self.products_col.delete_one({"pid": self.id_var.get()})
            self.refresh_table()

    def export_to_csv(self):
        """Bonus: Export records to CSV"""
        try:
            with open("inventory_report.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Product ID", "Name", "Quantity", "Price"])
                for row in self.products_col.find():
                    writer.writerow([row.get("pid"), row.get("name"), row.get("qty"), row.get("price")])
            messagebox.showinfo("Export Success", "Saved to inventory_report.csv")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {e}")

if __name__ == "__main__":
    app = SimpleInventory()
    app.mainloop()
