# 📌 Mini Project Management System

## 🚀 Project Overview

This is a **Mini Project Management System** where a company can manage:

* Users (admin / developer)
* Projects
* Tasks assigned to users

The system supports authentication, task assignment, status tracking, filtering, and pagination.

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic (for migrations)
* JWT Authentication

### Frontend

Not implemented frontend 

---

## 🧱 Architecture

The backend follows a **layered architecture**:

```
API Layer → Service Layer → Database Layer
```

* **API Layer**: Handles request/response
* **Service Layer**: Business logic
* **DB Layer**: Models and queries

---

## 🗄️ Database Design (ER Diagram)

```
User
 ├── id
 ├── name
 ├── email
 ├── role

Project
 ├── id
 ├── name
 ├── description
 ├── created_by → User.id

Task
 ├── id
 ├── title
 ├── description
 ├── status
 ├── project_id → Project.id
 ├── assigned_to → User.id
 ├── due_date
```

---

## 🔐 Authentication

* JWT-based authentication
* Login endpoint returns access token
* All protected APIs require:

```
Authorization: Bearer <token>
```

---

## 📡 API Endpoints

### 🔑 Auth

* `POST /auth/login`

### 👤 Users

* `POST /users` → Create user
* `GET /users` → List users

### 📁 Projects

* `POST /projects` → Create project
* `GET /projects` → List projects
* `PUT /projects/{id}` → Update project
* `DELETE /projects/{id}` → Delete project

### ✅ Tasks

* `POST /tasks` → Create task
* `GET /tasks` → List tasks (with filters + pagination)

Filters:

```
/tasks?project_id=1
/tasks?status=todo
/tasks?assigned_to=2
```

Pagination:

```
/tasks?skip=0&limit=10
```

### 🔄 Task Actions

* `PUT /tasks/{id}/assign`
* `PUT /tasks/{id}/status`

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone <your-repo-url>
cd backend
```

---

### 2. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create `.env` file:

```
DATABASE_URL=postgresql://username:password@localhost:5432/project_db
SECRET_KEY=your_secret_key
```

---

### 5. Run Migrations

```
alembic upgrade head
```

---

### 6. Start Server

```
uvicorn app.main:app --reload
```

---

### 7. Access API Docs

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Testing

* Use Swagger UI (`/docs`) or Postman
* Authenticate using JWT token before accessing protected routes

---

## 🌐 Frontend Setup

```
cd frontend
npm install
npm run dev
```

---

## 📦 Postman Collection

Included in submission:

* All endpoints
* Auth flow
* CRUD operations

---

## 📄 Environment Variables Example

`.env.example`

```
DATABASE_URL=
SECRET_KEY=
```

---

## ⚡ Features Implemented

* JWT Authentication
* Role-based users
* Project management
* Task assignment
* Task status updates
* Filtering & pagination
* Proper HTTP status codes
* Error handling
* DB transactions

---

## 🎯 Conclusion

This project demonstrates:

* Clean backend architecture
* Secure authentication
* Efficient database design
* Scalable API design

---

## 📬 Submission

Include:

* GitHub repo link
* Postman collection JSON
* README file
* `.env.example`

---

## 👨‍💻 Author

**Shamnad**
