from fastapi import FastAPI, HTTPException
from fastapi import Request  # Import the Request class
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

@app.post("/")
async def handle_request(request: Request):  # Change the parameter type to Request
    payload = await request.json()  # Use json method to parse JSON data
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']
 
    if intent == 'track.order-context:ongoing-tracking':
        return JSONResponse(content={
            "fulfillmentText": f"Received == {intent}== in the backend"
        })