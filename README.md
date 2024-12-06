# Weather Database Manager

## Overview
Weather Database Manager is a Python-based application that allows users to interact with a SQLite database for weather data. The application provides functionality to:
- Insert new records.
- Update existing records.
- Delete records (individually or all at once).
- Execute advanced queries with multiple conditions.

The project is designed with a user-friendly CLI interface and includes features like input validation and error handling.

## Features
1. **Insert Records**: Add new rows of data to the database.
2. **Update Records**: Modify existing data based on record ID.
3. **Delete Records**:
   - Delete records one by one.
   - Delete all records at once with confirmation.
4. **Advanced Querying**: Perform dynamic and complex queries with multiple conditions.
5. **Tabular Output**: Display query results in a user-friendly table format.

## Prerequisites
1. Python 3.x
2. SQLite3
3. Required Python libraries:
   - `tabulate`

To install dependencies, run:
```bash
pip install tabulate
