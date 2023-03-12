import socket
import time

# create client socket
# socket.AF_INET --> using IPv4 address type
# socket.SOCK_STREAM --> using TCP as communication protocol
with socket.socket( socket.AF_INET, socket.SOCK_STREAM ) as clientSocket:
    # specify address and port of the server
    addressAndPortTuple = ( '127.0.0.1', 8000 )

    # inform user we are trying to connect
    print( 'Trying to connect to server...' )

    # make connection to server
    clientSocket.connect( addressAndPortTuple )

    # inform user we have connected successfully
    print( 'Connection is made successfully' )

    # loop keep getting in put from user
    while True:

        # inform user we need something to send to server
        userInputStr = input( 'Please type something so we can send it to server: ' )

        # send data to server in byte format
        clientSocket.sendall( bytes( userInputStr, 'utf-8' ) )

        # waiting for server to send our message back to us
        messageByte = clientSocket.recv( 1024 )

        # print message from server
        print( 'We got {} from the server'.format( messageByte.decode() ) )