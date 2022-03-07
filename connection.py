import weakref
import psycopg2


_GLOBAL_POSTGRE_CONNECTION = None
_global_connections = dict()


def init_postgre_connection(dbname, user, password, host, port):
    # reset all connections first
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
