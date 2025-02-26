from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine("sqlite+pysqlite:///database.db", echo=True)

# commit as you go strategy
with engine.connect() as conn:
      ## create table and insert data into table
#     conn.execute(text("CREATE TABLE students (name string, age int)"))

      ## executemany table insertions
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

# create a statement that should be passed into the session
stmt = text("SELECT name, age FROM students WHERE age > :age ORDER BY name, age")

# when session is activated, pass the inquired attributes 
'''
with Session(engine) as session:
    result = session.execute(stmt, {"age": 30})
    # output result in a row-by-row format
    for row in result:
        print(f"\nName:{row.name}, Age:{row.age}")
'''

# UPDATE TABLE, new connection established from Engine during each SQL execute command against the DB.
with Session(engine) as session:
    result = session.execute(
        text("UPDATE students SET age=:age WHERE name=:name"),
        [{"name":"patricia", "age":24}, {"name":"sandra", "age": 28}],
    )
    session.commit()

# query student objects
stmt = select(Student).filter_by(name="pedro")

# list of "Student" objects
stdnt_obj = session.scalars(stmt).all()

# query individual columns in DB
col_stmt = select(Student.name, Student.age)

# list of Row objects
rows = session.execute(col_stmt).all()

# adding new individual entries to DB
student1 = Student(name="Pedro")
student2 = Student(name="Rafael")
session.add(student1)
session.add(student2)

session.commit()

# adding batch items to a session
session.add_all(student1, student2)

# deleting objects 
session.delete(obj1)
session.delete(obj2)