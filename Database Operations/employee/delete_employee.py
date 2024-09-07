import psycopg2

def delete(empId):
    # Connect to an existing database
    connection = psycopg2.connect("dbname=python_test user=python_test password=python_test")
    
    # Open a cursor to perform database operations
    cursor = connection.cursor()
    query = "delete from employee where employee_id = %d;"
    args = (empId)
    try:
        # Execute a command
        cursor.execute(query % args)
        connection.commit()
        print("Employee deleted")
    except Exception as e:
        connection.rollback()
        print("Error", e)    
    finally:
        cursor.close()
        connection.close()
        
empId = int(input("Enter the employee ID: "))
delete(empId)