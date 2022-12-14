import pandas as pd
from fastavro import writer, reader
import copy
import json
from avro.datafile import DataFileWriter, DataFileReader
from avro.io import DatumWriter, DatumReader

#df = pd.read_csv('departmerts_backup.csv')
##print(df)


#1. List to store the records
avro_records = []

# 2. Read the Avro file
with open(r'./src/data/backups/employees.avro', 'rb') as fo:
    avro_reader = reader(fo)
    for record in avro_reader:
        avro_records.append(record)
        
# 3. Convert to pd.DataFrame
df_avro = pd.DataFrame(avro_records)

# Print the first couple of rows
print(df_avro.head())


# with open('jobs.avro', 'rb') as f:
#     reader = DataFileReader(f, DatumReader())
#     metadata = copy.deepcopy(reader.meta)
#     schema_from_file = json.loads(metadata['avro.schema'])
#     users = [user for user in reader]
#     reader.close()