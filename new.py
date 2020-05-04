import records

db = records.Database('sqlite:///myproject-dev.sqlite3')
conn = db.get_connection()

rows = conn.query('select * from menu')
result = rows.as_dict()

# print(result)
for row in result:
    print(row)
# print(type(rows))
# print(rows.as_dict()[1])
# for i in rows.as_dict():
#     print(i)

# print(records.isexception(db))
#
#
#
# print(rows.as_dict())
#
# print(db.get_table_names())
