# API-ETL-Pipeline

Python ETL Pipeline

About the Project

This is a beginner data engineering project built with Python. The goal is to extract user and product data from the Fake Store API, transform the data using Pandas, and load it into a PostgreSQL database.

Tools Used

- Python
- Pandas
- Requests
- PostgreSQL
- SQLAlchemy
- Python-dotenv

How It Works

The project follows three main steps:

1. Extract

Fetches user and product data from the Fake Store API and stores the responses in Pandas DataFrames.

2. Transform

Cleans the data by renaming columns, extracting names and address details, and converting product prices to numeric values.

3. Load

Loads the transformed user and product data into PostgreSQL tables using SQLAlchemy.

Project Structure

python-etl-pipeline/
├── extract.py
├── transform.py
├── load.py
├── main.py
├── __init__.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

Getting Started

Requirements

- Python 3.10 or newer
- PostgreSQL
- Internet connection

1. Clone the repository

git clone https://github.com/kanonokamohelo3000-ux/python-etl-pipeline.git
cd python-etl-pipeline


2. Install the dependencies

pip install -r requirements.txt

3. Set up the database

Create a PostgreSQL database for the project.

Copy ".env.example" to ".env" and add your database details:

DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=etl_database

Keep your ".env" file private and do not upload it to GitHub.

4. Run the project

python main.py

The pipeline will retrieve the data, transform it, and load it into PostgreSQL.

Expected Results

The pipeline loads the data into two tables:

- users — contains user details such as names, email addresses, and addresses.
- products — contains product names, prices, categories, and descriptions.

The pipeline also uses logging to help track its progress and identify errors.

What I Learned

Through this project, I practised:

- Fetching data from a REST API.
- Working with Pandas DataFrames.
- Transforming raw data into a cleaner format.
- Connecting Python to PostgreSQL.
- Using environment variables to manage database credentials.
- Adding basic logging and error handling.

Data Source

"Fake Store API" (https://fakestoreapi.com/)

Author

KAMOHELO KANONO

GitHub: "KanonoKamohelo3000-ux" (https://github.com/kanonokamohelo3000-ux)