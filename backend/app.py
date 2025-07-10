import psycopg2

def app(environ, start_response):
    conn = psycopg2.connect(
        host="db",
        database="mydb",
        user="postgres",
        password="password"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders;")
    items = cursor.fetchall()
    cursor.close()
    conn.close()

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [f"<h1>Database Content:</h1><ul>{''.join(f'<li>{item}</li>' for item in items)}</ul>".encode()]
