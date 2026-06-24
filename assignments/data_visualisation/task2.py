import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

print(df.info())
print(df.describe())

avg_mathscore = df.groupby("gender")["math score"].mean()

print(avg_mathscore)

best_edu_level = df.groupby("parental level of education")["reading score"].mean()
print(best_edu_level.idxmax())