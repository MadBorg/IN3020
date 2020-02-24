import sqlite3

class DBmanager():
    tables = []
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cur = self.conn.cursor()

    def create_table(self, name, attributes):
        # init
        self.tables.append(name)
        query = "CREATE TABLE ? ("
        list_of_unpacked_attrs = [name]
        list_of_unpacked_attrs += [item for t in attributes for item in t]

        # Asumtions
        assert len(list_of_unpacked_attrs) == 1 + 2* len(attributes), "" + \
            f"len of list of unpacked attrs: {len(list_of_unpacked_attrs)} \n" + \
            f"number of questionmarks: {1 + 2* len(attributes)}"

        # attributes
        query += "\n"
        for _ in attributes[:-1]:
            query += " ? ?, \n" # name, datatype

        # last attr
        query + " ? ? \n);"
        with self.conn:  # With a context manager we dont need a commit
            self.cur.execute(query, list_of_unpacked_attrs)


    def close(self):
        self.conn.close()


if __name__ == "__main__":
    pass