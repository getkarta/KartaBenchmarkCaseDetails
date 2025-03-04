# transfer_to_human_representative()

[![](https://img.shields.io/badge/type-update-red)](https://img.shields.io/badge/type-update-red) 

## Tool Class

Use with caution. This is a **domain specific** tool and is used to transfer the call to a human representative. Using this tool will change the state of the database by adding a new contact record.

## Tool Function

Given a `customer_id` and a `summary_of_issues` this tool transfers the call to a human representative. 

## Caveats

A specific customer id is required to transfer the call to a human representative.

## Usage Example

```python-repl
transfer_to_human_representative(customer_id='CUST001001', 
summary_of_issues='The customer is having trouble with their order.')
```
