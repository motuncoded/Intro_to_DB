import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (replace host, user, password with your credentials)
        connection = mysql.connector.connect(
            host='3000',
            user='motunrayo',
            password='your_password'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        # Close cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()