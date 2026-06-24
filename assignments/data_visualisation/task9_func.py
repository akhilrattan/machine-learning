import matplotlib.pyplot as plt
months = ['Q1', 'Q2', 'Q3', 'Q4']
sales = [100000, 150000, 120000, 180000]
departments = ['IT', 'HR', 'Finance', 'Marketing']
performance = [85, 78, 92, 88]
companies = ['Company A', 'Company B', 'Company C', 'Others']
market_share = [35, 25, 20, 20]
ages = [25, 28, 32, 29, 35, 31, 27]

data = [months, sales]
def create_graph(data, chart_type , filename):
    plt.figure(figsize=(6,4))

    if(chart_type == "line"):
        plt.plot(
            data[0],
            data[1],
            color = "blue",
            marker ="o",
        )
    elif(chart_type =="bar"):
        plt.bar(
            data[0],
            data[1]
        )
    elif(chart_type =="pie"):
        plt.pie(
            data[1],
            labels=data[0],
            autopct='%1.1f%%'
        )
    elif(chart_type =="hist"):
        plt.hist(
            data[0],
            bins=5,
            edgecolor = "black"
        )

    else:
        print("Invalid chart type")
        return

    plt.tight_layout()

    plt.savefig(filename)

    plt.close()

    print(filename, "saved successfully")

create_graph(
    [months, sales],
    "line",
    "sales_chart.png"
)
create_graph(
    [departments, performance],
    "bar",
    "department_chart.png"
)
create_graph(
    [companies, market_share],
    "pie",
    "market_share_chart.png"
)
create_graph(
    ages,
    "hist",
    "age_distribution.png"
)

