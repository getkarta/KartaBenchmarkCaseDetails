# get_package_details()

[![](https://img.shields.io/badge/type-update-red)](https://img.shields.io/badge/type-update-red) 


## Tool Class

Use with caution. This is a **domain specific** tool and is used to issue a gift card to a customer. Using this tool will change the state of the database. A gift card with a predetermined amount is issued to the customer and its details
are updated in payment_methods.

## Tool Function

Given a `customer_id` and an `amount` this tool issues a gift card to the customer with the specified amount. It will return an error message if the customer cannot be found or if the amount is not valid.

## Caveats

A specific customer id is required to issue a gift card. Amount should be a positive integer.

## Usage Example

```python-repl
gift_card = issue_gift_card(customer_id='CUST001001', amount=100)
```
