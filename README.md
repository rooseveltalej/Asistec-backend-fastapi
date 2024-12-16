# Backend Migration: Node.js (TypeScript) to Python (FastAPI)

This repository contains the fully migrated backend system from **Node.js** (TypeScript) to **Python** (FastAPI). The migration aimed to maintain all core functionalities, enhance performance, and utilize FastAPI's features for better validation, maintainability, and documentation.

---

## 🚀 Features Implemented

### **1. Users Module**
- **Create User (`POST /usuarios/`)**:
  - Validates email format (`@estudiantec.cr`) and ensures uniqueness.
  -  [Planned] Hashes the password before storing it in MongoDB.
  - Returns the created user's ID.

- **User Login (`POST /usuarios/login`)**:
  - Validates credentials using bcrypt.
  - Returns user details (excluding password) if authentication succeeds.

### **2. Schedules Module**
- **Register Activity (`POST /schedules/registerActivity/{user_id}`)**:
  - Creates an activity linked to a `scheduleId` and `userId`.
  - Validates that the user and schedule exist.

- **Get Activities (`GET /schedules/getActivities/{user_id}`)**:
  - Fetches all activities related to a `userId` through `scheduleId`.

- **Update Activity (`PUT /schedules/updateActivity/{activity_id}`)**:
  - Updates an activity's details by its `activity_id`.

- **Delete Activity (`DELETE /schedules/deleteActivity/{activity_id}`)**:
  - Deletes an activity by its `activity_id`.

- **Delete Activities by Relation (`DELETE /schedules/deleteActivitiesByRelationId/{relation_id}`)**:
  - Deletes all activities associated with a given `relation_id`.

### **3. Events Module**
- **Create Event (`POST /events/registerEvent/{user_id}`)**:
  - Creates a new event linked to a user.
  - Validates the user and formats the event data.

- **Get Events (`GET /events/getEvents/{user_id}`)**:
  - Retrieves all events associated with a specific user.

- **Update Event (`PUT /events/updateEvent/{event_id}`)**:
  - Updates the details of a specific event.

- **Delete Event (`DELETE /events/deleteEvent/{event_id}`)**:
  - Deletes a specific event by its ID.

---

## 🛠️ Project Structure

```plaintext
.
├── app.py               # Entry point for the FastAPI application
├── routes/              # API route definitions
│   ├── users.py         # Routes for user-related operations
│   ├── schedules.py     # Routes for schedule-related operations
│   └── events.py        # Routes for event-related operations
├── controllers/         # Business logic for the application
│   ├── users.py         # Controllers for user operations
│   ├── schedules.py     # Controllers for schedule operations
│   └── events.py        # Controllers for event operations
├── models/              # Database models
│   ├── user.py          # MongoDB model for users
│   ├── activity.py      # MongoDB model for activities
│   └── event.py         # MongoDB model for events
├── schemas/             # Pydantic schemas for validation
│   ├── users.py         # Schemas for user operations
│   ├── activities.py    # Schemas for schedule operations
│   └── events.py        # Schemas for event operations
├── core/                # Core configurations
│   ├── __init__.py
│   └── config.py     
├── db/                  # MongoDB connection
│   ├── __init__.py
│   └── mongo_client.py   
├── .env                 # Environment variables (not included in repo)
├── README.md            # Project documentation
├── requirements.txt     # Dependencies for the project
└── run_server.py        # Script to start the FastAPI server
```
