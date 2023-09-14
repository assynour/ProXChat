# ProXChat

## ⚠️ Disclaimer

This project is in an experimental phase and remains under active development.


## 🎥 Screencast video
The video is prepared as part of the submission to the [International Conference on Process Mining ICPM 2023](https://icpmconference.org/2023/).

Due to time constraints, very few questions have been shown. Feel free to try the application with questions such as:
* Compute the automation rate
* Who are the most overloaded
* Find the most executed activities
* and others

Watch here 👉 https://www.youtube.com/watch?v=_YssZlXGfhA


## :whale: Docker setup

Follow the steps below to set up and run the application using Docker:

1. **Download the code**:  
   Clone the project or download the code and unzip the downloaded folder.

2. **Set Up environment variables**:  
   - Open the file named `.env-example`.
   - Replace the placeholder `your-openai-key` with your actual OpenAI API key.
   - Save and close the file.
   - Rename the file to `.env`.

3. **Start Docker**:  
   Ensure that your Docker application is up and running.

4. **Execute Docker commands**:  
   - **For Windows users**:  
     Open the `cmd` as an administrator. Navigate to the project's root directory. Execute the following:
     ```
     run-proxchat-docker.bat
     ```
   - **For Linux users**:  
     In the terminal, from the project's root directory, execute:
     ```
     ./run-proxchat-docker.sh
     ```

   The `run-proxchat-docker.bat` script will:
   - Start a MySQL service.
   - Populate the MySQL database with data from the `running-example.csv` file located in `/backend/src/data`.
   - load the docker images for both the frontend and backend applications.

5. **Verify container creation**:  
   After successful execution, Docker will have created images for the application. A container named `proxchat` will be up and running with an associated data volume to ensure data persistence.

6. **Access the application**:  
   You can access the running application via your web browser at:  
   [http://localhost:3000](http://localhost:3000)


## ℹ️ How to use the application

1. **Query execution data**:  
   Begin your queries on the execution data that corresponds to the BPMN process using natural language. Frame your questions, and the system will provide insights based on the data.

2. **IMPORTANT information about the data**:
   The provided execution data includes the following:
   - Case identifiers.
   - Names of the executed activities within a case.
   - Start and completion time for each activity.
   - The actor responsible for executing the activity.

## 🙌 Feedback
The application records your interactions in a file called `interaction_log.txt`, which is stored in the `logs` directory at the root. This file contains all the details of the LLM reasoning and the generated queries. We are actively working on improving the application's robustness and welcome your feedback. You can share the file or provide direct feedback to nour.assy@bonitasoft.com.

