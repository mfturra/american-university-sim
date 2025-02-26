from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///database.db", echo=True)

# commit as you go strategy
with engine.connect() as conn:
      ## create table and insert data into table
#     conn.execute(text("CREATE TABLE students (name string, age int)"))
#     conn.execute(
#         text("INSERT INTO students (name, age) VALUES (:name, :age)"),
#         [{"name": "pedro", "age": 25}, {"name": "daniel", "age": 32}]
#     )
#     conn.commit()
    ## search for entry that fulfills specific criteria
    result = conn.execute(text("SELECT name, age FROM students WHERE age < 30"))
    for row in result: 
        print(f"name:{row.name}, age:{row.age}")



# begin once strategy
# with engine.begin() as conn:
    ## create table and insert data into table
    # conn.execute(text("CREATE TABLE students (name string, age int)"))
    # conn.execute(
    #     text("INSERT INTO students (name, age) VALUES (:name, :age)"),
    #     [{"name": "pedro", "age": 25}, {"name": "daniel", "age": 32}])

    ## query table and output all elements of requested rows
    # result = conn.execute(text("SELECT name, age FROM students"))
    # for row in result:
    #     print(f"name:{row.name}, age:{row.age}")

