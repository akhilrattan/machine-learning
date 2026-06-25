import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv('Mall_Customers.csv')

plt.figure(figsize=(12,4))

plt.subplot(1,2,1)
sns.histplot(
    df["Annual Income (k$)"],
    bins = 15,
    kde = True
)
plt.title("annual income distribution")
plt.subplot(1,2,2)
sns.histplot(df["Spending Score (1-100)"], bins=15, kde=True)
plt.title("Spending Score Distribution")

plt.tight_layout()
plt.show()

X = df[
[
"Annual Income (k$)",
"Spending Score (1-100)"
]
]
scaler = StandardScaler()
x_scaled = scaler.fit_transform(X)

wcss = []

for i in range(1,11):
    kmeans = KMeans(
        n_clusters = i,
        random_state=42,
        n_init = 10
    )
    kmeans.fit(x_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(6,5))
plt.plot(
    range(1,11),
    wcss,
    marker = "o"
)
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.grid(True)
plt.show()

kmeans = KMeans(
    n_clusters = 5,
    random_state=42,
    n_init=10
)
clusters = kmeans.fit_predict(x_scaled)
df["clusters"] = clusters


plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    hue="clusters",
    palette="Set1",
    s=100
)

plt.title("Customer Segments")
plt.show()
print(df.groupby("Cluster").mean(numeric_only=True))