import weakref

import psycopg2

_GLOBAL_POSTGRE_CONNECTION = None
_global_connections = dict()


def init_postgre_connection(dbname, user, password, host, port):
    global _GLOBAL_POSTGRE_CONNECTION
    _GLOBAL_POSTGRE_CONNECTION = None

    commit_and_close_connections()
    connection = psycopg2.connect(
        dbname=dbname, user=user, password=password, host=host, port=port
    )

    _GLOBAL_POSTGRE_CONNECTION = connection
    return connection


def postgre_connection():
    return _GLOBAL_POSTGRE_CONNECTION


def commit_and_close_connections():
    for connections in _global_connections.values():
        for ref in connections:
            c = ref()
            if c is not None:
                c.close()


class MetaPostGreConnection(type):
    def __call__(cls, *args, **kw):
        instance = super().__call__(*args, **kw)
        name = cls.__name__
        if name not in _global_connections:
            _global_connections[name] = []
        _global_connections[name].append(weakref.ref(instance))
        return instance


class PostGreConnection(metaclass=MetaPostGreConnection):
    def __init__(self):
        self._db = None

    def __get__(self, instance, instance_type):
        if self._db is None:
            self._db = postgre_connection()
        return self._db

    def close(self):
        if self._db is not None:
            self._db.commit()
            self._db.close()
        self._db = None


class Executor:
    _db = PostGreConnection()

    def __init__(self):
        self._cursor = self._db.cursor()

    def execute(self, query):
        self._cursor.execute(query)

    def fetchall(self):
        return self._cursor.fetchall()

    def close(self):
        self._cursor.close()


if __name__ == "__main__":
    connection = init_postgre_connection(
        "dvdrental", "postgres", "postgres", "localhost", "5432"
    )
    c = Executor()
    c.execute("SELECT first_name, last_name FROM customer")
    print(c.fetchall())

    commit_and_close_connections()
