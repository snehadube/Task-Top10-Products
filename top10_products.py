"""
Top 10 Products — Veda Technology Internship (Data Analytics Track)
Identifies the top 10 products by sales.

Input : superstore.csv (must contain 'Product Name' and 'Sales' columns)
Output: top10_products.csv, top10_products_chart.png
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# 1. Load
df = pd.read_csv("superstore.csv", encoding="latin1")

# 2. Total sales per product (a product can appear in many orders)
totals = df.groupby("Product Name")["Sales"].sum().reset_index()

# 3. Rank descending and take the top 10.
#    method="min" gives tied products the SAME rank (competition ranking,
#    e.g. two products tied for #3 both show rank 3, next rank is 5) —
#    this is the standard way to "handle ties" instead of arbitrarily
#    breaking them.
totals["Rank"] = totals["Sales"].rank(method="min", ascending=False).astype(int)
totals = totals.sort_values("Sales", ascending=False)
top10 = totals[totals["Rank"] <= 10].copy()

# Flag any product that shares its sales total with another product
totals["Tie"] = totals.duplicated(subset="Sales", keep=False)
top10["Tie"] = top10["Product Name"].isin(totals.loc[totals["Tie"], "Product Name"])

top10 = top10[["Rank", "Product Name", "Sales", "Tie"]]
top10.to_csv("top10_products.csv", index=False)
print(top10.to_string(index=False))

# 4. Horizontal bar chart (top product at the top)
chart_data = top10.sort_values("Sales", ascending=True)
labels = [l if len(l) <= 45 else l[:42] + "..." for l in chart_data["Product Name"]]

fig, ax = plt.subplots(figsize=(9, 5.5))
bars = ax.barh(labels, chart_data["Sales"], color="#1F4E78")
ax.set_title("Top 10 Products by Sales", fontsize=13, fontweight="bold")
ax.set_xlabel("Total Sales ($)")
for bar, val in zip(bars, chart_data["Sales"]):
    ax.annotate(f"${val:,.0f}", xy=(val, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0), textcoords="offset points", va="center", fontsize=8)
ax.grid(True, alpha=0.3, axis="x")
plt.tight_layout()
plt.savefig("top10_products_chart.png", dpi=150)
print("\nSaved: top10_products.csv, top10_products_chart.png")
