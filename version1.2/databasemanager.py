import psycopg2
import psycopg2.extras

host = "localhost"
database = "usuarios"
username = "postgres"
pwd = "101213K"
port_id = "5432"

class DatabaseManager:
    def __init__(self):
        # to avoid errors if db not start
        self.conn = None
        self.cur = None
        self.memory_db = list()
    def inicializar_database(self):
        try:
            self.conn = psycopg2.connect(host=host, dbname =database, user=username, password=pwd, port=port_id )
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            create_script = ''' CREATE TABLE IF NOT EXISTS users (
                                    user_id   INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                                    email     VARCHAR(255) NOT NULL,
                                    password  VARCHAR(255) NOT NULL) '''
            self.cur.execute(create_script)
            self.conn.commit()
        except Exception as error:
            print(error)
        finally:
            if self.cur is not None:
                self.cur.close()
            if self.conn is not None:
                self.conn.close()

    def insert_into_table(self, a=str, b=str):
        try:
            self.conn = psycopg2.connect(host=host, dbname=database, user=username, password=pwd, port=port_id)
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            insert_script = ''' INSERT INTO users (email, password) VALUES (%s, %s)'''
            insert_values = (a, b)
            print('valores inseridos na base de dados')
            self.cur.execute(insert_script, insert_values)
            self.conn.commit()
        except Exception as error:
            print(error)
        finally:
            if self.cur is not None:
               self.cur.close()
            if self.conn is not None:
                self.conn.close()

    def show_all_data(self):
        try:
            self.conn = psycopg2.connect(host=host, dbname=database, user=username, password=pwd, port=port_id)
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            self.cur.execute('SELECT * FROM USERS')

            user_fetch_data = self.cur.fetchall()
            if len(user_fetch_data) > 0:
                return user_fetch_data
            elif len(user_fetch_data) <= 0:
                return False

            self.conn.commit()
        except Exception as error:
            print(error)
        finally:
            if self.cur is not None:
               self.cur.close()
            if self.conn is not None:
                self.conn.close()





