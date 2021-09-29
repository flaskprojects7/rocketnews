from config import mysql


class User(object):

    @staticmethod
    def register(login, password, email, regdate, status) -> None:
        connection = mysql.get_db()
        cursor = connection.cursor() #создаем курсор
        sql_query = """
            insert into users (login, password, email, regdate, status) 
            values (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql_query, (login, password, email, regdate, status))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def login() -> None:
        pass