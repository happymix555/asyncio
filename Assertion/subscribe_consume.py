import asyncio
import sqlite3
from asyncio import Queue

# Function to query data from SQLite
async def query_data(tableName, lastQueryId):
	''' This function queries data from db and returns it.
	'''
	conn = sqlite3.connect('mydatabase.db')
	cursor = conn.cursor()

	# Simulate querying data from a database based on lastQueryId
	query = f"SELECT id, username FROM {tableName} WHERE id > {lastQueryId} LIMIT 1;"
	cursor.execute(query)
	data = cursor.fetchone()

	# Close the connection
	conn.close()

	# print( f'fetching data: {data}' )
	return data

async def subscribe(queue: asyncio.Queue, lastQueryId: int, tableName: str):
	''' This function will put data from query into queue if found.
			- if found data, it will put data into queue and wait for 1 second to let consume function consume the data
			otherwise, it will continue loop and query data
	'''
	while True:
		data = await query_data(tableName, lastQueryId)
		
		if data is None:
			# print ( "No more data to fetch." )
			continue  # No more data to fetch, exit the loop
		
		lastQueryId = data[0]  # Update lastQueryId
		
		# Put the data into the queue
		await queue.put(data)

		# use sleep to allow consume function process the data
		await asyncio.sleep(0.01)

async def consume(queue):
	''' This function will consume data from queue.
		- it will wait result from queue and print when get it
	'''
	while True:
		# Get data from the queue
		item = await queue.get()

		# Process the item (e.g., print it)
		print(f'Received: {item}')

		# Mark the item as done in the queue
		queue.task_done()

async def main():
	lastQueryId = 0
	queue = Queue()

	tableName = 'users'

	# Create and the subscribe and consume tasks
	subscribe_task = asyncio.create_task(subscribe(queue, lastQueryId, tableName))
	consume_task = asyncio.create_task(consume(queue))

	# Wait for both tasks to complete
	# gather() will run both tasks concurrently and wait for both to complete
	await asyncio.gather(subscribe_task, consume_task)

if __name__ == "__main__":
	asyncio.run(main())
