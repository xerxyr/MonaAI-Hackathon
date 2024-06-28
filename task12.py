import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data/502acf0c3bfbe29dd8496a42634e85c7.csv')

# Group the data by 'city_name'
grouped = df.groupby('city_name')

over50 = []

# Iterate over each group and perform your processing
for city, data in grouped:

    # filtered_data = df[(df['dt_iso'].dt.date >= pd.Timestamp('2024-05-14').date()) & (df['dt_iso'].dt.date <= pd.Timestamp('2024-05-17').date())]
    filtered_data = data

    print(f"Processing data for {city}:", end='')
    average_rainfall_by_region = data['rain_1h'].mean()
    print(f'avg = {average_rainfall_by_region}')

    # Calculate the sum of rain in the last 24 hours

    data.set_index('dt_iso', inplace=True)
    # data = data.sort_values('dt_iso')
    data = data.sort_index()
    # data['rain_last_24h'] = data['rain_1h'].rolling('24H', on='dt_iso').sum()
    data['rain_last_24h'] = data['rain_1h'].rolling(24).sum()
    max_rainfall_by_region = data['rain_last_24h'].max()
    print(f'max = {max_rainfall_by_region}')
    data.reset_index(inplace=True)

    if max_rainfall_by_region > 50:
        over50.append((city, max_rainfall_by_region))

print('over 50mm:')

for x in over50:
    print(f' {x[0]} : {x[1]}')
