# Analytics Script: Analyze processed data
import psycopg2
import pandas as pd

def fetch_metrics(conn):
    return pd.read_sql("SELECT * FROM processed_data", conn)

def main():

    conn = psycopg2.connect(dbname='yourdb', user='youruser', password='yourpass', host='localhost')
    df = fetch_metrics(conn)
    print('Summary statistics for processed metrics:')
    print(df.describe())
    # Additional: show total and average transaction amount
    if 'metric_value' in df.columns:
        print('Total amount:', df['metric_value'].sum())
        print('Average amount:', df['metric_value'].mean())
    conn.close()

if __name__ == "__main__":
    main()
