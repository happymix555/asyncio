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

