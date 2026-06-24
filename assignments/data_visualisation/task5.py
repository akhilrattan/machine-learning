import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

sns.pairplot(iris, hue='species')
plt.show()

plt.figure(figsize=(8,6))
corr = iris.drop('species', axis=1).corr()

sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title('Correlation Heatmap of Iris Features')
plt.show()


plt.figure(figsize=(8,5))
sns.boxplot(
    x='species',
    y='petal_length',
    data=iris
)
plt.title('Petal Length Distribution by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()