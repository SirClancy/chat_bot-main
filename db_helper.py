import mysql.connector

global db_config

db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Twcp#4@6217vx',
        'database': 'pandeyji_eatery',
    }

def get_order_status(order_id):
    # Replace these values with your MySQL database connection details
  

    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(**db_config)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Query to retrieve the status for a given order_id
        query = f"SELECT status FROM order_tracking WHERE order_id = {order_id};"

        # Execute the query
        cursor.execute(query)

        # Fetch the result
        result = cursor.fetchone()

        if result:
            # Extract the status from the result
            status = result[0]
            print(f"Status for Order ID {order_id}: {status}")
        else:
            print(f"No status found for Order ID {order_id}")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Replace 'your_order_id' with the actual order_id you want to query
order_id_to_query = 'your_order_id'
get_order_status(order_id_to_query)
