''' This program is used to demonstrate how to work with Asyncio's Event

	Event is used to tell asyncio's task that something has happened.
'''

import asyncio

numberToBeSetInt = 0

# create coroutine
# this coroutine is going to wait for some event to occur
async def coroutineWillWaitForEvent( event, coroutineNameInt ):
	''' This coroutine is going to wait for some event to happened
		before it perform something else

		ARG: 
			event ( asyncio.Event() object )
	'''

	global numberToBeSetInt

	print( 'Coroutine {} is waiting for event to happened'.format( coroutineNameInt ) )

	# waiting for event to happened
	await event.wait()

	print( 'Coroutine {} knows that something has happened'.format( coroutineNameInt ) )

	# after something has happened 
	# performing some work
	result = coroutineNameInt * numberToBeSetInt

	print( 'Coroutine {} performing work and got {} as a result'.format( coroutineNameInt, result ) )

# asyncio task storage 
taskStorageList = list()

# main coroutine
# this is an entry point into asyncio's eventloop
async def main():
	''' This is our main coroutine and is an entry point to asyncio's eventloop
	'''

	global numberToBeSetInt

	# create asyncio event
	event = asyncio.Event()

	# loop 5 times
	for taskNameInt in range( 1, 6 ):

		# create task and store it
		taskStorageList.append( 
			asyncio.create_task( 
				coroutineWillWaitForEvent( event, taskNameInt ),
				name='task_{}'.format( taskNameInt )
			) 
		)
	
	# simulate long running process
	# and yield control to asyncio's eventloop
	await asyncio.sleep( 5 )
	numberToBeSetInt = 2

	# now long running process was done
	# trigger event to tell all tasks that something has happened
	event.set()

	# wait for all task to finish
	asyncio.gather( *taskStorageList )

	# existing the program
	print( 'Existing...' )

# run the program
asyncio.run( main() )





