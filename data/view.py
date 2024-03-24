import database as db

def Visualizar(classe):
    
    query = f'SELECT* FROM "{classe.__name__.upper()}"'
    with db.conn, db.conn.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
        
    return results
    