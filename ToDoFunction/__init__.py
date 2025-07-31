import logging
import azure.functions as func
import json
import os
import requests

# Your proxy function
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing request through secure proxy.')

    try:
        method = req.method
        body = req.get_json() if method in ["POST", "PUT", "DELETE"] else None

        # Load URL and Key from environment
        target_url = os.environ["AZURE_FUNCTION_URL"]
        key = os.environ["AZURE_FUNCTION_KEY"]

        # Forward request to the real function
        response = requests.request(
            method,
            f"{target_url}?code={key}",
            json=body
        )

        # Return the response to frontend
        return func.HttpResponse(
            response.text,
            status_code=response.status_code,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
