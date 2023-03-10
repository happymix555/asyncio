import socket

# create server socket
# socket.AF_INET = type of address --> host name and port number 
# socket.SOCK_STREAM = set to use TCP protocol for communication
serverSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# enable us to use the same port number after restart the server
serverSocket.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )

# specify the address for our server
address = ( '127.0.0.1', 8000 )
# binding address to our server so we can talk to it  
serverSocket.bind( address )

# listen for connection from user
serverSocket.listen()

# get connection and client address when client connect to our server
connection, clientAddress = serverSocket.accept()

# inform that we already have connection
print( f'We have connection from { clientAddress }' )
