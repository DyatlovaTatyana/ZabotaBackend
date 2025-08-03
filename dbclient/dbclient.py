from psycopg import connect, ProgrammingError
from psycopg.rows import dict_row


class PgClient:
    def __init__(self, host, port, user, password, db_name):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db_name = db_name
        self.connection = None
        self.connect()

    def connect(self) -> None:
        try:
            self.connection = connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                dbname=self.db_name
            )
            self.connection.autocommit = True

        except Exception as e:
            raise ConnectionError(e)

    def disconnect(self):
        if self.connection:
            self.connection.close()
        self.connection = None

    def execute(self, query: str) -> list[dict] | None:
        try:
            with self.connection.cursor(row_factory=dict_row) as cursor:
                cursor.execute(query)
                try:
                    result = cursor.fetchall()
                except ProgrammingError:
                    result = None
            return result
        except Exception as e:
            raise ConnectionError(e)

    def fetchall(self, query: str) -> list[dict]:
        result = self.execute(query=query)
        return result

    def fetchone(self, query: str) -> dict | None:
        result = self.execute(query=query)
        if result:
            return result[0]
        return None





    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
