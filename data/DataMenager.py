import database as db
import inspect

class DataMenager:
# no attributes

    def Delete(classe, id):
        signature = inspect.signature(classe)
        parameters = list(signature.parameters)

        primary_key = parameters[0]

        query = f'DELETE FROM "{classe.__name__.upper()}" WHERE "{primary_key}" = %s'

        with db.conn, db.conn.cursor() as cursor:
            cursor.execute(query, (id,))

        count = db.cur.rowcount

        if count > 0:
            print(f'{classe.__name__} deletado com sucesso!')


    def Insert(object, tabela):
        atributes = [attr for attr in dir(object) if not callable(getattr(object, attr)) and not attr.startswith("__")]

        # dinamic string SQL 
        colunas = ', '.join(atributes)
        valores = ', '.join(['%s'] * len(atributes))

        query = f"""
            INSERT INTO "{tabela}" ({colunas}) 
            VALUES ({valores})
        """

        # attribute values from object
        object_value = [getattr(object, attribute) for attribute in atributes]

        with db.conn, db.conn.cursor() as cursor:
            cursor.execute(query, object_value)

        count = db.cur.rowcount

    def View(classe):
        
        query = f'SELECT* FROM "{classe.__name__.upper()}"'
        with db.conn, db.conn.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            
        return results