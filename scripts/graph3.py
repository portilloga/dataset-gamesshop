import matplotlib.pyplot as plt
import pandas as pd

# Example: Load combined_df from a CSV file (update the path as needed)
combined_df = pd.read_csv('../data/processed_data/Meganium_Sales_data.csv')

# Calculate total profit per site
site_profits = combined_df.groupby("site")["total_price"].sum().sort_values(ascending=False)

# Plotting
plt.figure(figsize=(8, 6))
site_profits.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title("Lucros Totais por Fornecedor")
plt.ylabel("Lucro Total (após descontos)")
plt.xlabel("Fornecedor")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()
