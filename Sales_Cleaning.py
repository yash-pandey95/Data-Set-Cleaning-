import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Sample - Superstore.csv")


print(df.head())


print(df.info())

print(df.isnull().sum())


df = df.drop_duplicates()


df["Order Date"] = pd.to_datetime(df["Order Date"])


total_sales = df["Sales"].sum()

print("Total Sales:", total_sales)


monthly_sales = df.groupby(df["Order Date"].dt.month)["Sales"].sum()

print(monthly_sales)


monthly_sales.plot(kind="bar")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_chart.png")  
plt.show()


df.to_csv("cleaned_superstore.csv", index=False)

print("Data cleaning and analysis completed!")
