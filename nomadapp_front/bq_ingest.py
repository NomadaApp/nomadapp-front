from google.oauth2 import service_account
from google.cloud import bigquery
from google.cloud.exceptions import NotFound
import pandas as pd
import pandas_gbq

creds_file = "./keys.json"
credentials = service_account.Credentials.from_service_account_file(creds_file)

client = bigquery.Client(credentials=credentials)

df = pd.DataFrame({"a": [1, 2, 3], "b": [2, 3, 5], "c": [3, 2, 9]})

df.to_gbq(
    "nomadapp.user-queries",
    project_id="cocktail-bootcamp",
    credentials=credentials,
    if_exists="append",
)

# query = """
# SELECT name, SUM(number) as total_people
# FROM bigquery-public-data.usa_names.usa_1910_2013
# WHERE state = 'TX'
# GROUP BY name
# ORDER BY total_people DESC
# LIMIT 20
# """


# query_job = client.query(query)

# for row in query_job.result():
#     print(row[0], row["total_people"])


# def table_exists(table_id: str):
#     client = bigquery.Client(credentials=credentials)
#     try:
#         client.get_table(table_id)
#         print("Table ", table_id, "Exists")

#     except NotFound:
#         print("Table ", table_id, "Doesn't Exist")


# # table_exists("cocktail-bootcamp.class.adult_dataset")

# """
# pandas gbq
# """
# import pandas_gbq

# query = """
# select *
# from bigquery-public-data.chicago_crime.crime
# limit 10
# """
# project_id = "cocktail-bootcamp"

# df = pandas_gbq.read_gbq(query, project_id=project_id, credentials=credentials)

# print(df.head())

# df.to_gbq("chicago.pandas-table", project_id)
