
from sqlite3 import connect
from datetime import datetime


#con = connect('mydatabase.db')


class DBHelper:

    def __init__(self):
        #super(DBHelper, self).__init__()

        self.connection = connect('test.db')
        self.__create_table_user__()

    def __create_table_user__(self):
        cur = self.connection.cursor()

        cur.execute("""
            CREATE TABLE if not exists user(
                id integer PRIMARY KEY AUTOINCREMENT,
                username nvarchar(100),
                password nvarchar(100),
                regtime txt 
            );
        """)

        self.connection.commit()

        del cur

    def add_user(self, username: str, password: str):
        cur = self.connection.cursor()

        cur.execute(f"""
            insert into user (username, password, regtime)
            VALUES('{username}', '{password}', datetime('now', 'localtime'));
        """)

        self.connection.commit()

    def delete_user(self, _id: int):
        cur = self.connection.cursor()

        cur.execute(f"""
            delete from user where id == {_id};
        """)

        self.connection.commit()

    def update_user(self, username: str, password: str):
        cur = self.connection.cursor()

        cur.execute(f"""
            UPDATE user
            set password = '{password}'
            WHERE username == '{username}';
        """)

        self.connection.commit()



def main():

    dbhelper = DBHelper()
    dbhelper.add_user("hamid", "1234")
    #dbhelper.delete_user(1)
    dbhelper.update_user("reza", "123456")

if __name__ == "__main__":
    main()