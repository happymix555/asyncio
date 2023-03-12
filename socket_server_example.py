import socket

'''
We will use 'with' statement instead of 'try' and 'finally' 
to close properly close the connection 

this file create a socket server without the help of asyncio
this will demonstrate how to NOT properly handle multiple client with socket

'''

# create server socket
# socket.AF_INET = select IPv4 as the address type --> host name and port number 
# socket.SOCK_STREAM = set to use TCP protocol for communication
with socket.socket( socket.AF_INET, socket.SOCK_STREAM ) as serverSocket:
    # enable us to use the same port number after restart the server
    serverSocket.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )

    # specify the address for our server
    addressAndPortTuple = ( '127.0.0.1', 8000 )
    # binding address to our server so we can talk to it  
    serverSocket.bind( addressAndPortTuple )

    # listen for connection from user
    print( 'Start listening for client' )
    serverSocket.listen()

    # create list to store multiple client address and their connection
    clientAddressToConnectionDict = {}
    
    # loop trying accept every incoming connection
    while True:
        # get connection and client address when client connect to our server
        # our program will stuck and wait at this line
        # until have a connection from the client
        print( 'Waiting for a connection from client' )
        connection, clientAddress = serverSocket.accept()

        # inform that we already have connection
        print( f'We have connection from { clientAddress }' )

        # store client address and it's connection in dict
        clientAddressToConnectionDict[ clientAddress ] = connection    
        
        # loop get each client address and it's connection
        for clientAddress, connection in clientAddressToConnectionDict.items():

            # inform user we are waiting for message from client
            print( 'Waiting for message from client at {}'.format( clientAddress ) )

            # get message from connection
            # we get 1024 bytes of data at a time
            messageByte = connection.recv( 1024 )

            # print client address and it's message 
            print( '{} from client name: {} \n'.format( messageByte.decode(), clientAddress ) )

            # send that message back to clients 
            connection.send( messageByte )



