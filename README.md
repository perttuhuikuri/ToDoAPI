# Serverless To-Do API with Azure Functions (Python)

## Description
This project is a serverless To-Do API built using Azure Functions and Python. It demonstrates how to create, update, retrieve, and delete tasks using a scalable serverless architecture.

The API supports the following operations:
- **GET**: Retrieve all To-Do items.
- **POST**: Create a new To-Do item.
- **PUT**: Update an existing To-Do item.
- **DELETE**: Remove a To-Do item.

## Features
1. **Serverless Architecture**: Built on Azure Functions with a Consumption Plan for automatic scaling.
2. **CRUD Operations**: Complete Create, Read, Update, and Delete functionality.
3. **Python Implementation**: Developed with Python for simplicity and flexibility.

## Setup Instructions

### Prerequisites
Before running or deploying the project, ensure the following tools are installed:
- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
- [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local)
- Python 3.7 or later

### Local Setup
1. Clone the repository:
   ```bash
   git clone <GitHubRepoURL>
   cd ToDoApi
   ```

2. Create and activate a Python virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .\.venv\Scripts\Activate   # Windows
   ```

3. Install dependencies:
   ```bash
   pip install azure-functions
   ```

4. Run the function locally:
   ```bash
   func start
   ```

5. Test the API using Postman or curl:
   - **GET**: `http://localhost:7071/api/ToDoFunction`
   - **POST**: `http://localhost:7071/api/ToDoFunction` with JSON body:
     ```json
     { "id": 1, "task": "Learn Azure Functions", "completed": false }
     ```

### Deployment to Azure
1. Log in to Azure:
   ```bash
   az login
   ```

2. Create a Resource Group and Storage Account:
   ```bash
   az group create --name ToDoApiRG --location eastus
   az storage account create --resource-group ToDoApiRG --name todostorage123 --location eastus --sku Standard_LRS
   ```

3. Create a Function App:
   ```bash
   az functionapp create `
       --resource-group ToDoApiRG `
       --consumption-plan-location westeurope `
       --name ToDoFunctionApp123 `
       --storage-account todostorage123 `
       --os-type Linux `
       --runtime python `
       --runtime-version 3.12 `
       --functions-version 4
   ```

4. Deploy the function:
   ```bash
   func azure functionapp publish ToDoFunctionApp123
   ```

5. Test the deployed API:
   ```
   https://ToDoFunctionApp123.azurewebsites.net/api/ToDoFunction
   ```

## API Usage
### Endpoints
- **GET** `/api/ToDoFunction`: Retrieve all tasks.
- **POST** `/api/ToDoFunction`: Add a task.
  - Body Example:
    ```json
    { "id": 1, "task": "Learn Azure Functions", "completed": false }
    ```
- **PUT** `/api/ToDoFunction`: Update a task.
  - Body Example:
    ```json
    { "id": 1, "task": "Master Azure Functions", "completed": true }
    ```
- **DELETE** `/api/ToDoFunction`: Delete a task.
  - Body Example:
    ```json
    { "id": 1 }
    ```

## Future Improvements
- Add **persistent storage** with Azure Table Storage.
- Implement **authentication** using Azure AD.
- Build a **frontend** with React or Angular.
- Write **unit tests** for API validation.

## License
## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE.txt) file for details.
