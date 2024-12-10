from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker

database_url = f"postgresql://{os.environ["DATABASE_USERNAME"]}:{os.environ["DATABASE_PASSWORD"]}@{os.environ["DATABASE_HOST"]}:{os.environ["DATABASE_PORT"]}/{os.environ["DATABASE_DATABASE"]}"
engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()


metadata = MetaData()
city_table = Table(
    'City', 
    metadata,
    autoload_with=engine,
)

cities = [
    (1, "Orlando", "Florida"),
    (2, "Anaheim", "California"),
    (3, "Las Vegas", "Nevada"),
    (4, "New York", "New York"),
    (5, "Denver", "Colorado"),
    (6, "Atlanta", "Georgia"),
    (7, "Phoenix", "Arizona"),
    (8, "Tampa", "Florida"),
    (9, "Boston", "Massachusetts"),
    (10, "Fort Lauderdale", "Florida"),
    (11, "San Diego", "California"),
    (12, "Chicago", "Illinois"),
    (13, "Seattle", "Washington"),
    (14, "Dallas", "Texas"),
    (15, "Miami", "Florida"),
    (16, "Washington District of Columbia", ""),
    (17, "San Francisco", "California"),
    (18, "Charlotte", "North Carolina"),
    (19, "Honolulu", "Hawaii"),
    (20, "Houston", "Texas"),
    (21, "Philadelphia", "Pennsylvania"),
    (22, "Fort Myers", "Florida"),
    (23, "Nashville", "Tennessee"),
    (24, "Maui", "Hawaii"),
    (25, "Salt Lake City", "Utah"),
    (26, "Portland", "Oregon"),
    (27, "West Palm Beach", "Florida"),
    (28, "Minneapolis", "Minnesota"),
    (29, "Raleigh", "North Carolina"),
    (30, "Jacksonville", "Florida"),
    (31, "New Orleans", "Louisiana"),
    (32, "Austin", "Texas"),
    (33, "Savannah", "Georgia"),
    (34, "Cleveland", "Ohio"),
    (35, "St Louis", "Missouri"),
    (36, "Baltimore", "Maryland"),
    (37, "Pittsburgh", "Pennsylvania"),
    (38, "Charleston", "South Carolina"),
    (39, "Albuquerque", "New Mexico"),
    (40, "Columbus", "Ohio"),
    (41, "Myrtle Beach", "South Carolina"),
    (42, "San Jose", "California"),
    (43, "Providence", "Rhode Island"),
    (44, "Burlington", "North Carolina"),
    (45, "San Antonio", "Texas"),
    (46, "Kalaoa", "Hawaii"),
    (47, "Indianapolis", "Indiana"),
    (48, "Detroit", "Michigan"),
    (49, "Sacramento", "California"),
    (50, "Oakland", "California")
]


for city in cities:
    insert_query = city_table.insert().values(
        CityId=city[0],
        Name=city[1],
        State=city[2]
    )
    session.execute(insert_query)

session.commit()

session.close()
