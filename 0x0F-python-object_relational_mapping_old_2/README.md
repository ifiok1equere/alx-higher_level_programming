#0x0F. Python - Object-relational mapping

This project takes sql to a next level.

In this project, two amazing worlds are linked together: Databases and Python!

The first part of the project, I use the module MySQLdb to connect to a MySQL database and execute my SQL queries.

In the second part, you will use the module SQLAlchemy to do the same thing except that now we dealing with an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries because the purpose of an ORM is to abstract the storage to the usage. 
With an ORM, the biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. 
No SQL queries were written in this section of the project, only Python code. 
One last thing is that my code is no longer “storage type” dependent.
I am now able to change my storage easily without re-writing your entire project.

Without ORM:

`conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")`
`cur = conn.cursor()`
`cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database`
`query_rows = cur.fetchall()`
`for row in query_rows:`
    `print(row)`
`cur.close()`
`conn.close()`

With an ORM:

`engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)`
`Base.metadata.create_all(engine)`

`session = Session(engine)`
`for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!`
    `print("{}: {}".format(state.id, state.name))`
`session.close()`
