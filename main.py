import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import pymysql
from os import environ

llm = OpenAI(api_token=environ.get("OPENAI_API_TOKEN"))

query = """
        SELECT 
            TABLE_NAME, 
            COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE
            TABLE_SCHEMA = 'classicmodels'
        """

db_config = {
    "host": environ.get("HOST"),
    "user": environ.get("USER"),
    "password": environ.get("PASSWORD"),
    "db": environ.get("DB"),
    "port": environ.get("PORT")
}
conn = pymysql.connect(**db_config)
df = pd.read_sql(query, conn)
print("Processing\n")

pandas_ai = PandasAI(
    llm=llm, 
    enable_cache=False, 
    enforce_privacy=True, 
    conversational=True
    )

response = pandas_ai.run(df, prompt="enter you prompts here")
print(response)

