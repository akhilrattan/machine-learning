import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("country_wise_latest.csv")

print("number of records : ",len(df))

if "age" in df.columns and "id" in df.columns:
    df = df.dropna(subset=["age","id"])

print("Remaining Records:", len(df))

plt.figure(figsize=(8,5))
plt.plot(df["Active"],label = "active cases")
plt.plot(df["Recovered"],label = "recovered cases")
plt.title("recovered vs active cases")
plt.xlabel("records")
plt.ylabel("cases")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))
plt.plot(df["New deaths"], label = "new deaths")
plt.plot(df["New cases"], label = "new cases")
plt.title("new deaths vs new cases")
plt.xlabel("records")
plt.ylabel("results")
plt.legend()
plt.grid(True)
plt.show()
