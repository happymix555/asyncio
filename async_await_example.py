import asyncio
import time

'''

This code is used to demonstrate how to use async with await 
to create a coroutine function and wait for it to finished performing their task
before we move on to do something else

This code only demonstrate how we can use 'await' to pause coroutine function 
and wait for long running IO task to finished before do other things in queue

'''

# create coroutine function to simulate long process with asyncio.sleep
async def myPrint( numToPrintInt: int ):
	
	# print to inform user that we are in this specific myPrint function
	print( 'We are currently in myPrint number {}'.format( numToPrintInt ) )
	
	# sleep for 3 second to simulate a long running process
	await asyncio.sleep( 3 )
	
	# print to inform that this long process is completed
	print( 'myPrint number {} is done!'.format( numToPrintInt ) )

# create main function to host all coroutine function
# this will be used as an entry point for our event loop
async def main():
	
	# create timer, startTime to keep time used in this program
	startTime = time.time()

	# print to inform that we are in main function
	print( 'Starting main function' )
	
	# call myPrint function with 'await' keyword with number 1 to simulate the first long running process
	await asyncio.create_task( myPrint( 1 ) )
	
	# call myPrint function with 'await' keyword with number 2 to simulate the second long running process
	await asyncio.create_task( myPrint( 2 ) )
	
	# call myPrint function with 'await' keyword with number 3 to simulate the third long running process
	await asyncio.create_task( myPrint( 3 ) )

	# print to inform that all of the long running process is done
	# and we are currently resume to do something else in queue
	print( 'Long running process finished and ending main function' )

	# print time we spent for running the program
	print( 'This program took {}s to run'.format( time.time() - startTime ) )

# create an entry point to our event loop and run the program
asyncio.run( main() )