import pandas as pd
from fastavro import writer, reader, parse_schema



def departments_df_to_avro(df):
# 1. Define the schema
    department_schema = {
        'doc': 'Deparments table',
        'name': 'Deparments_table',
        'namespace': 'Deparments',
        'type': 'record',
        'fields': [
            {'name': 'id', 'type': 'int'},
            {'name': 'department', 'type': 'string'}
        ]
    }
    parsed_schema = parse_schema(department_schema)
    # 2. Convert pd.DataFrame to records - list of dictionaries
    records = df.to_dict('records')
    # 3. Write to Avro file
    with open(r'./src/data/backups/departments.avro', 'wb') as out:
        writer(out, parsed_schema, records)
        
def departments_avro_to_df():
    # 1. List to store the records
    avro_records = []
    # 2. Read the Avro file
    with open(r'./src/data/backups/departments.avro', 'rb') as fo:
        avro_reader = reader(fo)
        for record in avro_reader:
            avro_records.append(record)
    # 3. Convert to pd.DataFrame
    df_avro = pd.DataFrame(avro_records)
    #df_avro=df_avro.astype({'id':'int'},{'department':'string'})
    # Print the first couple of rows
    return df_avro

def jobs_df_to_avro(df):
# 1. Define the schema
    jobs_schema = {
        'doc': 'Jobs table',
        'name': 'Jobs_table',
        'namespace': 'Jobs',
        'type': 'record',
        'fields': [
            {'name': 'id', 'type': 'int'},
            {'name': 'job', 'type': 'string'}
        ]
    }
    parsed_schema = parse_schema(jobs_schema)
    # 2. Convert pd.DataFrame to records - list of dictionaries
    records = df.to_dict('records')
    # 3. Write to Avro file
    with open(r'./src/data/backups/jobs.avro', 'wb') as out:
        writer(out, parsed_schema, records)
        
def jobs_avro_to_df():
    # 1. List to store the records
    avro_records = []
    # 2. Read the Avro file
    with open(r'./src/data/backups/jobs.avro', 'rb') as fo:
        avro_reader = reader(fo)
        for record in avro_reader:
            avro_records.append(record)
    # 3. Convert to pd.DataFrame
    df_avro = pd.DataFrame(avro_records)
    #df_avro=df_avro.astype({'id':'int'},{'department':'string'})
    # Print the first couple of rows
    return df_avro

def employees_df_to_avro(df):
# 1. Define the schema
    department_schema = {
        'doc': 'Employees table',
        'name': 'Employees_table',
        'namespace': 'Employees',
        'type': 'record',
        'fields': [
            {'name': 'id', 'type': 'int'},
            {'name': 'name', 'type': 'string'},
            {'name': 'datetime', 'type': 'string'},
            {'name': 'department_id', 'type': 'int'},
            {'name': 'job_id', 'type': 'int'}
        ]
    }
    parsed_schema = parse_schema(department_schema)
    # 2. Convert pd.DataFrame to records - list of dictionaries
    records = df.to_dict('records')
    # 3. Write to Avro file
    with open(r'./src/data/backups/employees.avro', 'wb') as out:
        writer(out, parsed_schema, records)
        
def employees_avro_to_df():
    # 1. List to store the records
    avro_records = []
    # 2. Read the Avro file
    with open(r'./src/data/backups/employees.avro', 'rb') as fo:
        avro_reader = reader(fo)
        for record in avro_reader:
            avro_records.append(record)
    # 3. Convert to pd.DataFrame
    df_avro = pd.DataFrame(avro_records)
    #df_avro=df_avro.astype({'id':'int'},{'department':'string'})
    # Print the first couple of rows
    return df_avro