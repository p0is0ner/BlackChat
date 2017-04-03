# file for all queries serialized as strings
# need to be imported in the db-manager


class Queries:
    def __init__(self):
        # run once, for creating a table to store users data
        self.create_table = 'CREATE TABLE IF NOT EXISTS users(' \
                            'username TEXT UNIQUE, password TEXT, unread_data TEXT)'

        # change username if user wants new one
        self.update_username = 'UPDATE users SET username = %s WHERE username = %s'

        # delete an account if the user entered the needed command
        self.delete_account = 'DELETE FROM users WHERE username = %s'

        # account verification needed for login process
        self.login_query = 'SELECT * FROM users WHERE username = %s'

        # account creation process used for the register method
        self.register_process = 'INSERT INTO users(username, password) VALUES (%s, %s)'

