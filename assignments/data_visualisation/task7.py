import matplotlib.pyplot as plt

languages = ['Python','Java','C++','JavaScript','R']
votes = [45, 30, 25, 35, 15]
colors = ['gold', 'skyblue', 'lightgreen', 'orange', 'pink']

plt.figure(figsize=(8,5))
plt.barh(
    languages,
    votes,
    color = colors
)
plt.title('Favorite Programming Languages Survey')
plt.xlabel('Number of Votes')
plt.ylabel('Programming Languages')
plt.grid(axis='x')
plt.show()

plt.figure(figsize=(7, 7))

explode = (0.1, 0, 0, 0, 0)
plt.pie(
    votes,
    labels=languages,
    colors=colors,
    autopct='%1.1f%%',
    explode=explode,
    shadow=True,
    startangle=90
)

plt.title('Programming Language Popularity')

plt.show()