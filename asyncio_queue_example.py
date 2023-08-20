import asyncio
import random
import time

'''
	This program is used to demonstrate how to use asyncio.Queue
	to share data between coroutine in producer-consumer manner.

	In this example we're going to use multiple consumer task
'''

QueueSizeInt = 1
NumberOfItemToPutInQueueInt = 2
NumberOfConsumerInt = 2
LongRunningProcessTimeSec = 2

# producer function
async def producer( queue ):
	''' This function will create item ( just string for now ) and 
		putting it into asyncio's queue

		ARG: queue ( asyncio.Queue )
	'''

	# loop to create item in queue according to defined parameter
	for itemInt in range( NumberOfItemToPutInQueueInt ):

		# perform some operation with item
		itemAfterSomeOperation = itemInt + 10

		print( 'Done performing some operation with result = {}'.format( itemAfterSomeOperation ) )

		print( 'try putting item {} into queue'.format( itemAfterSomeOperation ) )

		# putting item into queue
		await queue.put( itemAfterSomeOperation )

		print( 'Item: {} has been put into queue!'.format( itemAfterSomeOperation ) )
	
	print( 'All Item has been processed so stopping the producer now' )

# consumer function
async def consumer( queue, consumerNameStr ):
	''' This function will consume item from queue to perform some processing

		ARG: queue ( asyncio.Queue )
	'''

	# loop forever
	while True:

		print( 'Consumer {} is getting item from queue'.format( consumerNameStr ) )

		# get item from queue
		itemInt = await queue.get()

		print( 'Consumer {} got item {} from queue'.format( consumerNameStr, itemInt ) )
		
		print( 'Consumer {}, Performing some long running process of item {}'.format( consumerNameStr, itemInt ) )

		# simulate long running process
		await asyncio.sleep( LongRunningProcessTimeSec )

		print( 'Consumer {}, The long running process of item {} in consumer was done!'.format( consumerNameStr, itemInt ) )

		# tell asyncio.Queue that formerly enqueued task is done
		# if we use queue.join() method
			# its will block until all task in queue has recieved .task_done call
		queue.task_done()

# our entry point to the event loop
async def main():

	# create instance of asyncio.Queue with maximum queue size = 1 
	queue = asyncio.Queue( maxsize=QueueSizeInt )

	# create producer task
	producerTask = asyncio.create_task( producer( queue ), name='producer task' )

	# consumer task storage 
	consumerTaskList = list()

	# loop 5 time
	for consumerCount in range( NumberOfConsumerInt ):

		# creat consumer task with name
		# and store it
		consumerTaskList.append( asyncio.create_task( consumer( queue, str( consumerCount ) ), name='consumer_task_{}'.format( consumerCount ) ) )

	print( 'We have created producer and consumer task and scheduled it to run in eventloop...' )

	# yield control of our program to eventloop and 
	# wait for producer task to finish 
	await producerTask

	# wait for all item in queue to be processed
	await queue.join()

	# loop through each consumer task
	for consumerTask in consumerTaskList:

		# cancel consumer task	
		consumerTask.cancel()
	
	# wait until all worker tasks are cancelled
	await asyncio.gather( *consumerTaskList, return_exceptions=True )

	print( 'Exiting...' )

# program start time 
startTime = time.time()

# run our program
asyncio.run( main() )

# time used for the whole program
print( 'Time used for the whole program was: {}s'.format( time.time() - startTime ) )