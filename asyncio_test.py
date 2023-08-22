import asyncio 
import time
import warnings


async def loop():
    for i in range( 5 ):
        print( i )
        await asyncio.sleep(1)

async def runSomething( n ):
    print( 'Run', n )

    await asyncio.sleep( 3 )

    print( 'Done', n )

async def main():

    # result = await runWithResult( 3 )
    # print(result)

    task1 = asyncio.create_task( loop() )
    task2 = asyncio.create_task( runSomething( 1 ) )
    
    await asyncio.sleep(1)
    await runSomething( 2 )

    await asyncio.gather( task1, task2 )

if __name__ == '__main__':
    asyncio.run( main() )