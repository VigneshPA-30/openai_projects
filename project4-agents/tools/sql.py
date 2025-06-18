import sqlite3
from langchain.tools import Tool
from pydantic.v1 import BaseModel
from typing import List

conn = sqlite3.connect("db.sqlite")

class RunQueryArgsSchema(BaseModel):
    query:str

def list_all_tables():
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in c.fetchall() if row[0] is not None]
    return ", ".join(tables)

def run_sql_query(query):
    c = conn.cursor()
    try:
        c.execute(query)
        return c.fetchall()
    except sqlite3.OperationalError as err:
        return str(err)

run_query_tool = Tool.from_function(
    func=run_sql_query,
    name="run_sql_query",
    description="Run a sql query",
    args_schema=RunQueryArgsSchema
    
)