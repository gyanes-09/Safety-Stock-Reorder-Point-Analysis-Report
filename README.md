# Safety Stock & Reorder Point Analysis

## Overview

This project analyzes historical sales data to calculate **Safety Stock** and **Reorder Points (ROP)** for products. These metrics are essential in supply chain management to prevent stockouts while minimizing excess inventory.

**Key Goals:**

- Calculate **Safety Stock** to account for demand variability.
- Calculate **Reorder Point** to determine when to place a new order.
- Perform data analysis and calculations using Python.

---

## Project Relevance

This project demonstrates:

- **Data-driven decision-making:** Uses historical sales data to optimize inventory.
- **Inventory optimization:** Balances product availability with holding costs.
- **Scalability:** Can handle large datasets for multiple products.

---

## Technical Stack

| Tool / Library | Purpose |
|----------------|---------|
| Python         | Core programming language for calculations and scripting. |
| Pandas         | Load, filter, and manipulate tabular data (CSV). |
| NumPy          | Numerical operations like square root and rounding. |
| Git / GitHub   | Version control and repository hosting. |

---

## Project Structure

inventory_analysis/
│
├─ generate_report.py # Python script for analysis
├─ sales_history.csv # Sample historical daily sales data
├─ .gitignore 

## Terminal Command
mkdir hul_inventory_analysis
cd hul_inventory_analysis

cat <<EOL > sales_history.csv
Date,Product,Sales
2023-01-01,Shampoo,155
2023-01-02,Shampoo,148
2023-01-03,Shampoo,162
2023-01-04,Shampoo,153
2023-01-05,Shampoo,170
2023-01-06,Shampoo,145
2023-01-07,Shampoo,166
2023-01-08,Shampoo,158
2023-01-09,Shampoo,175
2023-01-10,Shampoo,140
2023-01-01,Soap,310
2023-01-02,Soap,295
2023-01-03,Soap,325
2023-01-04,Soap,305
2023-01-05,Soap,330
2023-01-06,Soap,290
2023-01-07,Soap,340
2023-01-08,Soap,315
2023-01-09,Soap,335
2023-01-10,Soap,280
2023-01-01,Toothpaste,210
2023-01-02,Toothpaste,195
2023-01-03,Toothpaste,225
2023-01-04,Toothpaste,205
2023-01-05,Toothpaste,230
2023-01-06,Toothpaste,190
2023-01-07,Toothpaste,240
2023-01-08,Toothpaste,215
2023-01-09,Toothpaste,235
2023-01-10,Toothpaste,180
EOL

cat <<EOL > generate_report.py
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def generate_inventory_report(file_path='sales_history.csv'):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    LEAD_TIME_DAYS = 5
    Z_SCORE = 1.65
    results = []
    for product in df['Product'].unique():
        product_df = df[df['Product'] == product]
        avg_daily_sales = product_df['Sales'].mean()
        std_dev_sales = product_df['Sales'].std()
        safety_stock = Z_SCORE * np.sqrt(LEAD_TIME_DAYS * (std_dev_sales ** 2))
        reorder_point = (avg_daily_sales * LEAD_TIME_DAYS) + safety_stock
        results.append({
            'Product': product,
            'Avg Daily Sales': avg_daily_sales,
            'Std Dev of Sales': std_dev_sales,
            'Safety Stock': int(np.ceil(safety_stock)),
            'Reorder Point': int(np.ceil(reorder_point))
        })
    df_results = pd.DataFrame(results)
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=("Calculated Inventory Levels", "Daily Sales Distribution"),
        vertical_spacing=0.15
    )
    fig.add_trace(go.Bar(
        x=df_results['Product'],
        y=df_results['Reorder Point'],
        name='Reorder Point (ROP)',
        marker_color='#1E90FF'
    ), row=1, col=1)
    fig.add_trace(go.Bar(
        x=df_results['Product'],
        y=df_results['Safety Stock'],
        name='Safety Stock',
        marker_color='#FF6347'
    ), row=1, col=1)
    fig.add_trace(go.Box(
        x=df['Product'],
        y=df['Sales'],
        name='Sales Distribution',
        marker_color='#32CD32'
    ), row=2, col=1)
    fig.update_layout(
        title_text='<b>Safety Stock & Reorder Point Analysis Report</b>',
        height=800,
        template='plotly_dark',
        font=dict(family="Arial, sans-serif"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    fig.update_yaxes(title_text="Inventory Level (Units)", row=1, col=1)
    fig.update_yaxes(title_text="Daily Sales (Units)", row=2, col=1)
    report_filename = "inventory_analysis_report.html"
    fig.write_html(report_filename)
    print(f"Report generated: {report_filename}")

if __name__ == '__main__':
    generate_inventory_report()
EOL

pip3 install pandas numpy plotly
python3 generate_report.py
open inventory_analysis_report.html
<img width="452" height="257" alt="image" src="https://github.com/user-attachments/assets/c280f2c9-04ad-4447-88d9-cec4a24fcaf2" />
<img width="452" height="259" alt="image" src="https://github.com/user-attachments/assets/e56795ba-21d0-43b4-8a38-dad98d1aadec" />
<img width="452" height="259" alt="image" src="https://github.com/user-attachments/assets/1c05ccdd-8f7e-4362-b56c-68ed8486e15c" />
<img width="452" height="260" alt="image" src="https://github.com/user-attachments/assets/ec5e5e46-c7e4-45a0-b8e5-09e690c02ad0" />
<img width="452" height="261" alt="image" src="https://github.com/user-attachments/assets/74808ac9-be13-4311-a6e2-ca87adf41d23" />
<img width="452" height="260" alt="image" src="https://github.com/user-attachments/assets/2a9ae28d-3200-4293-822f-4854e39d0003" />





