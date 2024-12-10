import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import os

database_url = f"postgresql://{os.environ["DATABASE_USERNAME"]}:{os.environ["DATABASE_PASSWORD"]}@{os.environ["DATABASE_HOST"]}:{os.environ["DATABASE_PORT"]}/{os.environ["DATABASE_DATABASE"]}"

csv_file = os.path.join("artifacts", "courts.csv")
df = pd.read_csv(csv_file)

engine = create_engine(database_url)
connection = psycopg2.connect(database_url)

def get_city_id(city_name):
    with connection.cursor() as cursor:
        query = 'SELECT "CityId" FROM "City" WHERE "Name" = %s'
        cursor.execute(query, (city_name,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

courts_data = []

for _, row in df.iterrows():
    city_id = get_city_id(row['city'])
    if city_id:
        courts_data.append({
            'CourtId': _,
            'Name': row['name'],
            'CityId': city_id,
            'NumberOfCourts': row['number_of_courts'],
            'Lines': row['lines_status'],
            'Nets': row['nets_status']
        })

courts_df = pd.DataFrame(courts_data)

courts_df.to_sql('Courts', engine, if_exists='append', index=False)
