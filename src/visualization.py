# Visualization Script: Create dashboards
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2

def fetch_metrics(conn):
    return pd.read_sql("SELECT source_id, metric_name, metric_value, processed_at FROM processed_data", conn)

def plot_metrics(df):
    # Example: plot total amount by account
    import os
    reports_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../reports'))
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    pdf_path = os.path.join(reports_dir, 'transaction_amounts.pdf')
    print(f"Saving chart to: {pdf_path}")
    print(f"DataFrame columns: {df.columns.tolist()}")
    try:
        if 'metric_value' in df.columns and 'source_id' in df.columns:
            grouped = df.groupby('source_id')['metric_value'].sum()
            print("Grouped data:", grouped)
            grouped.plot(kind='bar')
            plt.title('Total Transaction Amount by Source ID')
            plt.xlabel('Source ID')
            plt.ylabel('Total Amount')
            plt.tight_layout()
            plt.savefig(pdf_path)
            print(f"Chart saved to {pdf_path}")
            plt.show()
        else:
            print("Required columns not found in DataFrame.")
    except Exception as e:
        print(f"Error saving chart: {e}")

def main():
    conn = psycopg2.connect(dbname='yourdb', user='youruser', password='yourpass', host='localhost')
    df = fetch_metrics(conn)
    plot_metrics(df)
    conn.close()

if __name__ == "__main__":
    main()
