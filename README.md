# Database Design Assignment

## Description
This project demonstrates database design, implementation, and API integration using both SQL (PostgreSQL) and NoSQL (MongoDB) databases. It also includes a classification ML model and a script to fetch data from the database for the laptop dataset to predict whether a laptop is cheap or expensive.

## Dataset Description

For this assignment we used a laptop price dataset that  contains information about 1,276 laptops, including specifications such as brand, screen size, weight, operating system, processor, and storage to classify if a laptop is either cheap or expensive.

## Dataset Used: [Laptop price ](Database-Design_Assignment/laptop_prices.csv)


## Columns Overview:

**Company** – Laptop manufacturer (e.g., Apple, Dell, HP).
**Product** – Model name of the laptop.
**TypeName** – Category of the laptop (Notebook, Ultrabook, etc.).
**Inches** – Screen size in inches.
**Weight** – Laptop weight in kg.
**OS** – Operating system (Windows, macOS, Linux, etc.).
**Price_euros** – Price of the laptop in euros (Target variable for regression).
**Other Features**: Screen resolution, CPU type, GPU type, RAM, and storage details

## Tasks

The project is divided into **three main tasks**:

# Task 1: Create a Database in SQL and MongoDB

## PostgreSQL Database

Our PostgreSQL database is designed to store and manage information about laptops and their specifications efficiently. The schema follows a relational structure where different aspects of a laptop, such as CPU, GPU, storage, and screen details, are stored in separate tables and linked through foreign keys. This approach maintains data consistency, reduces redundancy, and enhances scalability.

### Laptop Table
The Laptop table serves as the central entity, containing key details about each laptop, such as brand, product name, size, weight, price, and operating system. It also holds foreign keys linking it to other tables, ensuring normalized data storage.

### Price History (Logs)
To track changes in laptop prices over time, we maintain a priceHistory/logs table. This table records every price update, including the old price, new price, and the timestamp of the change. A trigger function automatically logs price modifications to maintain historical data.

### CPU Table
The CPU table stores information about different processors used in laptops, including brand, frequency (GHz), and model name. Each laptop links to a specific CPU using a foreign key.

### GPU Table
Similarly, the GPU table contains details about the graphics processing unit (GPU) used in each laptop, including brand and model. The gpuId in the Laptop table references this table.

### Storage Table
The Storage table records primary and secondary storage capacities, along with the storage type (e.g., SSD or HDD). Each laptop references this table to store storage configuration details.

### Screen Specifications (LaptopScreen Table)
To manage display details, the laptopScreen table contains screen size, resolution (width & height), touch capability, IPS panel presence, and Retina display support. Each laptop is linked to a specific screen configuration through a foreign key.

### Key Features of the Schema
- **Normalized Structure**: Data is split into separate tables to reduce redundancy and improve efficiency.
- **Historical Price Tracking**: The price history table automatically logs price changes via a trigger function.
- **Stored Procedures**: We use stored procedures to handle complex database operations efficiently.
- **Scalability**: The schema allows easy expansion, supporting additional features like user reviews, benchmarks, or inventory management.

## MongoDB Database

For MongoDB database we designed a MongoDB database using a hybrid approach that balances normalization and denormalization for efficient data storage and retrieval. Instead of using foreign keys like in SQL, we store related data in separate collections and reference them using ObjectId to ensure consistency, eliminates redundancy, and improves query performance while allowing flexibility for future changes.

### Laptops Collection
The laptops collection serves as the main entity, storing laptop-related details such as brand, model, size, weight, price, and operating system. It contains references (ObjectId) to other collections, such as CPU, GPU, Storage, and Screen Details.

### Price History (Logs) Collection
To track price changes over time, we maintain a priceHistory collection that stores previous and new prices along with a timestamp of the change. Every time a price is updated, a new document is inserted into this collection, ensuring historical price tracking.

### CPU Collection
The cpu collection contains processor details such as brand, frequency (GHz), and model. Instead of embedding this data directly into each laptop document, we store it as a separate collection and reference it using an ObjectId to avoid redundancy.

### GPU Collection
The gpu collection stores details about graphics cards used in laptops, including brand and model. The laptops collection references the gpu collection to keep the data modular.

### Storage Collection
To efficiently manage laptop storage configurations, we store primary and secondary storage details in a separate storage collection. Each laptop document references a storage configuration using an ObjectId.

### Screen Specifications (LaptopScreen Collection)
Instead of duplicating screen details for every laptop, we maintain a laptopScreen collection to store properties such as screen size, resolution, touch capability, IPS panel, and Retina display support. Laptops reference this collection as needed.

**ERD Diagram** 

![LaptopDB](https://github.com/user-attachments/assets/65354485-dfa7-4a47-bc91-091fa251ec15)


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



   
