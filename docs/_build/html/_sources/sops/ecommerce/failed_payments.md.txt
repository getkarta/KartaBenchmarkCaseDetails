# Handling Failed Payments

## Scope

This SOP applies to all customer service agents handling cases where a payment has failed or is pending.

### Step 1: Identify the Customer

* Ask the customer for their registered email address.

### Step 2: Retrieve Order Details

* Ask the customer for the order id. If the customer does not have it look for active orders from the customer details - `active_orders`
* Provide to the customer all the open orders and the items and their descriptions using the `summarize_orders_api`

### Step 3: Identify the Correct Order
* The customer should be able to identify the correct order ID.
* Use this to pull the order details using the `get_order_details' api.

### Step 4: Check Payment Status
* Check the payment status of the order using the response.
* If the payment status is `FAILED` or `PENDING` then proceed to the next step.
* If the payment status is `SUCCESS` then inform the customer that the payment has been successful and that the order is processing.

### Step 5: Offer Compensation
* If the payment status is `FAILED` inform the customer that the payment has failed and that they will have to try again.
* If the payment status is `PENDING` inform the customer that the payment is pending and that they will have to wait for it to be processed. Ask them to check again in 2 hours.
* If the amount has been deducted from the customer's account, re-assure them that the amount will be credited back to their account in case of a failed payment in 24 hours.











