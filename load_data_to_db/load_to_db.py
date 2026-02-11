import json
import os
import pandas as pd
from sqlalchemy import create_engine


with open('load_data_to_db/videos.json') as file:
    data = json.load(file)

snapshots = []
videos = []
for video in data['videos']:
    for snapshot in video['snapshots']:
        snapshots.append(snapshot)
    del video['snapshots']

    videos.append(video)


snapshots = pd.DataFrame(snapshots)
videos = pd.DataFrame(videos)


db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
database = os.environ['DATABASE']
db_uri = f"postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/{database}"

engine = create_engine(db_uri)
snapshots.to_sql('snapshots', engine, if_exists='replace', index=False)
videos.to_sql('videos', engine, if_exists='replace', index=False)
