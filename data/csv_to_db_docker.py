import os
import pathlib
from dotenv import load_dotenv

import pandas as pd
from sqlalchemy import ForeignKey, Integer, create_engine, MetaData, Table, Column, String, DateTime, inspect, text

db_username = os.environ.get("DB_USERNAME")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get('DB_HOST', 'localhost')
db_name = os.environ.get("DB_NAME")


def store_csv_to_db(csv_file):
    # Connect to MySQL without specifying a database
    root_engine = create_engine(f"mysql+pymysql://{db_username}:{db_password}@{db_host}")

    # Execute "CREATE DATABASE IF NOT EXISTS"
    with root_engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))

    # Connect to the specific database
    engine = create_engine(f'mysql+pymysql://{db_username}:{db_password}@{db_host}/{db_name}')

    # Load CSV file into DataFrame
    df = pd.read_csv(csv_file)
    column_mapping = {
        'case': 'case_id',
        'event': 'activity_name',
        'startTime': 'start_time',
        'completeTime': 'complete_time',
        'Resource': 'resource'
    }

    # Rename DataFrame columns to match SQL table columns
    df.rename(columns=column_mapping, inplace=True)
    cols_in_db = ['case_id', 'activity_name', 'start_time', 'complete_time', 'resource']
    # select only the columns from DataFrame that match the columns in your table
    df = df[cols_in_db]

    # create MetaData instance
    metadata = MetaData()

    # Create an inspector and check if the table exists
    inspector = inspect(engine)

    if not inspector.has_table('cases'):
        # Define the cases table
        cases_table = Table(
            'cases',
            metadata,
            Column('case_id', String(255), primary_key=True)
        )
        # Create the table
        cases_table.create(engine, checkfirst=True)

    if not inspector.has_table('events'):
        # Define the events table with case_id as a foreign key
        events_table = Table(
            'events',
            metadata,
            Column('event_id', Integer, primary_key=True),
            Column('case_id', String(255), ForeignKey('cases.case_id')),  # set as foreign key
            Column('activity_name', String(255)),
            Column('start_time', DateTime),
            Column('complete_time', DateTime),
            Column('resource', String(255))
        )
        # Create the table
        events_table.create(engine, checkfirst=True)

    # Write DataFrame to MySQL table
    df[['case_id']].drop_duplicates().to_sql('cases', con=engine, index=False, if_exists='append')
    df.to_sql('events', con=engine, index=False, if_exists='append')


def main():
    data_path = os.path.join('/data', 'running-example.csv')
    store_csv_to_db(data_path)
    print("Data stored successfully")


if __name__ == "__main__":
    main()
