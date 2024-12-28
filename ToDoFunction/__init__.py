import logging
import azure.functions as func
import json

# In-memory database (can be replaced with Azure Table Storage)
todos = []  # Global list to store to-do items

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing a request in ToDoFunction.')

    global todos  # Ensure todos is declared global at the start of the function

    try:
        method = req.method

        if method == "GET":
            # Return all To-Do items
            return func.HttpResponse(
                json.dumps(todos), 
                status_code=200, 
                mimetype="application/json"
            )

        elif method == "POST":
            # Create a new To-Do item
            new_todo = req.get_json()
            todos.append(new_todo)
            return func.HttpResponse(
                json.dumps({"message": "To-Do created", "todo": new_todo}), 
                status_code=201
            )

        elif method == "PUT":
            # Update an existing To-Do item
            update_data = req.get_json()
            for todo in todos:
                if todo["id"] == update_data["id"]:
                    todo.update(update_data)
                    return func.HttpResponse(
                        json.dumps({"message": "To-Do updated", "todo": todo}), 
                        status_code=200
                    )
            return func.HttpResponse("To-Do not found", status_code=404)

        elif method == "DELETE":
            # Delete a To-Do item
            delete_data = req.get_json()
            todos = [todo for todo in todos if todo["id"] != delete_data["id"]]
            return func.HttpResponse("To-Do deleted", status_code=200)

        else:
            # Method not allowed
            return func.HttpResponse("Method not allowed", status_code=405)

    except Exception as e:
        # Return an error response
        logging.error(f"Error processing request: {str(e)}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
