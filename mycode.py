import pandas as pd
import os

os.makedirs("data", exist_ok=True)
file_path = "data/dataset.csv"

new_row = pd.DataFrame([{
    "Hours_Studied": 5,
    "Attendance": 85,
    "Score": 78
}])

if os.path.exists(file_path):
    new_row.to_csv(file_path, mode="a", header=False, index=False)
else:
    new_row.to_csv(file_path, index=False)

print("Dataset updated successfully!")
print(pd.read_csv(file_path))
