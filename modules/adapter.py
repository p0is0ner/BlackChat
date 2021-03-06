"""
this file contains the class for the database manager.
It executes the queries and return the results, by this way
the server script only needs to treat them.
"""

import sqlite3  # database related stuff like cursor and connection
from queries import Container  # queries files

container = Container()  # making a local instance of the needed class


class Adapter:
    def __init__(self):
        # query to create an users table to store accounts
        self.create_table = container.create_table
        # adding an account to the table
        self.create_account = container.create_account
        # deleting an account if the user is logged in and entered the required command
        # or if the account isn't used for 48hrs
        self.delete_account = container.delete_account
        # deleting the table, run this query in the server shell,
        #  the server will abort and delete all files related to it
        self.delete_table = container.delete_table
        # fetching ip address
        self.fetch_ip = container.fetch_ip
        # fetching account data
        self.fetch_account = container.fetch_account
        # list to return username and password in same container
        self._account_data = []
        # username fetching
        self.fetch_username = container.fetch_username
        # variable containing database name
        self.database = 'blackchat.db'
        # instance of the conn
        self.conn = sqlite3.connect(self.database)
        # instance of the cursor
        self.cursor = self.conn.cursor()

    def close_conn(self):
        """
        this function will be called in all others to close the connection after the
        execution of the query
        :return: 
        """
        self.cursor.close()
        self.conn.close()

    def create_table(self):
        """
        this query will be executed automatically every time the server.py is executed 
        the table will be created if it doesnt already exist
        :return: True or False values 
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        try:
            cursor.execute(self.create_table)
            conn.commit()
            self.close_conn()
            return True
        except sqlite3.OperationalError:
            self.close_conn()
            return False

    def create_account(self, username, password, ip):
        """
        This query is executed to create an account and store it in the table if the 
        user entered the required command in the client shell 
        :return: True or False values
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        try:
            cursor.execute(self.create_account, (username, password, ip))
            conn.commit()
            self.close_conn()
            return True
        except sqlite3.OperationalError:
            self.close_conn()
            return False

    def delete_account(self, username):
        """
        This query will delete the account related to the username provided in args
        :param username: 
        :return: 
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        try:
            cursor.execute(self.delete_account, (username,))
            conn.commit()
            self.close_conn()
            return True
        except sqlite3.OperationalError:
            self.close_conn()
            return False

    def delete_table(self):
        """
        This query will delete the table
        it will be executed when the user wants 
        to delete a server set up (all files related to it)
        after he provided the command and the password for BlackChat administrator 
        server will abort too
        :return: 
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        try:
            cursor.execute(self.delete_table)
            conn.commit()
            self.close_conn()
            return True
        except sqlite3.OperationalError:
            self.close_conn()
            return False

    def ip_fetch(self, username):
        """
        IP fetching in function of a given username
        used for private messaging 
        :param username: 
        :return: 
        """

        try:
            self.cursor.execute(self.fetch_ip, (username, ))  # as tuple
            ip = self.cursor.fetchall()[0][0]  # returning ip without dictionary or list form, as simple string
            # using [0] * 2 to perform socket.send()
            self.close_conn()
            return ip

        except sqlite3.OperationalError:
            self.close_conn()
            return False  # this shouldn't happen but anyway if there isn't an ip for an user...

    def fetch_account(self, username, password):
        """
        this returns True if the account exists and the fetched data is equal to the provided data in params
        :param username: as string (original)
        :param password: hashed and salted password (never use plain text performing (insecure))
        :return: 
        """
        try:
            self.cursor.execute(self.fetch_account, (username, password))
            fetched_data = self.cursor.fetchall()
            self._account_data.append(fetched_data[0])
            self._account_data.append(fetched_data[1])
            self.close_conn()
            return self._account_data
        except sqlite3.OperationalError:
            self.close_conn()
            return False
    
    def fetch_username(self, username):
        """
        fetch the username and returns it as a single string to execute == test with username provided by user
        :param username: 
        :return: 
        """
        try:
            self.cursor.execute(self.fetch_username, (username, ))
            fetched_data = self.cursor.fetchall()
            fetched_username = fetched_data[0]
            self.close_conn()
            return fetched_username
        except sqlite3.OperationalError:
            self.close_conn()
            return False
