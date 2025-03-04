# get_order_details()

[![](https://img.shields.io/badge/type-read-green)](https://img.shields.io/badge/type-read-green) 
[![](https://img.shields.io/badge/Return%20Schema-Orders-orange)](https://img.shields.io/badge/Return%20Schema-Orders-orange)

## Tool Class

This is a **domain specific** tool and is used to get order details in an ecommerce context.

## Tool Function

Given an `order_id` this tool returns the details of the order from the orders dataset. It will return an error message if the order cannot be found. The details of the orders schema can be found in the data descriptions for this domain.

## Caveats

Many times customers will not provide their ID and not know it. So, use the customer email to retrieve customer details in such instances.

## Usage Example

```python-repl
order = get_order_details(order_id='ORD001001')
```