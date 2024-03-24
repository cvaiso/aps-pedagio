import database as db
import inspect

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