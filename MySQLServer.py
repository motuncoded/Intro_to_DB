import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (no specific database selected)
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',     # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )
        cursor = connection.cursor()

        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created or already exists.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()