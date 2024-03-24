I wrote this to help  
Incase I am not available

The two features we intend to demonstrate are:
- order-status-fetching
- order returning after delivery

End point for order-status-fetching is `/order_status`  only param required is the `order_id` user auth is required.  
>condition to run:
>>> Order must exist --> create an order (endpoint for this is `/order` it's a POST endpoint)

End point for order returning after delivery is `/return-order` only param required is the `order_id` user auth is required.  
>condition to run:

>>>Order must exist --> create an order  

>>>There must be an available agent --> create an agent (endpoint for this is `/agent` it's a POST endpoint)  

>>>Order status must be `DELIVERED` --> set order status to `DELIVERED` (endpoint for this is `/order/<int:id>/update_status` it's a `PUT` endpoint)



These resources are in the `app/order/controller.py` and `app/agent/controller.py` files  

Or you can just be a real chad and do everything from the shell :CHAD

DISCLAIMER !!!  
There is no disclaimer  
  
All functions are simply for demo purposes, I did not write this with the intent of using it for a real logistic company 
