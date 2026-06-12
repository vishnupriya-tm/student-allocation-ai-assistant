import pandas as pd
from django.db import connection


def create_table_and_insert_data(dataset):

    file_path = dataset.uploaded_file.path

    table_name = dataset.table_name

    df = pd.read_csv(file_path)

    columns = []

    for col in df.columns:
        columns.append(f'"{col}" TEXT')

    create_table_sql = f'''
        CREATE TABLE IF NOT EXISTS "{table_name}" (
            id SERIAL PRIMARY KEY,
            {",".join(columns)}
        );
    '''

    with connection.cursor() as cursor:

        cursor.execute(create_table_sql)

        for _, row in df.iterrows():

            values = [str(v) for v in row.tolist()]

            placeholders = ",".join(["%s"] * len(values))

            insert_sql = f'''
                INSERT INTO "{table_name}"
                ({",".join(df.columns)})
                VALUES ({placeholders})
            '''

            cursor.execute(insert_sql, values)