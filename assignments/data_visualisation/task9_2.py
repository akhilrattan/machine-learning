import matplotlib.pyplot as plt

months = ['Q1', 'Q2', 'Q3', 'Q4']
sales = [100000, 150000, 120000, 180000]
departments = ['IT', 'HR', 'Finance', 'Marketing']
performance = [85, 78, 92, 88]
companies = ['Company A', 'Company B', 'Company C', 'Others']
market_share = [35, 25, 20, 20]
ages = [25, 28, 32, 29, 35, 31, 27, 33, 30, 36, 28, 29, 31, 34, 26]

fig, axs = plt.subplots(2, 2, figsize=(12, 10))

axs[0, 0].plot(
    months,
    sales,
    marker='o',
    color='blue',
    linewidth=1
)

axs[0, 0].set_title('Quarterly Sales')
axs[0, 0].set_xlabel('Quarter')
axs[0, 0].set_ylabel('Sales')
axs[0, 0].grid(True)

axs[0, 1].bar(
    departments,
    performance,
    color=['red', 'green', 'orange', 'purple']
)

axs[0, 1].set_title('Department Performance')
axs[0, 1].set_xlabel('Departments')
axs[0, 1].set_ylabel('Performance (%)')


axs[1, 0].pie(
    market_share,
    labels=companies,
    autopct='%1.1f%%',
    startangle=90
)

axs[1, 0].set_title('Market Share Distribution')

axs[1, 1].hist(
    ages,
    bins=15,
    color='skyblue',
    edgecolor='black'
)

axs[1, 1].set_title('Employee Age Distribution')
axs[1, 1].set_xlabel('Age')
axs[1, 1].set_ylabel('Frequency')


plt.tight_layout()

plt.show()