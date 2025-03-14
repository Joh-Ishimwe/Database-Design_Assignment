# Database Design Assignment

## Description
This project is a FastAPI-based application that demonstrates database design, implementation, and API integration using both SQL (PostgreSQL) and NoSQL (MongoDB) databases. It includes CRUD operations for managing laptop data and integrates with a hosted database for machine learning predictions.

## Tasks
The project is divided into **3 tasks**:

### **Task 1: Create a Database in SQL and MongoDB**
- Designed and implemented a relational database schema with **PostgreSQL**.
- Created an **ERD Diagram** to visualize the schema.
- Implemented the database using **MongoDB collections**.
- Added a **stored procedure** and **trigger** in the SQL database for data validation and logging.

### **Task 2: Create API Endpoints for CRUD Operations**
- Developed **CRUD endpoints** using **FastAPI** for both SQL and NoSQL databases.
- Implemented **input validation** using Pydantic models.
- Deployed the API on **Render** with hosted NoSQL database integration.

### **Task 3: Create a Script to Fetch Data for Prediction**
- Wrote a script to fetch the latest data entry using the API.
- Prepared the data for machine learning predictions.
- Integrated a pre-trained machine learning model for predictions.

## Features
- **SQL Database**: CRUD operations for laptops using PostgreSQL.
- **NoSQL Database**: CRUD operations for laptops using MongoDB.
- **API Integration**: RESTful API endpoints for managing data.
- **Machine Learning**: Script to fetch data and prepare it for predictions.

## Technologies Used
- **Backend**: FastAPI
- **Databases**: PostgreSQL, MongoDB
- **API Documentation**: Swagger UI
- **Deployment**: Render

## Installation
Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Joh-Ishimwe/Database-Design_Assignment.git
   cd Database-Design_Assignment
