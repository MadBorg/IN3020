import sqlite3

class DBM():
    tables = []
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cur = self.conn.cursor()

    def create_table(self, name, attributes, primary_key=None, references=None, IF_NOT_EXISTS = True):
        """
        attributes:
            ((name, datatype, null, primary_key, default, unique)<str, str, <optional, str>, <optional, bool>, <optional, any>, <optional, bool>>)<itr>

        references:
            ((table, key, forign_key, on delete, on update)<str, str, str, <optional, bool>, <optional, bool>>)<itr>


        """

        # init
        self.tables.append(name)
        if IF_NOT_EXISTS:
            query = f"CREATE TABLE IF NOT EXISTS {name} ("
        else:
            query = f"CREATE TABLE {name} ("


        # Asumtions

        # attributes
        query += "\n"
        for attr in attributes[:-1]:
            query += _attr(attr, last=False)
        query += _attr(attributes[-1], last=True)       
        
        # Primary key
        if primary_key:
            query += ",\n"
            query += " PRIMARY KEY"
            if type(primary_key) is tuple or type(primary_key) is list:
                tmp = tuple(primary_key)
                query += f" {tmp}"
            elif type(primary_key) is str:
                query += f" ({primary_key})"
            else:
                raise TypeError("primary key is not list, tuple or dict")

        # References
        if references:
            query += ",\n"
            for reference in references:
                # table, key, forign_key
                table, key, forign_key = reference["table"], reference["key"], reference["forign_key"]
                query += f" FOREIGN KEY ({key})\n" + \
                    f"  REFERENCES {table} ({forign_key})\n"
                # on del
                if "on_delete" in reference:
                    on_del = reference["on_delete"]
                    assert type(on_del) is str, "on del is not str"
                    query += f"      ON DELETE {on_del}\n"
                # on update
                if "on_update" in reference:
                    on_upt = reference["on_update"]
                    assert type(on_upt) is str, "on update is not str"
                    query += f"     ON UPDATE {on_upt}"
        
        
        # Ending query
        query += ")"

        print(query)
        with self.conn:  # With a context manager we don't need a commit
            self.cur.execute(query)


    def close(self):
        self.conn.close()


def _attr(attr, last = False):
    q = "" # query
    attr_name, attr_datatype = attr["name"], attr["datatype"]
    q += f"{attr_name} {attr_datatype}"

    if "primary_key" in attr:
        attr_primary_key = attr["primary_key"]
        assert type(attr_primary_key) is bool, "primary_key is not boolean"
        if attr_primary_key:
            q += " PRIMARY KEY"
    else:
        if "null" in attr:
            null = attr["null"]
            assert type(null) is bool, "null is not bool"
            if not null:
                q += " NOT NULL"
        if "default" in attr:
            default = attr["default"]
            assert type(default) is str, "default is not str"
            q += f" DEFAULT {default} "
        if "unique" in attr:
            unique = attr[unique]
            assert type(unique) is bool
            if unique:
                q += " UNIQUE"
    # Ending attr
    if not last:
        q += ", \n"
    elif last:
        q += ""
    return q

if __name__ == "__main__":
    pass