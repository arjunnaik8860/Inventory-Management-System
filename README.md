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

## How to Run
1. Ensure **MongoDB** is running on your local machine (`localhost:27017`).
2. Install required libraries:
   `pip install customtkinter pymongo`
3. Run the application:
   `python app.py`
