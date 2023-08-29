import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import pymysql
from os import environ

llm = OpenAI(api_token=environ.get("OPENAI_API_TOKEN"))

query = """
        select * from payments;
        """

db_config = {
    "host": environ.get("HOST"),
    "user": environ.get("USERNAME"),
    "password": environ.get("PASSWORD"),
    "db": environ.get("DB"),
    "port": int(environ.get("PORT"))
}

conn = pymysql.connect(**db_config)
df = pd.read_sql(query, conn)
print("Processing...\n")

pandas_ai = PandasAI(
    llm=llm, 
    enable_cache=False, 
    enforce_privacy=True, 
    conversational=True
    )

response = pandas_ai.run(df, prompt="which customer has made the highest payment")
print(response)

