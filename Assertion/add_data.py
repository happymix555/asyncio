#####################################################
# Add new data to users table from user input


import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# get lastest id from db
cursor.execute("SELECT id FROM users ORDER BY id DESC LIMIT 1")
last_id = cursor.fetchone()[0]

end = 'n'
while end == 'n':
	# set last_id to the next id to be inserted
	last_id += 1
	id = last_id

	# get users from input
	username = input("Enter username: ")
	email = input("Enter email: ")
	password = input("Enter password: ")
	# Define the data to be inserted
	user_data = ( id, username, email, password )

	print( f'\nData to be inserted: {user_data}' )

	# Insert data into the 'users' table
	insert_users_query = "INSERT INTO users (id, username, email, password) VALUES (?, ?, ?, ?)"
	cursor.execute(insert_users_query, user_data)

	conn.commit()
	print( 'Data added to users table successfully.' )

	end = input("End? (y/n): ")
	print( '-' * 50 )

# Commit the changes and close the connection
conn.close()

print("Data added to 'users' table successfully.")
