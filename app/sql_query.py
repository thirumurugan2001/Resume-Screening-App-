from app.dbconnection import dbconnection

# Function to get all the users email  details
def getAllUserEmail():
    try:
        connection=dbconnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT email FROM users""")
        email = cursor.fetchall()
        cursor.close()
        connection.close()
        return  email
        
    except Exception as e:
        print(f"Error: Unable to connect to the database. {e}")
        return []