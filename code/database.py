import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()

def create_connection():
    """
    Establishes a connection to the PostgreSQL database using SQLAlchemy.
    Returns:
        engine: A SQLAlchemy engine object to interact with the database.
    """
    DATABASE_USERNAME = os.environ["DATABASE_USERNAME"]
    DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
    DATABASE_HOST = os.environ["DATABASE_HOST"]
    DATABASE_PORT = os.environ["DATABASE_PORT"]
    DATABASE_DATABASE = os.environ["DATABASE_DATABASE"]

    SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DATABASE}"

    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    return engine

if __name__ == "__main__":
    engine = create_connection()
    try:
        with engine.connect() as connection:
            print("Database connection successful!")
    except Exception as e:
        print(f"Error: {e}")