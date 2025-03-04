# get_customer_by_email()

[![](https://img.shields.io/badge/type-read-green)](https://img.shields.io/badge/type-read-green) 
[![](https://img.shields.io/badge/Return%20Schema-Customers-orange)](https://img.shields.io/badge/Return%20Schema-Customers-orange) 

## Tool Class

This is a **domain specific** tool and is used to get customer details in an ecommerce context. This is typically used when the customer does not have his / her customer id handy.

## Tool Function

Given a `email` this tool returns the details of the customer from the customers dataset. It will return an error message if the customer cannot be found.


## Caveats

None

## Usage Example

```python-repl
customer = get_customer_by_email(email='abhinav6671@somemail.com')

"""
```
