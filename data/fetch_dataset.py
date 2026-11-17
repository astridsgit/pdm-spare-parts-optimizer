
from ucimlrepo import fetch_ucirepo
import pandas as pd


dataset = fetch_ucirepo(id=601)
df = pd.concat([dataset.data.ids, dataset.data.features, dataset.data.targets], axis=1)

output_path = "data/ai4i2020.csv"
df.to_csv(output_path, index=False)

print(f"Saved {len(df)} rows and {len(df.columns)} columns to {output_path}")
print("\nFailure mode counts:")
print(df[["Machine failure", "TWF", "HDF", "PWF", "OSF", "RNF"]].sum())
