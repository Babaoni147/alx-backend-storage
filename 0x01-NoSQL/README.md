# Project: MongoDB and Python Scripts

This project contains a collection of Python scripts for managing and querying MongoDB databases. Below is a breakdown of each file and its purpose.

## File List

| File Name               | Description |
|-------------------------|-------------|
| `0-list_databases`      | Lists all databases in MongoDB. |
| `1-use_or_create_database` | Uses or creates a specified database in MongoDB. |
| `2-insert`              | Inserts documents into a specified MongoDB collection. |
| `3-all`                 | Queries and returns all documents in a MongoDB collection. |
| `4-match`               | Matches documents based on specific criteria. |
| `5-count`               | Counts the number of documents that match certain criteria. |
| `6-update`              | Updates specific documents in a MongoDB collection. |
| `7-delete`              | Deletes specified documents from a MongoDB collection. |
| `8-all.py`              | Retrieves all documents from a collection, with added logic. |
| `9-insert_school.py`    | Inserts school documents into a MongoDB collection. |
| `10-update_topics.py`   | Updates topics in school documents within a MongoDB collection. |
| `11-schools_by_topic.py` | Finds schools based on topic criteria. |
| `12-log_stats.py`       | Displays log statistics for Nginx logs stored in MongoDB. |
| `100-find`              | Custom script for finding documents with specified attributes. |
| `101-students.py`       | Manages student records in MongoDB. |
| `102-log_stats.py`      | Extended log statistics script for Nginx logs in MongoDB. |
| `README.md`             | Project documentation and file descriptions. |

## Requirements

- Python 3.x
- MongoDB
- `pymongo` library for MongoDB interactions
- Each script is designed to be executed with appropriate MongoDB permissions.

## Usage

Each script can be run independently. For example, to use the `0-list_databases` script, navigate to the project directory and execute:

```bash
python3 0-list_databases
