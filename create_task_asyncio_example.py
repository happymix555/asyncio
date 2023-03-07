import asyncio 
import time

'''
asyncio.create_task

asyncio.create_task is used when we want to run coroutine function concurrently while waiting for 
another long running IO task.

asyncio.create_task will return the task object.

we use task object to with await to indicate where in the code should we really wait for the result 
of the long running task before moving on for another task.

the below code demonstrate on how to use asyncio.create_task
'''

# create coroutine function to simulate long process with asyncio.sleep
async def myPrint( numToPrint: int ):
    # sleep for 3 second to simulate a long running process
    await asyncio.sleep( 3 )
    # print to inform that this long process is completed
    print( 'myPrint number {} is done!'.format( numToPrint ) )

# create main function to host all coroutine function
# this will be used as an entry point for our event loop
async def main():
    # create timer, startTime to keep time used in this program
    startTime = time.time()

    # print to inform that we are in main function
    print( 'Staring main function' )
    # call myPrint function with number 1 to simulate the first long running process
    firstLongRunningTask = asyncio.create_task( myPrint( 1 ) )
    # call myPrint function with number 2 to simulate the second long running process
    secondLongRunningTask = asyncio.create_task( myPrint( 2 ) )
    # call myPrint function with number 3 to simulate the third long running process
    thirdLongRunningTask = asyncio.create_task( myPrint( 3 ) )

    # print to inform that we have already start the long running process in the background
    # at this point we can perform other task concurrently while waiting for the long running
    # task to be done
    print( 'We are already start the long running process concurrently! with this print statement' )

    # at this point of code we are really want to wait for the result of 
    # the long running task before moving on to do other task
    await firstLongRunningTask
    await secondLongRunningTask
    await thirdLongRunningTask

    # print to inform that the main function in finished
    print( 'Ending main function' )

    # print time we spent for running the program
    print( 'This program took {}s to run'.format( time.time() - startTime ) )

# create an entry point to our event loop
asyncio.run( main() )

