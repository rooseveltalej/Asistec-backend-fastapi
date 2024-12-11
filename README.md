# Backend Migration: Node.js (TypeScript) to Python (FastAPI)

This repository contains the ongoing migration of a backend system originally developed in **TypeScript** using **Node.js** to **Python** using **FastAPI**. The migration aims to maintain or improve the functionality and structure of the original application, while leveraging Python's ecosystem and FastAPI's modern web framework.

---

## 🚧 Current Status: Under Construction 🚧

The backend migration is currently in progress. The following functionalities have been migrated and are functional:

### **Features Migrated**
1. **Users Module**:
   - User creation with email validation.
   - User login with password hashing.
   - MongoDB integration for user data.

2. **Schedules Module**:
   - Fetch activities associated with a user via `scheduleId`.
   - Create, update, and delete activities.
   - MongoDB integration for schedules and activities.

### **Tech Stack**
#### **Current Stack**
- **Framework**: FastAPI
- **Language**: Python
- **Database**: MongoDB (via Motor, an async driver)
- **Authentication**: bcrypt for password hashing (JWT planned for future updates)

#### **Previous Stack**
- **Framework**: Express.js
- **Language**: TypeScript
- **Database**: MongoDB

---

## 🛠️ Project Structure

```plaintext
.
├── app/
│   ├── app.py              # Entry point for the FastAPI application
│   ├── routes/             # API route definitions
│   │   ├── users.py        # Routes for user-related operations
│   │   └── schedules.py    # Routes for schedule-related operations
│   ├── controllers/        # Business logic for the application
│   │   ├── users.py        # Controllers for user operations
│   │   └── schedules.py    # Controllers for schedule operations
│   ├── models/             # Database models
│   │   ├── user.py         # MongoDB model for users
│   │   └── activity.py     # MongoDB model for activities
│   ├── schemas/            # Pydantic schemas for validation
│   │   ├── users.py        # Schemas for user operations
│   │   └── activities.py   # Schemas for activities operations
│   ├── core/               # Core configurations
│   │   ├── __init__.py
│   │   └── database.py     # MongoDB connection
├── .env                     # Environment variables (not included in repo)
└── README.md                # Project documentation            
