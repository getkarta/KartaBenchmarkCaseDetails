# Handling Returns

## Scope

This SOP applies to all customer service agents handling cases where a customer wants to return an item.

## Step 1: Identify the Customer

* Ask the customer for their registered email address.

## Step 2: Retrieve Order Details

* Ask the customer for the order id. If the customer does not have it look for active orders from the customer details - `active_orders`
* Provide to the customer all the open orders and the items and their descriptions using the `summarize_orders`

## Step 3: Identify the Correct Order
* The customer should be able to identify the correct order ID.
* Use this to pull the order details using the `get_order_details' api.

## Step 4: Identify the items to be returned
* Present the customer with the items in the order and ask them to identify the items to be returned.
* The customer should be able to identify the items to be returned.
* Use this to pull the item details using the `get_item_details' api.

## Step 4: Check Return Eligibility
* Check the return eligibility of the items using the response.
* Only those items that are eligible for return should be returned.
* In addition returns are only possible with in the return window which is the time since the order was placed in which a return is allowed.
* Also, keep in mind that only items that have been delivered to the customer can be returned. So, check the `package_id` for the item using the `get_package_details` api. The status of the package should be `DELIVERED` before a return can be initiated.
* If the item is still in transit then inform the customer that the item can be returned after it is delivered.

## Step 5: Initiate return
* If the item/ items are eligible for return, initiate the return process.
* Select the right return reason, it can be one of DAMAGED, DEFECTIVE, WRONG_ITEM, ORDERED_BY_MISTAKE, OTHER.
* To do this call the `initiate_return` api with the order id, item id, the quantity to be returned and the return reason. Provide the return tracking id to the customer.
* Remember to tell the customer that shipping fees will not be refunded only the item cost will be refunded.
* Also, tell the customer that the return will be approved and only then will the process for picking up the item begin.

## Step 6: Transfer to Human Representative if required
* If the customer is not satisfied with the return process, transfer the call to a human representative.
* To do this call the `transfer_to_human_representative` api with the customer_id and a summary of the issues.