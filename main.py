from fastapi import FastAPI, HTTPException
from fastapi import Request  # Import the Request class
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import db_helper
import generic_helper

app = FastAPI()

@app.post("/")
async def handle_request(request: Request):
		# Change the parameter type to Request
	payload = await request.json()  # Use json method to parse JSON data
	intent = payload['queryResult']['intent']['displayName']
	parameters = payload['queryResult']['parameters']
	output_contexts = payload['queryResult']['outputContexts']

	session_id = generic_helper.extract_session_id(output_contexts[0]['name'])

	intent_handler_dict = {
				'order.add-context: ongoing-order': add_to_order
				# 'order.remove - context: ongoing-order': remove_from_order,
				# 'order.complete - context: ongoing-order': complete_order,
				# 'track.order - context: ongoing-tracking': track_order
		}
	return intent_handler_dict[intent](parameters, session_id)


def add_to_order(parameters: dict, session_id: str):
    food_items = parameters["food-item"]
    quantities = parameters["number"]

    if len(food_items) != len(quantities):
        fulfillment_text = "Sorry I didn't understand. Can you please specify food items and quantities clearly?"
    else:
          new_food_dict = dict(zip(food_items, quantities))
	  
          fulfillment_text = f"Received {food_items} and {quantities} in the backend"
    #     if session_id in inprogress_orders:
    #         current_food_dict = inprogress_orders[session_id]
    #         current_food_dict.update(new_food_dict)
    #         inprogress_orders[session_id] = current_food_dict
    #     else:
    #         inprogress_orders[session_id] = new_food_dict

    #     order_str = generic_helper.get_str_from_food_dict(inprogress_orders[session_id])
    #     fulfillment_text = f"So far you have: {order_str}. Do you need anything else?"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def track_order(parameters: dict):
	
	order_id = parameters['order_id']
	order_status = db_helper.get_order_status(order_id)
	
	if order_status:
		fulfillmentText = f"The order status for order id : {order_id} is : {order_status}"
	else:
		fulfillmentText = f"No order found with order id : {order_id}"
	
	db_helper.get_order_status(order_id)
	return JSONResponse(content={"fulfillmentText": fulfillmentText})     