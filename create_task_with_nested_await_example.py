import asyncio 
import time
import warnings

'''
this program demonstrate how 'await' keyword change the running sequence of our program
from normal( line after line ) into event loop queue

'''

# global variable
taskList = list()
myPrintResultList = list()

programStartTime = time.time()

# create function to get and print all task in event loop
def getAndPrintAllTask( additionalMessageToPrintStr: str = None ):
	
	# get all task
	tasks = asyncio.all_tasks()
	
	# print additional message, if any
	if additionalMessageToPrintStr != None:
		print( additionalMessageToPrintStr )

	# loop through all task
	for task in tasks:
		
		# print task name 
		print( 'Task name: {}'.format( task.get_name() ) )
	
	# separate each print statement with empty line
	print( '\n' )

# create coroutine function
async def myPrint( numToPrintInt: int, timeToSleepInt: int = None ):
	
	# print to inform that we are in myPrint function
	print( 'We are current in myPrint: {}'.format( numToPrintInt ) + '\n' )

	# if time to sleep was specified, then use it
	if timeToSleepInt != None:
		await asyncio.sleep( timeToSleepInt )
	else:
		
		# default sleep for 3 seconds to simulate long running process
		await asyncio.sleep( 3 )
	
	# print to inform that the long running process of this coroutine function is done
	print( 'long running process of myPrint: {} is done \n'.format( numToPrintInt ) )

	return numToPrintInt

# create coroutine function that have asyncio.crate_task() inside of it
async def myPrintAndAddTask( numToPrintInt: int, timeToSleepInt: int = None ):
	
	# print to inform that we are in myPrintAndAddTask function
	print( 'We are currently in myPrintAndAddTask: {} \n'.format( numToPrintInt ) )

	# add task( myPrint ) to event loop using asyncio.create_task()
	myPrintTask = asyncio.create_task( myPrint( numToPrintInt, timeToSleepInt ), name='myPrint( {} )'.format( numToPrintInt ) )

	# show all task waiting in event loop
	getAndPrintAllTask( 'After create myPrint{}'.format( numToPrintInt ) )
	
	# await to wait for the result of myPrintTask
	await myPrintTask
	
	# print to inform that we have finished adding task to event loop
	print( 'myPrintAndAddTask {} was done'.format( numToPrintInt ) + '\n')

	# append task to global task storage
	taskList.append( myPrintTask )

	# append print result to global storage
	myPrintResultList.append( myPrintTask.result() )

# create main function to host all of our coroutine 
async def main():
	
	# print to inform that we are in main function
	print( 'We are in main function' + '\n')
	
	# add the first myPrintAndAddTask task to event loop
	firstMyPrintAndAddTask = asyncio.create_task( myPrintAndAddTask( numToPrintInt=1, timeToSleepInt=5 ), name='myPrintAndAddTask( 1 )' )

	# show all task in event loop
	getAndPrintAllTask( 'After firstMyPrintAndAddTask' )

	# add the second myPrintAndAddTask task to event loop
	secondMyPrintAndAddTask = asyncio.create_task( myPrintAndAddTask( numToPrintInt=2, timeToSleepInt=1 ), name='myPrintAndAddTask( 2 )' )

	# show all task in event loop
	getAndPrintAllTask( 'After secondMyPrintAndAddTask' )

	# print to inform that we are beginning to use 'await' keyword
	print( 'We are beginning to use await keyword' + '\n' )
	
	# begin to use 'await' keyword
	# our program will run line by line until this step
	# then it will switch to execute task queued in an event loop
	await firstMyPrintAndAddTask

	print( 'In main, after firstMyPrintAndAddTask {}'.format( myPrintResultList ) + '\n' )

	await secondMyPrintAndAddTask

	print( 'In main, after secondMyPrintAndAddTask {}'.format( myPrintResultList ) + '\n' )

	# show all task in event loop
	getAndPrintAllTask( 'After await firstMyPrintAndAddTask' )

	# print to inform user that we have finished main function
	print( 'Finished main function' )

# show all task in event loop
# try in case of no event loop exist
try:
	getAndPrintAllTask( 'Before running main function' )
except RuntimeError:
	
	# if event loop dose not exist
	print( 'Before main function, Event loop dose not exist' + '\n' )

########################################################################################################################################################################################################
# # create event loop
# eventLoop = asyncio.new_event_loop()

# # enable debug mode
# eventLoop.set_debug( True )

# # enable resource warning message
# # this will print warning message if we have problem with resource management
# # TODO: not sure what 'resource management' really mean, need to find out
# warnings.simplefilter( 'always', ResourceWarning )

# # try running event loop til it complete
# try:
	
# 	# create an entry point to our event loop and run it
# 	eventLoop.run_until_complete( main() )
# finally:
	
# 	# event loop has finished then close it
# 	eventLoop.close()
########################################################################################################################################################################################################

asyncio.run( main() )

# show all task in event loop
# try in case of no event loop exist
try:
	getAndPrintAllTask( 'After running main function' )
except RuntimeError:

	# if event loop dose NOT exist
	print( 'After main function, Event loop dose not exist' + '\n' )

print( 'Time used for the whole program was: {}s'.format( time.time() - programStartTime ) )
