import pandas as pd

# Load the large CSV
df = pd.read_csv("creditcard.csv")

# Split it in half
half = len(df) // 2
df1 = df.iloc[:half]
df2 = df.iloc[half:]

# Save the two parts
df1.to_csv("creditcard_part1.csv", index=False)
df2.to_csv("creditcard_part2.csv", index=False)
