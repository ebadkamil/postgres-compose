from connection import PostGreConnection, init_postgre_connection


class DataBaseProxy:
    _db = PostGreConnection()

    def __init__(self):
        self._cursor = self._db.cursor()

    def execute(self, query):
        self._cursor.execute(query)

    def fetchall(self):
        return self._cursor.fetchall()

    def close(self):
        self._cursor.close()
        DataBaseProxy.__dict__["_db"].close()


if __name__ == "__main__":
    connection = init_postgre_connection(
        "dvdrental", "postgres", "postgres", "localhost", "5432"
    )
    c = DataBaseProxy()
    c.execute("SELECT first_name, last_name FROM customer")
    print(c.fetchall())
    c.close()
