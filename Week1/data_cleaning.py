import pandas as pd

#Q1
df = pd.read_parquet('Week1/fhv_tripdata_2021-01.parquet')
print(f"Number of records in dataset are: {df.shape}")
#Answer: Number of records in dataset are: (1154112, 7)

#Q2
print(df.columns)
print(df.head(5))

df['duration'] = df.dropOff_datetime - df.pickup_datetime
df.duration = df.duration.apply(lambda td: td.total_seconds() / 60)
print(df.columns)
print(df.head(5))
