import psycopg2

def connect_to_database():
    try:
        conn = psycopg2.connect(
            database="pedagio",
            user="kariny",
            host="127.0.0.1",
            password="kakazinha10",
            port=5432
        )
        print("Conexão com o banco de dados estabelecida com sucesso.")
        return conn
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None

def close_connection(conn, cur):
    try:
        cur.close()
        conn.close()
        print("Conexão com o banco de dados fechada.")
    except psycopg2.Error as e:
        print("Erro ao fechar a conexão com o banco de dados:", e)