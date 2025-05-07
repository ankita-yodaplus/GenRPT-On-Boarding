from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, ForeignKey, func  #,Insert

# engine = create_engine('sqlite:///mydatabase.db, echo=True')
engine = create_engine('postgresql+psycopg2://postgres:root@localhost:5432/satutorialdatabase', echo=True)

meta = MetaData()

people =Table(
    "people",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer),
)

things = Table(
 "things",
    meta,
    Column("id",Integer,primary_key=True),
    Column("description",String,nullable=False),
    Column("price",Float),
    Column("owner",Integer,ForeignKey('people.id'),nullable=False),
)
 


meta.create_all(engine)

conn = engine.connect()


insert_people = people.insert().values([
    {"name":"Mike", "age":30},
    {"name":"Bob", "age":35},
    {"name":"Anna", "age":38},
    {"name":"John", "age":50},
    {"name":"clara", "age":42},
])

insert_things =things.insert().values([
    {"description":"laptop", "price":1000.00, "owner":18},
    {"description":"phone", "price":500.00, "owner":18},
    {"description":"tablet", "price":300.00, "owner":19},
    {"description":"monitor", "price":200.50, "owner":20},
    {"description":"keyboard", "price":50.00, "owner":21},
    {"description":"mouse", "price":25.00, "owner":19},

])

group_by_statement = things.select().with_only_columns(things.c.owner, func.sum(things.c.price)).group_by(things.c.owner).having(func.sum(things.c.price) > 1000)
result =conn.execute(group_by_statement)
for row in result.fetchall():
    print(row)




# join_statement =people.join(things,people.c.id == things.c.owner)
# select_statement = people.select().with_only_columns(people.c.name,things.c.description).select_from(join_statement)

# result = conn.execute(select_statement)
# for row in result.fetchall():
#     print(row)


# conn.execute(insert_people)
# conn.commit()

# conn.execute(insert_things)
# conn.commit()



# update_statement = people.update().where(people.c.name == "John Doe").values(age=50) 
# result = conn.execute(update_statement)
# conn.commit()

# delete_statement = people.delete().where(people.c.name=="John Doe")
# result = conn.execute(delete_statement)
# conn.commit()



# select_statement = people.select().where(people.c.age >20)
# result = conn.execute(select_statement)
# for row in result.fetchall():
#  print(row)


# # insert_statement = people.insert().values(name="John Doe", age=30)
# insert_statement = Insert(people).values(name="Jane", age=40)
# result =conn.execute(insert_statement)
# conn.commit()