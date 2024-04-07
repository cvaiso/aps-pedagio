from data.database import connect_to_database

class LoginController:
    @staticmethod
    def login(username, password):
        conn = connect_to_database()  # Alterando para uma conexão local
        query = "SELECT * FROM \"Admin\" WHERE email = %s AND password = %s"
        with conn.cursor() as cursor:
            cursor.execute(query, (username, password))
            admin = cursor.fetchone()

        if admin:
            return True
        else:
            return False

