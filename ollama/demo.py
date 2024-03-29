from vanna.ollama import Ollama
from vanna.chromadb.chromadb_vector import ChromaDB_VectorStore

class MyVanna(ChromaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config=config)


vn = MyVanna(config={'model': 'gemma:7b'})

vn.connect_to_sqlite('my-database.sqlite')

df_ddl = vn.run_sql("SELECT type, sql FROM sqlite_master WHERE sql is not null")

for ddl in df_ddl['sql'].to_list():
    vn.train(ddl=ddl)

vn.train(ddl="""
    CREATE TABLE IF NOT EXISTS my-table (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        age INT
    )
""")

vn.train(
    documentation="Our business defines OTIF score as the percentage of orders that are delivered on time and in full")

vn.train(sql="SELECT * FROM my-table WHERE name = 'John Doe'")

training_data = vn.get_training_data()

from vanna.flask import VannaFlaskApp

VannaFlaskApp(vn).run()
