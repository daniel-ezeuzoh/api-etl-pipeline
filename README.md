# API to SQLite ETL Pipeline

A modular Python application that demonstrates a real-world ETL (Extract, Transform, Load) workflow.

## 🚀 What This Project Does
1. **Extracts:** Fetches live JSON data from a public REST API (JSONPlaceholder) using the `requests` library.
2. **Transforms:** Cleans and extracts nested data using custom Python Object-Oriented Programming (OOP) classes.
3. **Loads:** Saves the transformed data into a local SQLite relational database.

## 🛠️ Skills Demonstrated
- **API Integration:** Handling HTTP requests, status codes, and network exceptions.
- **Data Security:** Using `.env` files and `python-dotenv` to hide API URLs and secrets.
- **Object-Oriented Programming:** Using Classes to represent data (`User` model).
- **Database Management:** Using `sqlite3` to create tables and execute secure parameterized queries (`?`) to prevent SQL injection.
- **Modular Design:** Separating the API client, data models, and database loader into distinct files.

## 📦 How to Run Locally
1. Install dependencies:
   ```bash
   python -m pip install requests python-dotenv

2. Create a .env file with the API URL:
   API_URL=https://jsonplaceholder.typicode.com/users

3. Run the pipeline:
   python api_client.py
   
