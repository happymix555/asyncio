''' Helper to create SQL table from CreativeDB assertion
'''

import sqlite3

if __name__ == '__main__':

    # connect to database
    connection = sqlite3.connect( 'test.db' )

    # create mock table
    connection.execute( """ CREATE TABLE IF NOT EXISTS Book (
                            id integer PRIMARY KEY,
                            name text NOT NULL,
                            authorName text NOT NULL
                        ); """ )

    # insert mock data to table
    connection.execute( "INSERT INTO Book ( id, name, authorName ) \
                        VALUES ( 1, 'ABC', 'happymix' );" )
    
    # insert mock data to table
    connection.execute( "INSERT INTO Book ( id, name, authorName ) \
                        VALUES ( 1, 'ABC', 'happymix' );" )
