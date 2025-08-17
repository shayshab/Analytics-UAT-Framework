# UAT Test Plan


## Test Cases
| Test Case | Description | Expected Outcome | Acceptance Criteria |
|-----------|-------------|-----------------|--------------------|
| TC01 | Ingest mock_transactions.csv | All rows ingested, no errors | Source data matches file |
| TC02 | Process transaction amounts | Metrics calculated correctly | Metrics match input data |
| TC03 | Audit log entry | ETL run logged | Audit log contains event |



## Workflow
1. Execute ETL and analytics scripts
2. Review logs and outputs
3. Record results in audit_log table
4. Approve/reject based on acceptance criteria
5. Track issues in Agile board



## Documentation
- Record test results in this file and in the database
- Summarize findings in `reports/`
