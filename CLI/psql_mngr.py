# postgresql database interaction manager
# this file is wrote using class model with several methods
# used by the server to perform queries and inserts statements with the database

import psycopg2
import queries


class DatabaseAdapter:
    """
    For every methods we create the cursor and the connection object and once the interaction
    is finished we close the cursor and close the connection
    """
    def __init__(self):
        """
        Main method, we convert all queries imported from the queries.py file in instances
        when a function need a query it calls directly to the __init__ method and receive it
        """
        self.instance = queries.Queries()
        self.login_query = self.instance.login_query
        self.update_username = self.instance.update_username
        self.create_table = self.instance.create_table
        self.delete_account = self.instance.delete_account
        self.register_process = self.instance.register_process

    def login_user(self, username, password):
        """
        This function is used to check if the account already 
        exists and then allowing access to the user
        :param username: 
        :param password: 
        :return: 
        """
        try:
            connection = psycopg2.connect(dbname='blackChat', user='postgres', password='admin', host='localhost')
        except psycopg2.Error:
            print('[!] Error during login process for user: ' + username + '\n')
            print('Unable to connect to PostgreSQL database ... \n')

        cursor = connection.cursor()
        cursor.execute(self.login_query, (username, password))
        lock = cursor.fetchall()

        if lock[0][0] == username and lock[1][1] == password:  # checking if the account exists
            cursor.close()  # closing cursor
            connection.close()  # closing connection
            return True  # returning prefix to the server so it can accept the client
        else:
            cursor.close()  # closing cursor
            connection.close()  # closing connection
            return False  # login process failed

    def register_user(self, username, password):
        """
        This method checks if the username already exists, 
        if so it breaks and return an error prefix
        And then if not it insert the rows in the database
        :param username: 
        :param password: 
        :return: 
        """
        try:
            connection = psycopg2.connect(dbname='blackChat', user='postgres', password='admin', host='localhost')
        except psycopg2.Error:
            print('[*] Error during registration process for user: ', username + '\n')
            print('Unable to connect to the database server ... \n')

        cursor = connection.cursor()
        try:
            cursor.execute(self.register_process, (username, password))
        except psycopg2.IntegrityError:
            return False

        cursor.close()
        connection.close()
        return True

    def update_username(self, username):
        """
        this method just finds the username in the database and update the row then it quit
        :param username: 
        :return: 
        """
        try:
            connection = psycopg2.connect(dbname='blackChat', user='postgres', password='admin', host='localhost')
        except psycopg2.Error:
            print('[*] Error during username update process for user: ', username + '\n')
            print('Unable to connect to the database server ... \n')

        cursor = connection.cursor()
        try:
            cursor.execute(self.update_username, (username, ))
            cursor.close()
            connection.close()
            return True

        except psycopg2.Error:
            cursor.close()
            connection.close()
            return False

    def delete_account(self, username, password):
        """
        deleting an account if requested by the owner using a specific prefix
        :param username: 
        :param password: 
        :return: 
        """
        try:
            connection = psycopg2.connect(dbname='blackChat', user='postgres', password='admin', host='localhost')
        except psycopg2.Error:
            print('[*] Error during account deleting process for user: ', username + '\n')
            print('Unable to connect to the database server ... \n')

        cursor = connection.cursor()

        try:
            cursor.execute(self.delete_account, (username, ))
            cursor.close()
            connection.close()
            return True
        except psycopg2.Error:
            return False

    def create_table(self):
        try:
            connection = psycopg2.connect(dbname='blackChat', user='postgres', password='admin', host='localhost')
        except psycopg2.Error:
            print('[*] Error during table creating process \n')
            print('Unable to connect to the database server ... \n')

        cursor = connection.cursor()

        try:
            cursor.execute(self.create_table)
            cursor.close()
            connection.close()
            return True
        except psycopg2.Error:
            cursor.close()
            connection.close()
            return False
