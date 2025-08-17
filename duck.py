import duckdb
import os


class DuckDB:
    def __init__(self, duckdb_file):
        self.duckdb_file = duckdb_file
        self.conn = None

    def connect_database(self):
        if not os.path.exists(self.duckdb_file):
            raise FileNotFoundError(f"DuckDB file not found: {self.duckdb_file}")

        self.conn = duckdb.connect(self.duckdb_file)
        print(f"Connected to DuckDB: {self.duckdb_file}")
        return self.conn

    def fetch_all_tables(self):
        tables = self.conn.execute("select * from information_schema.tables")

        header = [col[0] for col in tables.description]
        print("header:", header)
        rows = tables.fetchall()
        print("rows:", rows)
        return header, rows

    def show_table_contents(self, table_name):
        if not self.conn:
            raise ConnectionError("Please connect to the database first.")

        rows = self.conn.execute(f"SELECT * FROM {table_name}").fetchall()
        for row in rows:
            print(row)

    def close_connection(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            print("DuckDB connection closed")
