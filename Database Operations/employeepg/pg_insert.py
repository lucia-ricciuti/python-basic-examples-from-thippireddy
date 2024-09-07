import psycopg2

connection = psycopg2.connect(database="employeedb",
                              user="test",
                              password="password",
                              host="127.0.0.1",
                              port="5432")

print("Connected to EmployeeDB")
cursor = connection.cursor()
cursor.execute("insert into employee (name, sal) values ('Lucia', 2500)")
connection.commit()

print("Employee created")

connection.close()