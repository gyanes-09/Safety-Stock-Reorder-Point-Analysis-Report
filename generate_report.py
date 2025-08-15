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
