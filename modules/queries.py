"""
This file is a container for all queries that 
will be executed in the database manager 
It's just to write a clean database adapter 
"""


class Container:  # where all queries are stored as strings

    def __init__(self):
        # run once to create a table to store clients accounts for the server
        self.create_table = 'CREATE TABLE users(username TEXT UNIQUE, password TEXT, ip TEXT)'
        # creating an account with username and hashed and salted password
        self.create_account = 'INSERT INTO users(username, password, ip) VALUES(?, ?, ?)'
        # deleting an account if the user is logged in and entered the command to do that
        self.delete_account = 'DELETE FROM users WHERE username = ?'
        # deleting the table, the server will be formatted
        self.delete_table = 'DELETE FROM users'
        # select all username that corresponds to a variable
        # kind of verification test for the register process
        self.fetch_username = 'SELECT username FROM users WHERE username = ?'
        # select ip address corresponding to an username to use PM method
        self.fetch_ip = 'SELECT ip FROM users WHERE username = ?'
        # select username and password to validate identification test
        self.fetch_account = 'SELECT username, password FROM users WHERE username = ? AND password = ?'
