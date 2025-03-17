# Database Design Assignment

## Description
This project demonstrates database design, implementation, and API integration using both SQL (PostgreSQL) and NoSQL (MongoDB) databases. It also includes a classification ML model and a script to fetch data from the database for the laptop dataset to predict whether a laptop is cheap or expensive.

## Tasks
The project is divided into **three main tasks**:

### **Task 1: Create a Database in SQL and MongoDB**
- Designed and implemented a relational database schema with **PostgreSQL**.
- Implemented the database using **MongoDB collections**.  
- Created an **ERD Diagram** to visualize the schema.
  
  **Hosted Databases:**
  **MongoDB**:mongodb+srv://kayitesililiane73:ilmjXVwPBIRvY8MN@cluster0.lph39.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
  **PostgreSQL**:postgresql://laptopdb_user:RgRtnEoW5FdENLIAu7ABvzIutmxpacBu@dpg-cv8balbqf0us73b6eg40-a.oregon-postgres.render.com/laptopdb

### **Task 2: Create API Endpoints for CRUD Operations**
- Developed **CRUD endpoints** using **FastAPI** for both SQL(PostgreSQL) and NoSQL(MongoDB) databases.
- Implemented **input validation** using Pydantic models.
- Hosted the API on **Render**.
#### Deployed API
**API Documentation:** https://database-design-assignment.onrender.com/docs

### **Task 3: Create a Script to Fetch Data for Prediction**
- Implemented a classification ML model to predict if a laptop is cheap or expensive.
- Developed a script to fetch the latest data entry from the database using the API.
- Prepared the data for prediction using the trained model


## Technologies Used
- **Backend**: FastAPI
- **Databases**: PostgreSQL, MongoDB
- **API Documentation**: Swagger UI
- **Deployment**: Render


## Group Members 
- Liliane Kayitesi - Task 1
- Josiane Ishimwe - Task2
- Inès IKirezi - Task 3

## Installation
Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Joh-Ishimwe/Database-Design_Assignment.git
   cd Database-Design_Assignment
2. **Create a Virtual Environment & Install Dependencies:**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt

3. **Set Up Environment Variables**(Create a .env file and add credentials for PostgreSQL, MongoDB, and API keys as needed)
4. **Run the FastAPI Server:**
   ```bash
   uvicorn main:app --reload
5.**Access the API Documentation:**
    ```bash 
    Open http://127.0.0.1:8000/docs in your browser.



   
