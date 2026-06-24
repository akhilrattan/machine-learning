import numpy as np 
import matplotlib.pyplot as plt

np.random.seed(42) 
scores = np.random.normal(
    loc = 75,
    scale = 10,
    size = 200
)
plt.figure(figsize=(8,5))
plt.hist(
    scores,
    bins=15,
    color='skyblue',
    edgecolor='black',
    alpha=0.7,
    label='Frequency'
)

plt.hist(
    scores, 
    bins=15,
    density=True,
    color="pink",
    edgecolor="red",
    alpha= 0.5,
    label="density"
)
plt.xlabel('Exam Scores')
plt.ylabel('Frequency / Densitypython task8.py')
plt.title('Distribution of Exam Scores')
plt.grid(True)
plt.legend()
plt.show()