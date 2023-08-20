import asyncio
import random
import time

'''
	This program is used to demonstrate how to use asyncio.Queue
	to share data between coroutine in producer-consumer manner.
'''

# producer function
async def producer( queue ):
	''' This function will create item ( just string for now ) and 
		putting it into asyncio's queue

		ARG: queue ( asyncio.Queue )
	'''

	# loop 3 times
	for itemInt in range( 3 ):

		# perform some operation with item
		itemAfterSomeOperation = itemInt + 10

		print( 'Done performing some operation with result = {}'.format( itemAfterSomeOperation ) )

		print( 'putting item into queue' )

		# putting item into queue
		await queue.put( itemAfterSomeOperation )

		print(f'Item: { itemAfterSomeOperation } has been put into queue!')

# consumer function
async def consumer( queue ):
	''' This function will consume item from queue to perform some processing

		ARG: queue ( asyncio.Queue )
	'''

	# loop forever
	while True:

		print( 'Getting item from queue' )

		# get item from queue
		itemInt = await queue.get()

		# signal to stop this program
		if itemInt is None:
			break
		
		print( 'Performing some long running process...' )

		# simulate long running process
		await asyncio.sleep( 5 )

		print( 'The long running process in consumer was done!' )

		# tell asyncio.Queue that formerly enqueued task is done
		# if we use queue.join() method
			# its will block until all task in queue has recieved .task_done call
		queue.task_done()

# our entry point to the event loop
async def main():

	# create instance of asyncio.Queue with maximum queue size = 1 
	queue = asyncio.Queue( maxsize=2 )

	# create producer task
	producerTask = asyncio.create_task( producer( queue ), name='producer task' )

	# creat consumer task
	consumerTask = asyncio.create_task( consumer( queue ), name='consumer task' )

	print( 'We have created producer and consumer task and scheduled it to run in eventloop...' )

	# yield control to the eventloop to run tasks in it for sometime
	await asyncio.sleep(10)

	# signal consumer to stop
	await queue.put( None )

	# wait for both producer and consumer to finish 
	await asyncio.gather( producerTask, consumerTask )

	print( 'Exiting...' )

# run our program
asyncio.run( main() )