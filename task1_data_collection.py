import pandas as pd
import requests
df_csv = pd.read_csv("your_file.csv")
print(df_csv.head())
df_excel = pd.read_excel("your_file.xlsx")
print(df_excel.head())
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()
df_api = pd.DataFrame(data)
print(df_api.head())
