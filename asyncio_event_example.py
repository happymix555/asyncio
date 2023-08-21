''' This program is used to demonstrate how to work with Asyncio's Event nad lock

	Event is used to tell asyncio's task that something has happened.

	Lock is used to prevent multiple task to access the same resource ( eg. variable )
		at the same time. As this can create race condition and corrupted data.
'''

import asyncio

sharedResourceInt = 0

# create coroutine
# this coroutine is going to wait for some event to occur
# then performing something with lock
async def coroutineWithEventAndLock( event, lock, coroutineNameInt ):
	''' This coroutine is going to wait for some event to happened
			before it perform something else

		After got signal from event, this coroutine is going to
			access shared resource and increase its value by 1

		ARG: 
			event ( asyncio.Event() object )
	'''

	global sharedResourceInt

	print( 'Coroutine {} is waiting for event to happened'.format( coroutineNameInt ) )

	# waiting for event to happened
	await event.wait()

	print( 'Coroutine {} knows that something has happened'.format( coroutineNameInt ) )

	# wait for lock to available then access the shared resource
	async with lock:

		# access and update the shared resource
		sharedResourceInt += 1

	print( 'Coroutine {} performing work and update the shared resource to {}'.format( coroutineNameInt, sharedResourceInt ) )

# create coroutine
# this coroutine is going to wait for some event to occur
# then performing something but WITHOUT lock
async def coroutineWithEventButNotLock( event, coroutineNameInt ):
	''' This coroutine is going to wait for some event to happened
			before it perform something else

		After got signal from event, this coroutine is going to
			access shared resource and increase its value by 1
			but this time its is going to simultaneously access the shared resource
			with another coroutine because the 'lock' was not implemented

		ARG: 
			event ( asyncio.Event() object )
	'''

	global sharedResourceInt

	print( 'Coroutine {} is waiting for event to happened'.format( coroutineNameInt ) )

	# waiting for event to happened
	await event.wait()

	print( 'Coroutine {} knows that something has happened'.format( coroutineNameInt ) )

	# access and update the shared resource
	sharedResourceInt += 1

	print( 'Coroutine {} performing work and update the shared resource to {}'.format( coroutineNameInt, sharedResourceInt ) )

async def longerCoroutineWithEventAndLock( event, lock ):
	''' This coroutine is going to simulate the longer long running process
		and the access the shared variable and increase its value by 1

		ARGS:
			event ( asyncio.Event() object )
			lock ( asyncio.Lock() object )
	'''

	# global variable
	global sharedResourceInt

	# inform
	print( 'Longer coroutine is waiting for event' )

	# wait for event ( wait for something to happened )
	await event.wait()

	# inform 
	print( 'Longer coroutine got signal from event that something has happened' )

	# use lock to hold control over shared resource
	async with lock:

		# inform 
		print( 'Longer coroutine is holding control over the shared resource' )
		print( 'Longer coroutine is waiting for the long running process to be done' )

		# simulate the long running process 
		await asyncio.sleep( 5 )

		# inform
		print( 'Longer coroutine is done performing the long running process' )

		# access and update the shared resource 
		sharedResourceInt += 1

		# inform 
		print( 'Longer coroutine update shared resource and produce {}'.format( sharedResourceInt ) )


# asyncio task storage 
taskStorageList = list()

# main coroutine
# this is an entry point into asyncio's eventloop
async def main():
	''' This is our main coroutine and is an entry point to asyncio's eventloop
	'''

	global sharedResourceInt

	# create asyncio event
	event = asyncio.Event()

	# create asyncio lock
	lock = asyncio.Lock()

	# loop 5 times
	for taskNameInt in range( 1, 6 ):

		# # create task and store it
		# taskStorageList.append( 
		# 	asyncio.create_task( 
		# 		coroutineWithEventAndLock( event, lock, taskNameInt ),
		# 		name='task_{}'.format( taskNameInt )
		# 	) 
		# )

		# create task and store it
		taskStorageList.append( 
			asyncio.create_task( 
				coroutineWithEventButNotLock( event, taskNameInt ),
				name='task_{}'.format( taskNameInt )
			) 
		)
	
	# simulate long running process
	# and yield control to asyncio's eventloop
	await asyncio.sleep( 3 )

	# now long running process was done
	# trigger event to tell all tasks that something has happened
	event.set()

	# wait for all task to finish
	asyncio.gather( *taskStorageList )

	# existing the program
	print( 'Existing...' )

# run the program
asyncio.run( main() )





