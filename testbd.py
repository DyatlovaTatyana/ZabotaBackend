import psycopg2
from psycopg2.extras import DictCursor
conn = psycopg2.connect(
    host="80.90.188.41",
    user="esia-modul-dev-user",
    password="hg",
    port=5432,
    dbname="esia-modul-dev"
)

if conn:
    print("Подключение установлено")

cursor = conn.cursor(cursor_factory=DictCursor)
cursor.execute("SELECT * FROM active_long WHERE registration_type_id = 1")
result = cursor.fetchall()
first_active_id = result[0]["id"]
print(first_active_id)

# for active in result:
#     print(active["id"])