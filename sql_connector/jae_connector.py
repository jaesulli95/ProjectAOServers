import mysql.connector
import MySQLdb # need to use this library, reason: speed


class aedb_connector:

    def __init__(self, host, user, pw, database, port):
        self.config = {
            'user': user,
            'password': pw,
            'host': host,
            'database': database,
            'port': port
        }
        self.cnx = None
        self.cursor = None

    def connect(self):
        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor()

    def user_login(self, acc_name, acc_pw):
        query = "SELECT aethor_password, aethor_account_id FROM aethor_accounts WHERE aethor_username = %s"
        self.cursor.execute(query, (acc_name, ))
        for(aethor_account_password, aethor_account_id, ) in self.cursor:
            if acc_pw == aethor_account_password:
                return (True, aethor_account_id)
            else:
                return (False, -1)
        return (False, -1)

    def getAccountCharacters(self, account_id):
        query = "SELECT * FROM aethor_characters WHERE aethor_account_id = %s"
        characters = []
        self.cursor.execute(query, (account_id, ))
        for( acid, aaid, name, ac, armor, ) in self.cursor:
            characters.append({'character_id':acid, 'name': name, 'aethor_class': ac, 'armor': armor})
        return characters


    def close(self):
        self.cursor.close()
        self.cnx.close()
