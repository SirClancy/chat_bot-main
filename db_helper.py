import mysql.connector

global db_config

db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Twcp#4@6286vx',
        'database': 'pandeyji_eatery',
        'port': '3306'
    }


def get_order_status(order_id):
    # Replace these values with your MySQL database connection details


        # Connect to the MySQL database
        connection = mysql.connector.connect(**db_config)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Query to retrieve the status for a given order_id
        query = f"SELECT status FROM order_tracking WHERE order_id = {order_id}"


        # Execute the query
        cursor.execute(query)


        # Fetch the result
        result = cursor.fetchone()

        cursor.close()

        if result is not None:            
                return result[0]
        else:
                return None

#         if result:
#             # Extract the status from the result
#             status = result[0]
#             print(f"Status for Order ID {order_id}: {status}")
#         else:
#             print(f"No status found for Order ID {order_id}")


# # Replace 'your_order_id' with the actual order_id you want to query
# order_id_to_query = 41
# print (get_order_status(order_id_to_query))
