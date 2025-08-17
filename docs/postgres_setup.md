# PostgreSQL Setup Guide

## 1. Install PostgreSQL
- macOS: `brew install postgresql`
- Windows: Download from [postgresql.org](https://www.postgresql.org/download/)

## 2. Start PostgreSQL Service
- macOS: `brew services start postgresql`

## 3. Create Database & User
```
psql postgres
CREATE DATABASE yourdb;
CREATE USER youruser WITH ENCRYPTED PASSWORD 'yourpass';
GRANT ALL PRIVILEGES ON DATABASE yourdb TO youruser;
```

## 4. Run Schema Script
- Execute the SQL in `sql/schema.sql` to create tables:
```
psql -U youruser -d yourdb -f sql/schema.sql
```

## 5. Update Python Scripts
- Edit connection details in `src/etl.py`, `src/analytics.py`, and `src/visualization.py`:
  - `dbname='yourdb', user='youruser', password='yourpass', host='localhost'`
