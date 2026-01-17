# Inventory-Management-System
# Inventory Management System (Python & MongoDB)

## Project Description
This application is a modern Inventory Management System designed to replace manual record-keeping. It allows administrators to track product stock, update prices, and delete obsolete records through a user-friendly graphical interface.

## Scenario Chosen
**Inventory Management System**: Real-world application for a mid-sized retail or warehouse setting.

## Technologies Used
- **Language**: Python 3.x
- **GUI Library**: CustomTkinter
- **Database**: MongoDB (Local Instance)
- **Integration**: PyMongo
- **Data Export**: CSV Library

## Key Features
1. **Authentication**: Secure admin login (User: admin, Pass: 1234).
2. **Full CRUD**: Create, Read, Update, and Delete operations for inventory items.
3. **Validation**: Prevents empty fields or incorrect data types from being saved.
4. **Export**: One-click functionality to save all records to an external CSV file.

## Key Features
1. **# Database Connection
        try:
            self.client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
            self.db = self.client["inventory_db"]
            self.products_col = self.db["users"]
        except:
            messagebox.showerror("DB Error", "Could not connect to MongoDB!")**
   
## How to Run
1. Ensure **MongoDB** is running on your local machine (`localhost:27017`).
2. Install required libraries:
   `pip install customtkinter pymongo`
3. Run the application:
   `python app.py`

   ![WhatsApp Image 2026-01-17 at 8 51 43 PM](https://github.com/user-attachments/assets/c1a3f79d-0a61-401b-a67e-3c9b2d553128)

![WhatsApp Image 2026-01-17 at 8 47 22 PM](https://github.com/user-attachments/assets/05474cf9-6f18-46a5-ae5f-e05b5452ddaa)
