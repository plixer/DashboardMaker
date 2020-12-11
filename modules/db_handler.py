import psycopg2


class DB_handler:
    ## Handles the database connection
    def __init__(self,db_name,user,password,scrut_ip):
        self.db_name = db_name
        self.db_user = user
        self.db_password = password
        self.db_host = scrut_ip

    #method used to insert into DB

    def open_connection(self):
        self.conn = psycopg2.connect("dbname={} user={} password={} host={}".format(self.db_name,self.db_user,self.db_password,self.db_host))
        self.cur = self.conn.cursor()
        return self.cur

    def execute_query(self, query):
        self.cur.execute(query)
        try:
            record = [r[0] for r in self.cur.fetchall()]
            
        except:
            record = 'nothing_returned'
        self.conn.commit()
        return(record)

    def close_connection(self):
        self.cur.close()
        self.conn.close()
        print('disconnected from DB')


    def test_connection(self):

        try:
            self.conn = psycopg2.connect("dbname={} user={} password={} host={}".format(self.db_name,self.db_user,self.db_password,self.db_host))
            print('Connection has been Succesful')
            return True
        except psycopg2.Error as err:
            print("Error: ", err)
            return False
        
        self.conn.close()
