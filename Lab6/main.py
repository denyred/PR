import psycopg2

conn = psycopg2.connect(database="master", user="postgres", password="admin", host="localhost", port=5432)
cur = conn.cursor()

print("1. Add user")
print("2. Update user")
print("3. Delete user")
print("4. Quit")

while True:
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter name: ")
        email = input("Enter email: ")
        insert_sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        insert_values = (name, email)
        cur.execute(insert_sql, insert_values)
        conn.commit()
        print("User added successfully!")

    elif choice == '2':
        email = input("Enter email to update: ")
        name = input("Enter new name: ")
        update_sql = "UPDATE users SET name = %s WHERE email = %s"
        update_values = (name, email)
        cur.execute(update_sql, update_values)
        conn.commit()
        print("User updated successfully!")

    elif choice == '3':
        email = input("Enter email to delete: ")
        delete_sql = "DELETE FROM users WHERE email = %s"
        delete_values = (email,)
        cur.execute(delete_sql, delete_values)
        conn.commit()
        print("User deleted successfully!")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1-4.")

cur.close()
conn.close()