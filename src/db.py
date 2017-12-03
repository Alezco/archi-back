import MySQLdb


def execute(query):
    connector = MySQLdb.connect(user='root', password='password', host='127.0.0.1', database='archi')
    cursor = connector.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]
    for result in res:
        json_data.append(dict(zip(row_headers, result)))
    cursor.close()
    connector.close()
    return json_data


def insert(query):
    connector = MySQLdb.connect(user='root', password='password', host='127.0.0.1', database='archi')
    cursor = connector.cursor()
    cursor.execute(query)
    last_id = cursor.lastrowid
    cursor.close()
    connector.commit()
    connector.close()
    return last_id
