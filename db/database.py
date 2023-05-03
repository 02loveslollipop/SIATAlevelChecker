import pandas as pd
import sqlalchemy as sql
from console import Console

#Data source is users
class DataBase:
    def __init__(self,database: str = 'users',type: str = 'access' ,path: str = './users.accdb', user: str = None, password: str = None, host: str = None ,port: str = None, url: str = None) -> None:
        
        if type == 'access':
            engine = sql.create_engine(f"access:///?DataSource={path}")
            self.dataFrame = pd.read_sql_table(database,engine)
        elif type == 'csv':
            self.dataFrame = pd.read_csv()
        elif type == 'excel':
            self.dataFrame = pd.read_excel()
        elif type == 'postgresql':
            if port == None:
                port = '5432'
            engine = sql.create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")
            self.dataFrame = pd.read_sql_table(database,engine)
        elif type == 'mysql':
            if port == None:
                port = '3306'
            engine = sql.create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")
            self.dataFrame = pd.read_sql_table(database,engine)
        elif type == 'microsoftsql':
            if port == None:
                port = '1433'
            engine = sql.create_engine(f"mssql+pyodbc://{user}:{password}@{host}:{port}/{database}")
            self.dataFrame = pd.read_sql_table(database,engine)
        elif type == 'custom':
            if port == None:
                print(Console.error("You are trying to use a custom database setup but didn't provide a port"))
                exit()
                
            if port == None:
                print(Console.error("You are trying to use a custom database setup but didn't provide a url"))
                exit()
            try:
                engine = sql.create_engine(url)
            except Exception as e:
                print(Console.error(f"sqlalchemy throw this excpection when trying to setup the custom databse: {e}"))
                exit()
    def printDataFrame(self) -> None:
        print(self.dataFrame.to_string)
    def checkUserPassword(self,user: str,passwordHash: str) -> bool:
        pass