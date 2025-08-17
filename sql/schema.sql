-- Initial PostgreSQL schema
CREATE TABLE source_data (
    id SERIAL PRIMARY KEY,
    source_name VARCHAR(100),
    data_date DATE,
    raw_data JSONB,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE audit_log (
    id SERIAL PRIMARY KEY,
    event_type VARCHAR(50),
    event_details TEXT,
    event_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE processed_data (
    id SERIAL PRIMARY KEY,
    source_id INT REFERENCES source_data(id),
    metric_name VARCHAR(100),
    metric_value NUMERIC,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE uat_tests (
    id SERIAL PRIMARY KEY,
    test_name VARCHAR(100),
    expected_result VARCHAR(255),
    actual_result VARCHAR(255),
    status VARCHAR(20),
    tested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
