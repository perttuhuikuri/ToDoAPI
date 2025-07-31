import logging
import azure.functions as func
import requests
import os
import json

API_URL = "https://todoapifunction.azurewebsites.net/api/ToDoFunction"
API_KEY = os.environ.get("TODO_API_KEY")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Proxy request received.")

    if not API_KEY:
        logging.error("TODO_API_KEY environment variable is missing!")
        return func.HttpResponse("Server misconfigured", status_code=500)

    method = req.method
    headers = {"x-functions-key": API_KEY}

    try:
        if method == "GET":
            r = requests.get(API_URL, headers=headers)
        elif method == "POST":
            r = requests.post(API_URL, headers=headers, json=req.get_json())
        elif method == "PUT":
            r = requests.put(API_URL, headers=headers, json=req.get_json())
        elif method == "DELETE":
            r = requests.delete(API_URL, headers=headers, json=req.get_json())
        else:
            return func.HttpResponse("Method not allowed", status_code=405)

        return func.HttpResponse(
            r.text,
            status_code=r.status_code,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
