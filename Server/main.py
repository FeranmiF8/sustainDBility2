import pandas as pd

data = {
    "Temperature":[12, 43, 35],
    "Moisture":[65, 43, 32]
}

df = pd.DataFrame(data)

df.to_csv("test.csv")

print(df)