# get_return_details()

[![](https://img.shields.io/badge/type-read-green)](https://img.shields.io/badge/type-read-green) 
[![](https://img.shields.io/badge/Return%20Schema-Returns-orange)](https://img.shields.io/badge/Return%20Schema-Returns-orange)


## Tool Class

This is a **domain specific** tool and is used to get details of a specific return that has been initiated.

## Tool Function

Given a `return_id` this tool returns the details of the return from the returns dataset. It will return an error message if the return cannot be found. The details of the returns schema can be found in the data descriptions for this domain.

## Caveats

A specific return id is required to retrieve the return details. Usually the return id can be obtained from `active_returns` field in the customer details. Customers generally do not know the return id.

## Usage Example

```python-repl
return_details = get_return_details(return_id='RET001001')
```
