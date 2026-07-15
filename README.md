# 🚀 FastAPI Customer Management API

A RESTful Customer Management API built using **FastAPI**, **SQLModel**, and **MySQL**. This project demonstrates complete CRUD (Create, Read, Update, Delete) operations with a clean and modular project structure.

## 📌 Features

- ✅ Create a new customer
- ✅ Get all customers
- ✅ Get customer by ID
- ✅ Update customer details
- ✅ Delete a customer
- ✅ MySQL database integration
- ✅ SQLModel ORM
- ✅ Automatic Swagger API documentation
- ✅ Modular and scalable project structure

---

## 🛠️ Tech Stack

| Technology | Description |
|------------|-------------|
| FastAPI | High-performance Python web framework |
| SQLModel | ORM built on SQLAlchemy and Pydantic |
| MySQL | Relational Database |
| SQLAlchemy | Database Engine |
| PyMySQL | MySQL Driver |
| Uvicorn | ASGI Server |

---

## 📂 Project Structure

```
FASTAPI/
│
├── config/
│   └── database.py
│
├── models/
│   └── customers.py
│
├── add_customers.py
├── query_customers.py
├── update_customers.py
├── delete_customers.py
├── main.py
│
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/fastapi-customer-management.git

cd fastapi-customer-management
```

---

### Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install fastapi
pip install uvicorn
pip install sqlmodel
pip install sqlalchemy
pip install pymysql
```

Or

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

Create a MySQL database.

```sql
CREATE DATABASE employee;

USE employee;

CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    mobile VARCHAR(255) NOT NULL
);
```

Insert sample records

```sql
INSERT INTO customers (name, email, mobile) VALUES
('Ayesha Nagma', 'ayesha@gmail.com', '9876543210'),
('Rahul Sharma', 'rahul@gmail.com', '9988776655'),
('Priya Singh', 'priya@gmail.com', '9123456789');
```

---

## ⚙️ Configure Database

Update **config/database.py**

```python
DATABASE_URL = "mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/employee"
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

Server

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📖 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /customers | Get all customers |
| GET | /customers/{id} | Get customer by ID |
| POST | /customers | Add a new customer |
| PATCH | /customers/{id} | Update customer |
| DELETE | /customers/{id} | Delete customer |

---

## 📷 API Preview

### Swagger UI

<img width="100%" src="https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png">

---

## Example Request

### POST

```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "mobile": "9876543210"
}
```

---

### Response

```json
{
    "id": 6,
    "name": "John Doe",
    "email": "john@example.com",
    "mobile": "9876543210"
}
```

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Building REST APIs with FastAPI
- Working with SQLModel ORM
- Connecting FastAPI with MySQL
- CRUD operations using SQLAlchemy
- API documentation with Swagger UI
- Structuring scalable FastAPI projects

---

## 🚀 Future Improvements

- JWT Authentication
- User Login & Registration
- Input Validation
- Pagination
- Search Customers
- Docker Support
- Unit Testing
- Environment Variables (.env)

---

## 👨‍💻 Author

**Ayesha Nagma**

- GitHub: https://github.com/ayesha-decodes
- LinkedIn: https://www.linkedin.com/in/your-linkedin/

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!
