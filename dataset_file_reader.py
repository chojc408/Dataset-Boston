import pandas as pd
import numpy as np

def csv_to_dataframe(file_name, col_names=None, header=None):
    # header=0
    df = pd.read_csv(file_name, names=col_names, header=header)
    return df

def dataframe_to_array(df):
    array = pd.DataFrame(df).to_numpy()
    return array

def array_to_dataframe(array, col_names=None):
    df = pd.DataFrame(array, columns = col_names)
    return df

file_name = "Boston_Housing.csv"

# === Conversions
df = csv_to_dataframe(file_name, header=0)
print(df); print()
print(list(df.columns)); print()

array = dataframe_to_array(df)
print(array[:5]); print()

# === Save
df.to_pickle("Boston_Housing.df.pkl")
np.save("Bostong_Housing.npy", array)

# === Load
df = pd.read_pickle("Boston_Housing.df.pkl")
print(df.iloc[50:60]); print()
array = np.load("Bostong_Housing.npy", allow_pickle=True)
print(array[:5])
