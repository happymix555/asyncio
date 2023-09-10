#####################################################
# This script creates a SQLite database and tables,
# and adds data to the tables.
# provided by chatGPT

import sqlite3

# Create a connection to the SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define the SQL statements to create tables
create_users_table = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
'''

create_office_locations_table = '''
CREATE TABLE IF NOT EXISTS office_locations (
    id INTEGER PRIMARY KEY,
    location_name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    postal_code TEXT NOT NULL
)
'''

# Execute the SQL statements to create tables
cursor.execute(create_users_table)
cursor.execute(create_office_locations_table)

# Commit the changes and close the connection
conn.commit()
conn.close()

#####################################################

print("Database and tables created successfully.")

# Create a connection to the SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Insert data into the 'users' table
user_data = [
    (1, 'user1', 'user1@email.com', 'password1'),
    (2, 'user2', 'user2@email.com', 'password2'),
    (3, 'user3', 'user3@email.com', 'password3')
]

insert_users_query = "INSERT INTO users (id, username, email, password) VALUES (?, ?, ?, ?)"
cursor.executemany(insert_users_query, user_data)

# Insert data into the 'office_locations' table
location_data = [
    (1, 'Office A', '123 Main St', 'City A', 'State A', '12345'),
    (2, 'Office B', '456 Elm St', 'City B', 'State B', '67890'),
    (3, 'Office C', '789 Oak St', 'City C', 'State C', '98765')
]

insert_locations_query = "INSERT INTO office_locations (id, location_name, address, city, state, postal_code) VALUES (?, ?, ?, ?, ?, ?)"
cursor.executemany(insert_locations_query, location_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data added to tables successfully.")
