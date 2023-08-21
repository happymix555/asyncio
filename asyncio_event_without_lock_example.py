''' This program is used to demonstrate how to work with Asyncio's Event and lock

	Event is used to tell asyncio's task that something has happened.

	Lock is used to prevent multiple task to access the same resource ( eg. variable )
		at the same time. As this can create race condition and corrupted data.

	In this script we're NOT going to use lock to simulate WRONG order of execution of our program

	The desired behavior is:
		
'''

import asyncio

sharedResourceInt = 0

async def coroutineWithDynamicTimeOfLongRunningProcessWithoutLock( event, longRunningProcessTimeInt ):
	''' This function is used to create a coroutine with variable 
			long running process simulation time
		
		This function is NOT going to use lock to simulate wrong order of execution

		ARGS:
			event ( asyncio.Event() object )
			longRunningProcessTimeInt ( int ), used to specify the long running process simulation time
	'''

	# global variable
	global sharedResourceInt

	# inform
	print( 'Coroutine {} is waiting for event'.format( longRunningProcessTimeInt ) )

	# wait for event ( wait for something to happened )
	await event.wait()

	# inform 
	print( 'Coroutine {} got signal from event that something has happened'.format( longRunningProcessTimeInt ) )
	print( 'Coroutine {} is waiting for the long running process to be done'.format( longRunningProcessTimeInt ) )

	# simulate the long running process 
	await asyncio.sleep( longRunningProcessTimeInt )

	# inform
	print( 'Coroutine {} is done performing the long running process'.format( longRunningProcessTimeInt ) )

	# access and update the shared resource 
	sharedResourceInt += 1

	# inform 
	print( 'Coroutine {} update shared resource and produce {}'.format( longRunningProcessTimeInt, sharedResourceInt ) )

# main coroutine
# this is an entry point into asyncio's eventloop
async def main():
	''' This is our main coroutine and is an entry point to asyncio's eventloop
	'''

	global sharedResourceInt

	# create asyncio event
	event = asyncio.Event()

	# create and schedule the longer long running task to run
	longerTask = asyncio.create_task( coroutineWithDynamicTimeOfLongRunningProcessWithoutLock( event, 4 ) )

	# create and schedule the shorter long running task to run
	shorterTask = asyncio.create_task( coroutineWithDynamicTimeOfLongRunningProcessWithoutLock( event, 2 ) )

	# simulate another long running process before trigger the event
	await asyncio.sleep( 5 )

	# now long running process was done
	# trigger event to tell all tasks that something has happened
	event.set()

	# wait for all task to finish
	await asyncio.gather( longerTask, shorterTask )

	# existing the program
	print( 'Existing...' )

# run the program
asyncio.run( main() )





