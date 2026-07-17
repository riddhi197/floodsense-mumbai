import sqlite3
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
import os
import sys

def migrate(postgres_url):
    db_path = 'floodsense.db'
    nlp_csv_path = 'nlp_severity_scores.csv'
    
    if not os.path.exists(db_path):
        print(f"Error: SQLite database '{db_path}' not found in current directory.")
        sys.exit(1)
        
    print("--- Step 1: Connecting to Local SQLite Database ---")
    conn_sqlite = sqlite3.connect(db_path)
    
    # Read tables
    df_rainfall = pd.read_sql('SELECT * FROM rainfall_daily', conn_sqlite)
    df_wards = pd.read_sql('SELECT * FROM ward_risk', conn_sqlite)
    conn_sqlite.close()
    
    # Read NLP CSV
    if os.path.exists(nlp_csv_path):
        df_nlp = pd.read_csv(nlp_csv_path)
    else:
        df_nlp = None
        print("Warning: nlp_severity_scores.csv not found, skipping news feed table migration.")
        
    print("--- Step 2: Connecting to Cloud Supabase PostgreSQL ---")
    try:
        conn_pg = psycopg2.connect(postgres_url)
        cursor = conn_pg.cursor()
    except Exception as e:
        print(f"Error: Failed to connect to Supabase: {e}")
        sys.exit(1)
        
    print("--- Step 3: Creating Tables in PostgreSQL ---")
    
    # Create rainfall_daily table
    cursor.execute("""
    DROP TABLE IF EXISTS rainfall_daily CASCADE;
    CREATE TABLE rainfall_daily (
        Date TEXT PRIMARY KEY,
        Month INTEGER,
        Rainfall_mm REAL,
        Rainfall_3day REAL,
        Rainfall_7day REAL,
        Flood_Severity TEXT,
        Confirmed_Event INTEGER
    );
    """)
    
    # Create ward_risk table
    cursor.execute("""
    DROP TABLE IF EXISTS ward_risk CASCADE;
    CREATE TABLE ward_risk (
        Ward_Code TEXT PRIMARY KEY,
        Area_Covered TEXT,
        Risk_Level TEXT,
        Known_Flood_Spots_Count INTEGER,
        Population_At_Risk_Pct REAL,
        Cluster INTEGER,
        Cluster_Label TEXT,
        GMM_Prob_Low DOUBLE PRECISION,
        GMM_Prob_Med DOUBLE PRECISION,
        GMM_Prob_High DOUBLE PRECISION
    );
    """)
    
    # Create nlp_news table
    if df_nlp is not None:
        cursor.execute("""
        DROP TABLE IF EXISTS nlp_news CASCADE;
        CREATE TABLE nlp_news (
            Snippet_ID INTEGER PRIMARY KEY,
            Related_Date TEXT,
            Severity_Score INTEGER,
            Keywords_Found TEXT,
            Snippet_Preview TEXT
        );
        """)
        
    conn_pg.commit()
    print("Tables created successfully.")
    
    print("--- Step 4: Uploading Data to Supabase ---")
    
    # Helper to insert dataframe
    def insert_df(cursor, table_name, df, columns):
        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES %s ON CONFLICT DO NOTHING"
        values = [tuple(x) for x in df[columns].to_numpy()]
        execute_values(cursor, query, values)
        print(f"Uploaded {len(values)} rows to table '{table_name}'.")

    # Insert rainfall_daily
    insert_df(cursor, 'rainfall_daily', df_rainfall, 
              ['Date', 'Month', 'Rainfall_mm', 'Rainfall_3day', 'Rainfall_7day', 'Flood_Severity', 'Confirmed_Event'])
              
    # Insert ward_risk
    insert_df(cursor, 'ward_risk', df_wards, 
              ['Ward_Code', 'Area_Covered', 'Risk_Level', 'Known_Flood_Spots_Count', 'Population_At_Risk_Pct', 'Cluster', 'Cluster_Label', 'GMM_Prob_Low', 'GMM_Prob_Med', 'GMM_Prob_High'])
              
    # Insert nlp_news
    if df_nlp is not None:
        insert_df(cursor, 'nlp_news', df_nlp, 
                  ['Snippet_ID', 'Related_Date', 'Severity_Score', 'Keywords_Found', 'Snippet_Preview'])
                  
    conn_pg.commit()
    cursor.close()
    conn_pg.close()
    print("Database migration to Supabase completed successfully!")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python migrate_to_supabase.py \"<supabase_postgresql_connection_url>\"")
        sys.exit(1)
    migrate(sys.argv[1])
