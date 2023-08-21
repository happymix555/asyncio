import asyncio

# create coroutine that will generate error at some point
async def simulateErrorCoroutine():
    
    # sleep to simulate some work
    await asyncio.sleep( 2 )

    # create fake list but it is actually a number
    listButActuallyNum = 0

    # make an error
    # try to access index of list 
    # but it is actually a number so this will create an error 
    try:
        mockVariable = listButActuallyNum[ 0 ]
    except Exception as e:
        print( 'Exception: ', e )  

async def main():
    
    # create task from coroutine
    simulateErrorTask = asyncio.create_task( simulateErrorCoroutine(), name='simulate error task' )
    print( asyncio.all_tasks() )

    # await to ensure execution of task
    await simulateErrorTask

    # print status of all task in an event loop
    print( asyncio.all_tasks() )

asyncio.run( main() )
