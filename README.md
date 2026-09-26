# Top 10 Products

**Track:** Data Analytics — Veda Technology Internship
**Task:** Identify the top 10 products by sales
**Objective:** Practice ranking and sorting
**Tools:** Excel (SUMIF, LARGE, INDEX/MATCH, COUNTIF) and Python (pandas, matplotlib)
**Dataset:** Superstore sales dataset (9,994 order lines, 1,850 unique products)

## What's in this repo

| File | Description |
|---|---|
| `Top10_Products.xlsx` | `Sales_Data` (raw order lines), `Product_Totals` (SUMIF total per unique product), and `Summary` sheets (Top 10 via LARGE + INDEX/MATCH, tie flag via COUNTIF, cross-check, native horizontal bar chart) |
| `top10_products.py` | Python script — reproduces the same ranking with pandas and plots the chart with matplotlib |
| `top10_products.csv` | Output of the Python script — the ranked Top 10 list |
| `top10_products_chart.png` | Horizontal bar chart of the Top 10 (also embedded in the PDF report) |
| `Top10_Products_Report.pdf` | Project report: approach, Top 10 table, chart, key insights, interview-question notes |

## Approach

1. Totaled `Sales` per unique product (a product can appear in many order lines).
   - **Excel:** helper `Product_Totals` sheet with a `SUMIF` per product, then the `Summary` sheet
     pulls the Top 10 with `LARGE()` (value) + `INDEX/MATCH` (matching product name).
   - **Python:** `groupby('Product Name')['Sales'].sum()`, then `rank(method='min', ascending=False)`.
2. **Tie handling:** flagged whether any Top-10 product shares its exact sales total with another
   product (`COUNTIF` in Excel / `duplicated()` in Python) — none did in this dataset, but the method
   would surface a genuine tie rather than silently dropping one product.
3. Cross-checked rank 1's value against `MAX()` of all product totals — difference = $0.00.
4. Plotted the Top 10 as a horizontal bar chart (Excel native chart + matplotlib PNG).

## Key results

- **Canon imageCLASS 2200 Advanced Copier** is the #1 product by a wide margin — $61,599.82, more
  than double the #2 product.
- No exact ties occur in the Top 10.
- The list is dominated by high-ticket office equipment (copiers, binders, printers), not high-volume
  everyday items — unit price drives the leaderboard as much as order volume.

## How to run the Python version

```bash
pip install pandas matplotlib
python top10_products.py
```

Requires `superstore.csv` (Superstore dataset) in the same folder.
