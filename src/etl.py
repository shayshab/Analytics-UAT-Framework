# ETL Script: Ingest and process data
import psycopg2
import json
from datetime import datetime

def ingest_data(source_name, data, conn):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO source_data (source_name, data_date, raw_data)
            VALUES (%s, %s, %s)
            RETURNING id;
        """, (source_name, datetime.now().date(), json.dumps(data)))
        return cur.fetchone()[0]

def process_data(source_id, metrics, conn):
    with conn.cursor() as cur:
        for metric_name, metric_value in metrics.items():
            cur.execute("""
                INSERT INTO processed_data (source_id, metric_name, metric_value)
                VALUES (%s, %s, %s);
            """, (source_id, metric_name, metric_value))

def main():

    import csv
    conn = psycopg2.connect(dbname='yourdb', user='youruser', password='yourpass', host='localhost')
    # Ingest mock_transactions.csv
    data_path = '/Applications/MAMP/htdocs/data analytics_DBAG/data/mock_transactions.csv'
    print(f"Attempting to open data file: {data_path}")
    try:
        with open(data_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                source_id = ingest_data('mock_transactions', row, conn)
                process_data(source_id, {'amount': row['amount']}, conn)
    except Exception as e:
        print(f"Error opening data file: {e}")
    # Log audit event
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO audit_log (event_type, event_details)
            VALUES (%s, %s);
        """, ('ETL_RUN', 'Ingested mock_transactions.csv'))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
