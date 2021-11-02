import mysql.connector as mc


class OverDB:

    def __init__(self, params, create=False):

        self.params = params

        self.db = self.connect()
        self.cursor = self.db.cursor()
        create and self.create()

    def connect(self):
        print(f'Connecting to {self.params["db"]} database at {self.params["host"]}')
        return mc.connect(
            host=self.params["host"],
            user=self.params["user"],
            password=self.params["pw"],
            database=self.params["db"]
        )

    def create(self):
        self.cursor.execute("CREATE DATABASE OverGG")

    def query(self, query, verbose=False):
        verbose and print(f"QUERY: '{query}'")

        self.cursor.execute(query)
        result = self.cursor.fetchall()

        verbose and print(result)

        return result
