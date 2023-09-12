# ProXChat

## ⚠️ Disclaimer

This project is in an experimental phase and remains under active development. Please use it with caution and understand that you do so at your own risk.

## Docker setup

## Screencast video
add link here

## How to use the application

1. **Query execution data**:  
   Begin your queries on the execution data that corresponds to the BPMN process using natural language. Frame your questions, and the system will provide insights based on the data.

2. 🚨 **IMPORTANT information about the data**:
   The provided execution data includes the following:
   - Case identifiers.
   - Names of the executed activities within a case.
   - Start and completion time for each activity.
   - The actor responsible for executing the activity.

3. **Logging**: The application records your interactions to a file called `interaction_log.txt`, stored in the `logs` directory at the root. This file includes the LLM's reasoning for your question and the corresponding SQL queries.

