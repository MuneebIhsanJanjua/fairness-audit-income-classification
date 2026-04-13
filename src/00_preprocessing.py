import pandas as pd

# Define the path to your .data file
data_file = '/Users/muneebihsan/Desktop/census+income/adult.data'

# Define column names (from adult.names)
columns = [
    "age", "workclass", "fnlwgt", "education", "education-num",
    "marital-status", "occupation", "relationship", "race", "sex",
    "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"
]

df = pd.read_csv(data_file, names=columns, sep=',', skipinitialspace=True)


print(df.head())
print(df.shape)
print(df.dtypes)


df.replace('?', pd.NA, inplace=True)
print("\nMissing values per column:")
print(df.isnull().sum())

df.dropna(inplace=True)
print(f"\nShape after dropping missing rows: {df.shape}")

df['income'] = df['income'].str.replace('.', '', regex=False)

df['income'] = df['income'].map({'<=50K': 0, '>50K': 1})

df.to_csv('/Users/muneebihsan/Desktop/census+income/adult_cleaned.csv', index=False)
print("\nCleaned data saved to your project folder!")

print(df.head())
print(df['income'].value_counts())