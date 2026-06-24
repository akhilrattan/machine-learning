import matplotlib.pyplot as plt


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
temperature = [15, 18, 22, 28, 35, 42]


plt.figure(figsize=(8, 5))
plt.plot(
    months,
    temperature,
    color='red',
    marker='o',
    linestyle='--',
    label='Temperature'
)
plt.xlabel("months")
plt.ylabel("temperature")
plt.title("months vs temperature")
plt.ylim(0,50)
plt.legend()
plt.grid(True)
plt.show()
        

