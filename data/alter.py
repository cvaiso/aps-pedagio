import database as db

#change the database
def Alter(object, table):

    #print("") 
    attributes = [attr for attr in dir(object) if not callable(getattr(object, attr)) and not attr.startswith("__")]

    # dinamic string SQL
    value_collumns = ', '.join([f'"{attr}" = %s' for attr in attributes])

    query = f"""
        UPDATE "{table}"
        SET {value_collumns}
        WHERE "{attributes[0]}" = %s
    """

    # attributes values from object
    obj_value = [getattr(object, attribute) for attribute in attributes]

    # Adiciona o valor do ID como último parâmetro
    #obj_value.append(getattr(object, attributes[0]))

    with db.conn, db.conn.cursor() as cursor:
        cursor.execute(query, obj_value)

    count = db.cur.rowcount