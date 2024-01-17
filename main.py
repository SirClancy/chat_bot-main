from fastapi import FastAPI, HTTPException
from fastapi import Request  # Import the Request class
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import db_helper


app = FastAPI()

@app.post("/")
async def handle_request(request: Request):  # Change the parameter type to Request
    payload = await request.json()  # Use json method to parse JSON data
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']
 
    if intent == 'track.order-context:ongoing-tracking':
        return track_order(parameters)
      
    
def track_order(parameters: dict):
  order_id = parameters['order_id']
  order_status = db_helper.get_order_status(order_id)
  
  if order_status:
     fulfillmentText = f"The order status for order id : {order_id} is : {order_status}"
  else:
     fulfillmentText = f"No order found with order id : {order_id}"
  
  db_helper.get_order_status(order_id)
  return JSONResponse(content={
            "fulfillmentText": fulfillmentText
        })     