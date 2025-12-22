# user_management_system

User Management System (Desktop App)
Tech Stack

Python

CustomTkinter (Tkinter-based UI)

SQLite

This project follows a clean, layered architecture to allow two developers to work in parallel without conflicts.

user_management_system/
│
├── app.py
│
├── config/
│   └── settings.py
│
├── database/
│   ├── db.py
│   ├── models.py
│   └── seed_data.py
│
├── services/
│   ├── user_service.py
│   ├── auth_service.py
│   └── log_service.py
│
├── ui/
│   ├── login_window.py
│   ├── main_window.py
│   ├── user_form.py
│   └── components/
│       ├── sidebar.py
│       ├── table.py
│       ├── buttons.py
│       └── dialogs.py
│
├── utils/
│   ├── validators.py
│   └── helpers.py
│
├── assets/
│   ├── icons/
│   └── images/
│


HARD RULES (MANDATORY)

UI must NEVER talk directly to the database

UI must NEVER contain SQL

Database layer must NEVER import UI

Services are the ONLY layer allowed to contain business logic

Each file has ONE responsibility

No circular imports

If logic grows, it goes into services/, not UI
