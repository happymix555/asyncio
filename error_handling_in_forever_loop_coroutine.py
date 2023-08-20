''' This file is intended to demonstrate how AsyncIO event loop
    handle infinite loop coroutine which also have error inside it
    (eg. coroutine with a while loop and some parts of code that can 
    raise an error).

    This file will demonstrate 2 scenarios:
    1. Coroutine with:
        - while loop
        - error inside loop
    2. Coroutine with:
        - while loop
        - error inside loop
        - try, except statement to handle error
'''
import asyncio

def 

async def foreverLoopCoroutineWithError():
    ''' This coroutine have:
            - forever loop
            - error at some point in loop
    '''

    # create forever loop
    while True:

        # inform user we are in loop
        print( '[foreverLoopCoroutineWithError] we are in loop.' )
        
        # sleep to simulate sone work
        await asyncio.sleep( 1 )

        # create integer variable
        thisIsInteger = 0

        try:
            # simulating error by
            # access the first element of integer
            # this will raise TypeError
            thisIsInteger[ 0 ] = 0
        
        except TypeError:
            
            # inform user this error has been catch
            print( '[foreverLoopCoroutineWithError] TypeError has been catch' )


async def foreverLoopCoroutineWithErrorAndExceptionCatch():
    ''' This coroutine have:
            - forever loop
            - error at some point
            - try, except statement to catch an error
    '''

    # create forever loop
    while True:

        # inform user we are in loop
        print( '[foreverLoopCoroutineWithErrorAndExceptionCatch] we are in loop.' )

        # sleep to simulate some work
        await asyncio.sleep( 1 )

        # create integer variable
        thisIsInteger = 0

        try:
            
            # simulating error by
            # access the first element of integer
            # this will raise TypeError
            thisIsInteger[ 0 ] = 0
        except TypeError:
            
            # inform user this error has been catch
            print( '[foreverLoopCoroutineWithErrorAndExceptionCatch] TypeError has been catch' )

            # continue the loop
            continue
        
async def main():
    ''' This function act as an entry point of our program

        This function will:
            - crete task from coroutine
            - print all task in AsyncIO's event loop:
                - after create each task
                - after each await of each task
    '''

    # create forever loop with error task
    foreverLoopTaskWithError = asyncio.create_task ( foreverLoopCoroutineWithError(), name='foreverLoopTaskWithError' )

    print( '[main] after create foreverLoopTaskWithError' )
    print( '[main] task in event loop is: {}'.format( asyncio.all_tasks() ) )

    # create forever loop with error and error catcher task
    foreverLoopTaskWithErrorAndExceptionCatch = asyncio.create_task(
                                                                            foreverLoopCoroutineWithErrorAndExceptionCatch(), 
                                                                            name='foreverLoopTaskWithErrorAndExceptionCatch'
                                                                        )

    print( '[main] after create foreverLoopTaskWithErrorAndExceptionCatch' )
    print( '[main] task in event loop is: {}'.format( asyncio.all_tasks() ) )

    # explicitly command AsyncIO to run foreverLoopTaskWithError
    await foreverLoopTaskWithError
    print( '[main] await foreverLoopTaskWithError' )
    print( '[main] task in event loop is: {}'.format( asyncio.all_tasks() ) )

    # explicitly command AsyncIO to run foreverLoopTaskWithError
    await foreverLoopTaskWithErrorAndExceptionCatch
    print( '[main] await foreverLoopTaskWithErrorAndExceptionCatch' )
    print( '[main] task in event loop is: {}'.format( asyncio.all_tasks() ) )

    # inform use this program is ended
    print( '[main] This program is ended.' )

# run our program
asyncio.run( main() )

