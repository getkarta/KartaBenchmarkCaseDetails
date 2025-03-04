# get_customer_by_id()

[![](https://img.shields.io/badge/type-read-green)](https://img.shields.io/badge/type-read-green) 
[![](https://img.shields.io/badge/Return%20Schema-Customers-orange)](https://img.shields.io/badge/Return%20Schema-Customers-orange)

## Tool Class

This is a **domain specific** tool and is used to get customer details in an ecommerce context.

## Tool Function

Given a `customer_id` this tool returns the details of the customer from the customers dataset. It will return an error message if the customer cannot be found. The details of the  customers schema can be found in the data descriptions for this domain.

## Caveats

Many times customers will not provide their ID and not know it. So, use the customer email to retrieve customer details in such instances.

## Usage Example

```python-repl
customer = get_customer_by_id(customer_id='CUST001001')
```
