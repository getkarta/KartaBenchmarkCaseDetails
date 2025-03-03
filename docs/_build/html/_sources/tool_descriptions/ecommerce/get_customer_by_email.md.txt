# get_customer_by_email()

## Tool Class

This is a **domain specific** tool and is used to get customer details in an ecommerce context. This is typically used when the customer does not have his / her customer id handy. 

## Tool Function

Given a `email` this tool returns the details of the customer from the customers dataset. It will return an error message if the customer cannot be found.

## Caveats

None

#### Usage Example

```python-repl
customer = get_customer_by_email(email='abhinav6671@somemail.com')
print(customer)
"""
{
	"first_name" : "Abhinav",
        "last_name" : "Kumar",
        "email" : "abhinav6671@somemail.com",
        "phone_number" : "+91 99999 88888",
        "date_of_birth" : "1994-01-01",
        "gender" : "Male",
        "account_creation_date" : "2024-01-01",
        "last_order_date" : "2025-02-01",
        "is_active" : true,
        "is_email_verified" : true,
        "is_phone_verified" : true,
        "is_fraud_flag" : false
}
"""
```
