import asyncio 
import time

'''
this program demonstrate how 'await' keyword change the running sequence of our program
from normal( line after line ) into event loop queue

'''

# create coroutine function 
async def myPrint( numToPrintInt: int ):
    # print to inform that we are in myPrint function
    print( 'We are current in myPrint: {}'.format( numToPrintInt ) )
    # # sleep for 3 seconds to simulate long running process
    # await asyncio.sleep( 3 )
    # # print to inform that the long running process of this coroutine function is done
    # print( 'long running process of myPrint: {} is done'.format( numToPrintInt ) )

# create coroutine function that have asyncio.crate_task() inside of it
async def myPrintAndAddTask( numToPrintInt: int ):
    # print to inform that we are in myPrintAndAddTask function
    print( 'We are current in myPrintAndAddTask: {}'.format( numToPrintInt ) )
    # add task( myPrint ) to event loop using asyncio.create_task()
    myPrintResult = asyncio.create_task( myPrint( numToPrintInt ) )
    # print to inform that we have finished adding task to event loop
    print( 'Task with number: {} added to event loop via myPrintAndAddTask function' )

# create main function to host all of out coroutine 
async def main():
    # print to inform that we are in main function
    print( 'We are in main function' )
    # add the first myPrintAndAddTask task to event loop
    firstMyPrintAndAddTask = asyncio.create_task( myPrintAndAddTask( 1 ) )
    # add the second myPrintAndAddTask task to event loop
    secondMyPrintAndAddTask = asyncio.create_task( myPrintAndAddTask( 2 ) )

    # begin to use 'await' keyword
    # our program will run line by line until this task
    # then it will switch to execute 

