import mysql.connector


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
        ''' if self.cnx is not None:
            print("Connection Established")
        else:
            print("Connection was not Established")'''
        self.cursor = self.cnx.cursor()

    def user_login(self, acc_name, acc_pw):
        query = "SELECT aethor_account_password FROM aethor_users WHERE aethor_account_name = %s"
        self.cursor.execute(query, (acc_name, ))
        for(aethor_account_password, ) in self.cursor:
            if acc_pw == aethor_account_password:
                return True
            else:
                return False
        return False

    def close(self):
        self.cursor.close()
        self.cnx.close()
